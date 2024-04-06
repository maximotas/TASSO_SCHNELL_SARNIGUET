# API UniteAI - Exploration des Nouvelles sur l'Intelligence Artificielle

Ce projet développe une API Flask qui interagit avec des données d'articles sur l'intelligence artificielle du site [Unite.AI](https://www.unite.ai/category/artificial-intelligence/). Outre la récupération des données des articles, l'API offre une fonctionnalité de visualisation sous forme de nuages de mots pour résumer les thèmes abordés.

## Fonctionnalités Principales

- Page d'accueil qui oriente vers les différentes actions possibles.
- Liste des derniers articles sur l'IA incluant titre, lien, et date de publication.
- Détails sur un article spécifique via son identifiant.
- Visualisation de nuages de mots basée sur le contenu des articles.

## Installation et Lancement

1. **Téléchargez** le projet sous forme de fichier zip et **extrayez-le** dans un dossier de votre choix.
2. Ouvrez une fenêtre de commande (CMD) dans ce dossier (Astuce : tapez `cmd` dans la barre d'adresse du dossier et appuyez sur Entrée).
3. **Installez** les dépendances nécessaires avec la commande : `pip install -r requirements.txt`.
4. **Exécutez** `main.py` pour démarrer le serveur Flask.

Une fois le serveur démarré, rendez-vous sur [http://127.0.0.1:5000](http://127.0.0.1:5000) dans votre navigateur pour accéder à l'API. Veuillez patienter le temps que les données se chargent à chaque action.

## Structure du Code

Le projet est structuré comme suit :

- `main.py` sert de point d'entrée pour démarrer l'application Flask.
- Le dossier `templates` contient des fichiers HTML pour l'affichage des données dans le navigateur.
- `UniteIA_scraper.py` est responsable du scraping des données depuis le site Unite.AI en utilisant Selenium. Ce fichier contient la logique pour extraire les informations nécessaires telles que les titres, les liens, et les dates de publication des articles.
- `requirements.txt` liste toutes les bibliothèques Python nécessaires au projet.

Ce choix de structure et de technologies vise à simplifier l'utilisation et l'extension de l'API.

## Démarrage Rapide

Pour visualiser les articles et générer des nuages de mots, suivez les instructions et liens fournis sur la page d'accueil de l'API.

## Auteurs

- TASSO Maximo
- SCHNELL Clément
- SARNIGUET Nicolas

