# POSD System

Sviluppo di un’applicazione web che integri ogni elemento della PRIVACY KNOWLEDGE BASE e il mapping esistente tra tali elementi

## ⭐ Obiettivo caso di studio

- ⚔️ Supportare gli sviluppatori nella progettazione e reingegnerizzazione di sistemi orientati alla privacy e sicurezza
- ⚔️ Supportare le aziende nella definizione di processi compliance al GDPR

---

## 📚 Guida all'installazione (step-by-step)

### 🔧 Cosa installare sulla tua macchina

1. **Docker Desktop**
   - Scarica da [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
   - Avvialo e assicurati che sia attivo (balena verde nella traybar)

2. **Git**
   - Scarica da [https://git-scm.com/](https://git-scm.com/)
   - Serve per clonare il progetto

3. **Node.js** (consigliata versione 20.x)
   - Scarica da [https://nodejs.org/](https://nodejs.org/)
   - Include anche `npm` (Node Package Manager)

4. **Python 3.12** (solo per sviluppo manuale, opzionale)
   - Scarica da [https://www.python.org/](https://www.python.org/)
   - Aggiungi al `PATH` durante l'installazione

5. **Un editor di codice** (es. Visual Studio Code, PyCharm)

6. **Browser moderno** (Chrome, Firefox, Edge)

---

## 🚀 Avvio rapido con Docker

### 1. Clona il repository
```bash
git clone https://github.com/GiuseppePioDeBiase/POSD_System.git
cd POSD_System
```

### 2. Avvia tutto con Docker Compose
```bash
docker compose up --build -d
```

Questo avvia:
- MongoDB con restore automatico
- Backend Flask (porta `5000`)
- Frontend Vite (porta `5173`)

### 3. Apri nel browser
- Frontend: [http://localhost:5173](http://localhost:5173)
- API Backend: [http://localhost:5000/api](http://localhost:5000/api)

---

## 🛠️ Struttura del progetto
```
POSD_System/
├── backend/
├── frontend/
├── backup/              # Dump MongoDB
├── docker-compose.yml
```

---

## 🔄 Restore manuale del database
Se necessario, puoi eseguire il restore manualmente con:
```bash
docker compose exec compose_db mongorestore --drop --db POSD_System /backup/POSD_System
```

---

## 🔧 Sviluppo manuale senza Docker (opzionale)

### Backend (Flask)
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # o source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Frontend (React/Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## 👤 Credenziali primo accesso (Amministratore)
<img src="Primoaccesso.png" alt="Primo accesso" width="400px"/>

---

## 🎨 IDE & Strumenti

<code><img alt="PyCharm" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"/></code>
<code><img alt="mongoDB" width="60px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/MongoDB_Logo.svg/2560px-MongoDB_Logo.svg.png"/></code>

---

## 🎓 Frameworks

<code><img alt="Flask" width="60px" src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png"/></code>
<code><img alt="React" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/2300px-React-icon.svg.png"/></code>
<code><img alt="Vite" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Vitejs-logo.svg/2078px-Vitejs-logo.svg.png"/></code>
<code><img alt="Bootstrap" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/512px-Bootstrap_logo.svg.png"/></code>
<code><img alt="Tailwind" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/512px-Tailwind_CSS_Logo.svg.png?20230715030042"/></code>

---

## 💍 Crediti

Sviluppato da:

- [@GiuseppePioDeBiase](https://github.com/GiuseppePioDeBiase)
