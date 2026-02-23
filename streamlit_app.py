import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
X_raw = df.drop('species', axis=1)
y_raw = df['species']

st.title('🤖 Pinguim ML')
st.info('Aplicativo de Classificacao de Especies de Pinguim 🐧')

with st.expander('Dataset'):
  st.write('**Dados Brutos**')
  df

with st.expander('Visualizacao de Dados'):
  st.scatter_chart(df, 
                   x='bill_length_mm', 
                   y='body_mass_g', 
                   color='species',
                   y_label = 'massa corporal (g)',
                   x_label = 'comprimento bico (mm)'
                  )

with st.sidebar:
  st.header('Entrada de Atributos')
  island = st.selectbox('Ilha:', df['island'].unique())
  gender = st.selectbox('Genero:', df['sex'].unique())
  bill_length_mm = st.slider('Comprimento do Bico (mm):',float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()), float(df['bill_length_mm'].mean()))
  bill_depth_mm = st.slider('Profundidade do Bico (mm):', float(df['bill_depth_mm'].min()), float(df['bill_depth_mm'].max()), float(df['bill_depth_mm'].mean()))
  flipper_length_mm = st.slider('Comprimento da Nadadeira (mm):', float(df['flipper_length_mm'].min()), float(df['flipper_length_mm'].max()), float(df['flipper_length_mm'].mean()))
  body_mass_g = st.slider('Massa Corporal (g):', float(df['body_mass_g'].min()), float(df['body_mass_g'].max()), float(df['body_mass_g'].mean()))

#Dataframe dos dados de entrada
data = {'island' : island,
        'bill_length_mm' : bill_length_mm,
        'bill_depth_mm' : bill_depth_mm,
        'flipper_length_mm' : flipper_length_mm,
        'body_mass_g' : body_mass_g,
        'sex' : gender}

input_df = pd.DataFrame(data, index=[0]) 
input_penguin = pd.concat([input_df,X_raw], axis=0) 

with st.expander('Dados de Entrada'):
  input_df

#Data preparation (encode X)
encode = ['island','sex']
df_penguin = pd.get_dummies(input_penguin,columns=encode,prefix=encode)

X = df_penguin[1:]
input_row = df_penguin[:1]

#encode y
target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

#Treinamento do modelo
modelo = RandomForestClassifier()
modelo.fit(X,y)

#Predicao
prediction = modelo.predict(input_row)
prediction_proba = modelo.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie',
                                 1: 'Chinstrap',
                                 2: 'Gentoo'})


