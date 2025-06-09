# 📘 Dettagli tecnici: Dockerfile e docker-compose.yml

## 🔨 Dockerfile (Backend)

Il `Dockerfile` del backend esegue questi step:

1. Usa l'immagine base `python:3.12-slim`.
2. Imposta la directory di lavoro in `/backend`.
3. Copia `requirements.txt` e installa le dipendenze.
4. Copia l'intero codice sorgente del backend.
5. Espone la porta `5000`.
6. Avvia l'app con `CMD ["python", "app.py"]`.

Esempio semplificato:

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

## ⚙️ docker-compose.yml

Definisce tre servizi principali:

### 📦 `mongodb`
- Immagine: `mongo:7`
- Porta: `27017:27017`
- Volume montato per i backup
- Ripristino automatico del dump con `mongorestore`

### 📦 `backend`
- Build dalla cartella `backend`
- Porta esposta `5000:5000`
- Dipende da MongoDB
- Comunica usando `mongodb:27017`

### 📦 `frontend`
- Build dalla cartella `frontend`
- Porta esposta `5173:5173`
- Avviato con `npm run dev`

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
