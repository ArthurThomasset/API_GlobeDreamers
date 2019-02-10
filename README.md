# API Globedreamers

## Présentation 

GlobeDreamers est la première plateforme de financement participatif pour les voyageurs, elle vise à développer des projets à impact positifs au niveau environnemental et humanitaire.

Un enjeu majeur de GlobeDreamers pour les entreprises est notamment d’humaniser leurs marques et engager leurs communautés à travers des valeurs qui leurs sont propres en sponsorisant ces projets.

Pour ce faire, GlobeDreamers doit se doter d’un outil de recommandation de prospects performant afin d’améliorer les financements et la visibilité des projets qu’elle propose et ainsi aider les business développeurs dans le choix de leurs partenaires.

Les objectifs de départ étaient de fournir une interface web permettant de donner un projet en entrée, pour avoir une liste d’entreprises à contacter afin de financer un projet.

## Description technique 

### Fonctionnement 

Le fonctionnement du projet est décomposé en 2 parties : 
  - La partie exploratoire où nous avons crée les algorithmes de recommendations
  - La partie API avec Flask où nous utilisons les résultats de la partie exploratoire dans l'API afin de servir la partie web

### Arborescence

```bash
/app 

 -/static (partie web)
 
  --/js
   --- .script.js
   
  --/css
   --- .style.css

 -/template (partie web)
  -- .index.html
 
 - .__init__.py
 
 - .routes.py

/data

 -/Entreprises (Données d'entreprises)

 -/Projets (Données de projets)

/modeles (modèles à importer et algo V1 et V2)

/venv (contient les librairies)

.flaskenv

.gitignore

.api_flask.py

.bdd_entreprise_globedreamers.sql

.create_table_entreprise.py

.README.md

.requirements.txt 
```

## Initialisation du projet

### Installation de l'environnement virtuel

Se mettre dans un nouveau répertoire et créer un environnement virtuel 

```
python -m venv venv
```

Activer l'environnement virtuel

```
venv\Scripts\activate
```

Une fois dans l'environnement virtuel, installer les librairies nécaissaires

```
pip install –r requirements.txt
```

### Créer la bdd et la table Entreprise

- Se connecter sur le serveur local MySQL depuis Workbench (renseigner )

- Ouvrir dans workbench le fichier "bdd_entreprise_globedreamers.sql" et éxécuter seulement la 1ere ligne

- Vérifier que la bdd Entreprise_GlobeDreamers a bien été crée

- Ouvrir le script "create_table_entreprise.py" et passer la variable "create_db" à 1 

- CD API_Flask puis lancer l'environnement virtuel et éxécuter le script "create_table_entreprise.py" pour créer et remplir les données d'entreprises

```
$python create_table_entreprise.py
```

- Vérifier que la table "Entreprise" a bien été crée dans la bdd "Entreprise_GlobeDreamers" en éxécutant les autres lignes de "bdd_entreprise_globedreamers.sql"

- Pour finir installer le module "Allow-Control-Allow-Origin: *" et l'activer pour utiliser l'API


Lien utile pour comprendre comment Flask fonctionne : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
