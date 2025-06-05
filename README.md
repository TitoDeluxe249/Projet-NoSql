# 💎 ObsidianLog

ObsidianLog est une application web de journalisation à destination des développeurs. Elle permet de documenter quotidiennement ses sessions de code, d’exprimer son ressenti, de suivre les technologies utilisées et de mieux comprendre son propre rythme de travail. C’est un outil simple, élégant et personnel pour progresser dans sa pratique du développement logiciel.

---

## 🚀 Fonctionnalités

- ✍️ Ajout de journaux quotidiens avec :
  - contenu libre
  - humeur sélectionnable
  - liste de technologies utilisées
- 📅 Affichage des entrées de log récentes
- 🎨 Interface en **thème sombre obsidien** (inspiré de l'éditeur Obsidian)
- 🗂️ Utilisation de MongoDB pour stocker les données de manière flexible

---

## 🛠️ Stack technique

- **Frontend** : HTML, Bootstrap 5, CSS personnalisé
- **Backend** : Python 3 + Flask
- **Base de données** : MongoDB (NoSQL)

---

## 📦 Installation & Lancement

1. **Cloner le projet**
```bash
git clone https://github.com/TitoDeluxe249/Projet-NoSql/
```
---

2. **Créer et activer un environnement virtuel**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer MongoDB**

L’application utilise une base MongoDB locale (par défaut : mongodb://localhost:27017/)
Nom de la base : devlog
Collection : logs

5. **Lancer l’application**
```bash
python app.py
```
L’application est disponible à l’adresse : http://127.0.0.1:5000/


