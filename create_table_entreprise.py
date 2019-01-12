import pandas as pd
import numpy as np
import json
from sqlalchemy import create_engine

with open("data/Entreprises/globedreamersAssuranceVoyage.json") as datafile:
    data = json.load(datafile)
df_assurance_voyages = pd.DataFrame(data)
df_assurance_voyages['category'] = 'Assurance_Voyage'
print(df_assurance_voyages.shape)

with open("data/Entreprises/globedreamersDataset.json") as datafile:
    data = json.load(datafile)
df_entreprise = pd.DataFrame(data)
print(df_entreprise.shape)

df = pd.concat([df_entreprise, df_assurance_voyages], sort=True)
df = df.reset_index()
df = df.drop(['index'], axis=1)

# On supp tt les doublons
df_clean = df.drop_duplicates(subset='title', keep="first") 
df_clean = df_clean.reset_index(drop=True)
print("Shape finale doit être égale à (736,10) ==> ",df_clean.shape)

 # Supp les carac invalides
df_clean['presentation'] = df_clean.loc[:, 'presentation'].replace(regex=True, to_replace="\xa0", value="").replace(regex=True, to_replace="\n", value="").replace(regex=True, to_replace="\r", value="")

# majuscule des category
df_clean['category'] = df_clean['category'].str.upper()


create_db = 1

if create_db:
    engine = create_engine("mysql://root:root@localhost:3306/Entreprise_GlobeDreamers?charset=utf8")
    #if you want to create a new table 
    df_clean.to_sql(name='Entreprise_',con=engine,if_exists='fail',index=False)
    print("**BDD crée**")
