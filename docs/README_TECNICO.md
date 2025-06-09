# 📘 Dettagli tecnici: Dockerfile e docker-compose.yml

## 🔨 Dockerfile (Backend)

Il `Dockerfile` del backend esegue questi step:

1. Usa l'immagine base `python:3.12-slim`.
2. Imposta la directory di lavoro in `/backend`.
3. Copia `requirements.txt` e installa le dipendenze.
4. Copia l'intero codice sorgente del backend.
5. Espone la porta `5000`.
6. Avvia l'app con `CMD ["python", "app.py"]`.

```dockerfile
FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 🔨 Dockerfile (Frontend)

Il Dockerfile del frontend costruisce e avvia l'interfaccia React con Vite:

```dockerfile
FROM node:20-alpine

WORKDIR /frontend

COPY package.json ./

COPY . .

RUN npm install -g npm@latest

RUN npm install --legacy-peer-deps

RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "dev"]
```

---

## ⚙️ docker-compose.yml

Definisce tre servizi principali:

```yaml
services:
  compose_backend:
    build: /backend
    container_name: compose_backend
    ports:
      - "5000:5000"
    depends_on:
      - mongodb
    networks:
      - evoluzione-del-software
    restart: unless-stopped
    command: python app.py

  frontend:
    build: /frontend
    container_name: compose_frontend
    ports:
      - "5173:5173"
    depends_on:
      - compose_backend
    networks:
      - evoluzione-del-software
    restart: unless-stopped
    command: npm run dev

  mongodb:
    image: mongo:7
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - ./backup:/backup
    networks:
      - evoluzione-del-software
    restart: unless-stopped
    command: >
      bash -c "
         mongod --bind_ip_all &
         sleep 5 &&
         mongorestore --drop --db POSD_System /backup/POSD_System &&
         wait -n
      "

volumes:
  mongodb_volumes:
    name: mongodb_volumes

networks:
  evoluzione-del-software:
    name: evoluzione-del-software
    driver: bridge
```

---

## 🔗 Networking

Tutti i container usano una rete bridge chiamata `evoluzione-del-software`, permettendo loro di comunicare usando i nomi dei servizi.

---

## 📦 Volumi

Il volume `mongodb_volumes` conserva i dati anche dopo lo stop del container MongoDB.

---

## 🛑 Spegnimento

Usa:
```bash
docker compose down
```
per fermare e rimuovere i container in modo ordinato.

Per rimuovere anche volumi e immagini:
```bash
docker compose down -v --rmi all
```
