# Modèles

Ce dossier est prévu pour documenter les modèles entraînés dans le cadre du projet.

Les fichiers de modèles lourds ne sont pas versionnés dans GitHub.

## Modèle final

Le modèle final est entraîné dans le notebook :

```text
notebooks/02_modelisation_supervisee.ipynb
```

Il est ensuite sauvegardé pour être utilisé par l'API BentoML.

## BentoML

Le modèle utilisé par l'API est géré via le store local de BentoML.

La logique de chargement du modèle est définie dans :

```text
api/service.py
```

Le fichier de configuration du service est :

```text
api/bentofile.yaml
```

## Remarque

Pour reproduire le modèle, il faut exécuter le notebook de modélisation, puis sauvegarder le modèle selon la logique utilisée dans le projet.
