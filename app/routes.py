from flask import Flask, request, render_template
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
    print(category)                                        
    category = [[category]]  
    print(category)                             

    new_matrix_entreprise = oneHotEncoding_model.transform(category)

    distance_sim_entreprise = linear_kernel(new_matrix_entreprise, oneHotEncoding_matrix_entreprise)

    cosin_max = distance_sim_entreprise.max()

    index = np.where(distance_sim_entreprise == cosin_max)

    reponse = indices_entreprise[index[1][0]]

                                                          
    return ("Entreprises : {0}").format(reponse)      
