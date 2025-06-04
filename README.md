# DevLog - Application de Journalisation pour Développeurs
Description

DevLog est une application web simple permettant aux développeurs de créer et gérer des journaux de développement (logs). Chaque log contient du texte libre, des technologies utilisées, une humeur, une date et peut être affiché dans une interface web conviviale.

Cette application utilise Flask comme backend et serveur web, et MongoDB comme base de données NoSQL pour stocker les logs.
Fonctionnalités

    Ajouter un nouveau journal de développement via formulaire web

    Visualiser les logs récents avec détails (contenu, technologies, humeur, date)

    Backend REST API prêt à être étendu (routes CRUD JSON possibles)

    Utilisation de MongoDB pour la flexibilité et le stockage de documents JSON

Pourquoi MongoDB / NoSQL ?

    Les journaux ont des structures flexibles (tags, technologies, humeur, contenu variable)

    NoSQL permet de stocker des documents sans schéma rigide, facilitant les évolutions rapides

    Bonne gestion des données semi-structurées et non relationnelles

    Plus adapté à un modèle orienté documents que SQL traditionnel