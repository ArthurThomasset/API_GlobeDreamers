from flask import Flask, request, render_template, jsonify
from app import app
import numpy as np 
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle 


with open('modeles/oneHotEncoding_matrix_entreprise.pkl', 'rb') as d:
    oneHotEncoding_matrix_entreprise = pickle.load(d)
    print("Done")

with open('modeles/oneHotEncoding_model.pkl', 'rb') as d:
    oneHotEncoding_model = pickle.load(d)
    print("Done")


with open('modeles/indices_entreprise.pkl', 'rb') as d:
    indices_entreprise = pickle.load(d)
    print("Done")
    

# Route home qui permet d'afficher l'index
@app.route('/')
def home():
    return render_template('index.html')


# Route prediction qui permet de récupérer les données et de faire la prédiction
@app.route('/prediction', methods=['POST'])
def prediction():
    category = str(request.form.get('category')).upper()                               
    category = [[category]]  
    print(category)                             

    #Encode la catégorie du projet suivant le modèle de One Hot Encoding
    new_matrix_entreprise = oneHotEncoding_model.transform(category)

    #Calcul la sim par cosin entre la matrice du projet et celle de l'entreprise
    distance_sim_entreprise = linear_kernel(new_matrix_entreprise, oneHotEncoding_matrix_entreprise)

    # recup les scores de similarité de tt les autres entreprises par rapport aux param
    sim_scores = list(enumerate(distance_sim_entreprise[0]))

    # trie les entreprises par score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # top 10 des plus similaires
    sim_scores = sim_scores[0:11]

    # recup les index des entreprises avec les meilleurs score
    idx_entreprises = [i[0] for i in sim_scores]

    reponse = list(indices_entreprise[idx_entreprises])

    print(reponse)
                                                          
    return jsonify(reponse)   
