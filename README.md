# POSD System

Sviluppo di un’applicazione web che integri ogni elemento della PRIVACY KNOWLEDGE BASE e il mapping esistente tra tali elementi

## ⭐ Obiettivo caso di studio

- ⚔️ Supportare gli sviluppatori nella progettazione e reingegnerizzazione di sistemi orientati alla privacy e sicurezza
- ⚔️ Supportare le aziende nella definizione di processi compliance al GDPR

---

## 📚 Guida all'installazione (step-by-step)

### 🔧 Cosa installare sulla tua macchina

## 1. **Docker Desktop**
- Scarica Docker Desktop dal sito ufficiale:  
  👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- Una volta installato, avvialo e assicurati che sia attivo.  
  Verifica la presenza dell’icona della balena **verde** nella traybar per confermare che tutto funzioni correttamente.
  
  <img src="docs/image.png" alt="Docker" height="200px" />

## 2. **Git**
- Scarica Git dal sito ufficiale:  
  👉 [https://git-scm.com/](https://git-scm.com/)
- È necessario per **clonare il progetto** dal repository.

### **Video guida per l’installazione:**
- ▶️ [Git su Windows](https://www.youtube.com/watch?v=iYkLrXobBbA&ab_channel=CodeBear)
- ▶️ [Git su macOS](https://www.youtube.com/watch?v=9GZmaxaQV0c&ab_channel=Codingenthusiast)

3. **Browser moderno** (Chrome, Firefox, Edge ...)

---

## 🚀 Avvio rapido con Docker

- ▶️ [Video Tutorial ](https://streamable.com/rk93fv)

### 🧬 1. Clona il repository
```bash
git clone https://github.com/GiuseppePioDeBiase/Posd_System_Docker.git
cd Posd_System_Docker
```

### ⌨️ 2. Apri Terminale
Apri il terminale nella cartella del progetto clonato

### 🐳 3. Avvia tutto con Docker Compose
```bash
docker compose up --build -d
```

Questo avvia:
- MongoDB con backup 
- Backend Flask (porta `5000`)
- Frontend Vite (porta `5173`)

### 🌐 4. Apri nel browser
- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend: [http://localhost:5000](http://localhost:5000)

### 🔚 5. Chiudere tutto
Quando vuoi spegnere i container:
```bash
docker compose down
```
Questo fermerà tutti i servizi in modo sicuro.

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

## ⚙️ Approfondimento tecnico: Dockerfile e docker-compose.yml

👉 [Leggi il README tecnico](docs/README_TECNICO.md)

---

## 👤 Credenziali primo accesso (Amministratore)
<img src="Primoaccesso.png" alt="Primo accesso" width="400px"/>

🔐 Durante la registrazione sarà obbligatorio inserire una password che:
- contenga una **lettera maiuscola**, una **minuscola**, un **numero** e un **carattere speciale**
- sia lunga almeno **8 caratteri**

---

## 🎨 IDE & Strumenti

<code><img alt="PyCharm" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"/></code>
<code><img alt="mongoDB" width="60px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/MongoDB_Logo.svg/2560px-MongoDB_Logo.svg.png"/></code>
<code><img alt="Docker" width="60px" src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png"/></code>

---

## 🎓 Frameworks e Librerie

<code><img alt="Flask" width="60px" src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png"/></code>
<code><img alt="React" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/2300px-React-icon.svg.png"/></code>
<code><img alt="Vite" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Vitejs-logo.svg/2078px-Vitejs-logo.svg.png"/></code>
<code><img alt="Bootstrap" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/512px-Bootstrap_logo.svg.png"/></code>
<code><img alt="Tailwind" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/512px-Tailwind_CSS_Logo.svg.png?20230715030042"/></code>

---

## 💍 Crediti

Sviluppato da:

- [@GiuseppePioDeBiase](https://github.com/GiuseppePioDeBiase)
