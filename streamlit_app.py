import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

st.title('Machine Learning App')
st.info('This app buils a machine learning model!')

with st.expander('Dados'):
  st.write('**Dados Brutos**')
  df

with st.expander('Visualizacao de Dados'):
  st.scatter_chart(df,x='bill_length_mm',
                   y='body_mass_g',
                   color='species', 
                   y_label="Massa Corporal(g)",
                   title="Relação entre Comprimento do Bico e Massa Corporal"
  )

with st.sidebar:
  st.header('Entrada de Atributos')
  island = st.selectbox('Island:', df['island'].unique())
  gender = st.selectbox('Gender:', df['sex'].unique())
  bill_length_mm = st.slider('Bill length(mm):',float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()), float(df['bill_length_mm'].mean()))
  bill_depth_mm = st.slider('Bill depth(mm):', float(df['bill_depth_mm'].min()), float(df['bill_depth_mm'].max()), float(df['bill_depth_mm'].mean()))
  flipper_length_mm = st.slider('flipper_length(mm):', float(df['flipper_length_mm'].min()), float(df['flipper_length_mm'].max()), float(df['flipper_length_mm'].mean()))
  body_mass_g = st.slider('body_mass(g):', float(df['body_mass_g'].min()), float(df['body_mass_g'].max()), float(df['body_mass_g'].mean()))

#Dataframe dos dados de entrada
data = {'Island' : island,
        'bill_length_mm' : bill_length_mm,
        'bill_depth_mm' : bill_depth_mm,
        'flipper_length_mm' : flipper_length_mm,
        'body_mass_g' : body_mass_g,
        'Sex' : gender}

input_df = pd.DataFrame(data, index=[0])

with st.expander('Dados de Entrada'):
  input_df

#Encode
encode = ['island','gender']
df_penguins = pd.get_dummies(input_df, prefix=encode)
df_penguins
