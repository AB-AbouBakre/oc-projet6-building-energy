# Projet 6 — Anticipez les besoins en consommation de bâtiments

## Contexte

Ce projet s'inscrit dans un contexte de transition énergétique pour la ville de Seattle.
L'objectif est de prédire la consommation énergétique de bâtiments non résidentiels à partir de leurs caractéristiques 
structurelles : surface, usage, année de construction, localisation, nombre d'étages, etc.

Les relevés réels de consommation étant coûteux à obtenir, le but est de construire un modèle capable d'estimer la consommation 
énergétique d'un bâtiment à partir de données disponibles en amont.

## Objectifs du projet

Le projet est organisé en deux parties :

### Partie 1 — Modélisation supervisée

* Réaliser une analyse exploratoire des données.
* Nettoyer et filtrer les bâtiments non pertinents ou incohérents.
* Créer de nouvelles variables explicatives.
* Préparer les features pour la modélisation.
* Comparer plusieurs modèles de régression.
* Optimiser le meilleur modèle.
* Identifier les variables ayant le plus d'impact sur la prédiction.

### Partie 2 — API et déploiement

* Sauvegarder le modèle entraîné.
* Créer une API avec BentoML.
* Ajouter une logique de validation des données d'entrée.
* Tester l'API en local.
* Containeriser le service.
* Déployer l'API sur Google Cloud Run.

## Structure du dépôt

```text
.
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   ├── 01_eda_feature_engineering.ipynb
│   └── 02_modelisation_supervisee.ipynb
│
├── api/
│   ├── service.py
│   ├── bentofile.yaml
│   └── test_api.sh
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── docs/
│
└── reports/
```

## Données

Le jeu de données utilisé correspond aux données de consommation énergétique des bâtiments de Seattle.

Le fichier source `Building_Energy.csv` n'est pas versionné dans ce dépôt afin d'éviter de stocker un fichier de données 
volumineux dans GitHub.

Pour exécuter les notebooks, il faut placer le fichier CSV localement dans le dossier `data/`.

## Notebooks

Les notebooks sont organisés dans le dossier `notebooks/`.

### `01_eda_feature_engineering.ipynb`

Ce notebook contient :

* la découverte du jeu de données ;
* le nettoyage initial ;
* le filtrage des bâtiments ;
* l'analyse exploratoire ;
* la création de nouvelles features ;
* la préparation des données pour la modélisation.

### `02_modelisation_supervisee.ipynb`

Ce notebook contient :

* la préparation finale des jeux d'entraînement et de test ;
* la comparaison de plusieurs modèles supervisés ;
* l'évaluation avec plusieurs métriques ;
* l'optimisation du meilleur modèle ;
* l'analyse des variables les plus importantes ;
* la sauvegarde du modèle pour l'API.

## Modélisation

Le problème traité est un problème de régression supervisée.

La variable cible principale est la consommation énergétique du bâtiment.
Plusieurs modèles ont été comparés avec une démarche cohérente :

* séparation train / test ;
* validation croisée ;
* comparaison des métriques ;
* optimisation des hyperparamètres ;
* interprétation du modèle final.

Les métriques utilisées incluent notamment :

* R² ;
* MAE ;
* RMSE.

## API

L'API est développée avec BentoML.

Les fichiers liés à l'API sont dans le dossier `api/`.

### Lancement local

Depuis la racine du projet :

```bash
bentoml serve api/service.py:svc
```

### Test de l'API

Un script de test est disponible :

```bash
bash api/test_api.sh
```

L'API reçoit les caractéristiques d'un bâtiment et renvoie une prédiction de consommation énergétique.

## Déploiement

L'API a été containerisée puis déployée sur Google Cloud Run.

Le fichier `api/bentofile.yaml` décrit les éléments nécessaires à la construction du service BentoML.

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Auteur

Projet réalisé dans le cadre du parcours OpenClassrooms — Data Engineer / Machine Learning.

