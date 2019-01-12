# python -m venv venv

# venv\Scripts\activate

# pip install –r requirements.txt

## Créer la bdd et la table Entreprise

# Se connecter sur le serveur local MySQL depuis Workbench

# Ouvrir dans workbench le fichier "bdd_entreprise_globedreamers.sql" et éxécuter seulement la 1ere ligne

# Vérifier que la bdd Entreprise_GlobeDreamers bien été crée

# Ouvrir le script "create_table_entreprise.py" et passer la variable "create_db" à 1

# CD API_Flask puis lancer l'environnement virtuel et éxécuter le script "create_table_entreprise.py" 
($python create_table_entreprise.py)

# Vérifier que la table "Entreprise" a bien été crée dans la bdd "Entreprise_GlobeDreamers" en éxécutant les autres lignes de "bdd_entreprise_globedreamers.sql"