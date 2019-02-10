from flask import Flask, request, render_template, jsonify
from app import app
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
from flaskext.mysql import MySQL

# Chargement des fichiers nécaissaires pour la partie recommandation 
with open('modeles/oneHotEncoding_matrix_entreprise.pkl', 'rb') as d:
    oneHotEncoding_matrix_entreprise = pickle.load(d)
    print("Done")

with open('modeles/oneHotEncoding_model.pkl', 'rb') as d:
    oneHotEncoding_model = pickle.load(d)
    print("Done")


with open('modeles/indices_entreprise.pkl', 'rb') as d:
    indices_entreprise = pickle.load(d)
    print("Done")

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Entreprise_GlobeDreamers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

# Route home qui permet d'afficher l'index
@app.route('/')
def home():
    return render_template('index.html')


# Route prediction qui permet de récupérer les données et faire la prédiction
@app.route('/prediction', methods=['POST'])
def prediction():
    category = str(request.form.get('category')).upper()
    print(category)
    code_postal = int(request.form.get('code_postal'))
    print(code_postal)

    df_sim_param = pd.DataFrame({'code_postaux':[code_postal], 'category':[category]})

    ###########
    #Calcul de similarité pour la recommandation
    ###########

    #Encode la catégorie du projet suivant le modèle de One Hot Encoding
    new_matrix_projet = oneHotEncoding_model.transform(df_sim_param)

    #Calcul la similarité par cosin entre la matrice du projet et celle des entreprises
    distance_sim_entreprise = linear_kernel(new_matrix_projet, oneHotEncoding_matrix_entreprise)

    # Récupére  les scores de similarité de toutes les autres entreprises
    sim_scores = list(enumerate(distance_sim_entreprise[0]))

    # Trie les entreprises par score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Top 10 des plus similaires
    sim_scores = sim_scores[0:11]

    # Récupére  les index des entreprises avec les meilleurs scores
    idx_entreprises = [i[0] for i in sim_scores]

    # Récupére  les noms des entreprises
    l_titre_entreprise = list(indices_entreprise[idx_entreprises])

    ###########
    #Affichage via BDD MySQL
    ###########
    cursor = mysql.connect().cursor()

    liste_json_entreprise = []
	
	# Crée un json avec le résultats des requetes pour chaque titre d'entreprise dans la bdd MySQL afin de récupérer toutes les informations
    for titre_ in l_titre_entreprise:
    	cursor.execute("SELECT * FROM Entreprise as E WHERE E.title = %s" , [titre_])
    	requete_Information_Entreprise = cursor.fetchall()
    	liste_json_entreprise.append(requete_Information_Entreprise)


    print(liste_json_entreprise)


   ##########

    return jsonify(liste_json_entreprise)
