# API Globedreamers

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

- Se connecter sur le serveur local MySQL depuis Workbench

- Ouvrir dans workbench le fichier "bdd_entreprise_globedreamers.sql" et éxécuter seulement la 1ere ligne

- Vérifier que la bdd Entreprise_GlobeDreamers a bien été crée

- Ouvrir le script "create_table_entreprise.py" et passer la variable "create_db" à 1 

- CD API_Flask puis lancer l'environnement virtuel et éxécuter le script "create_table_entreprise.py" pour créer et remplir les données d'entreprises

```
$python create_table_entreprise.py
```

- Vérifier que la table "Entreprise" a bien été crée dans la bdd "Entreprise_GlobeDreamers" en éxécutant les autres lignes de "bdd_entreprise_globedreamers.sql"