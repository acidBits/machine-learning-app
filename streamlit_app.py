import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

st.title('Machine Learning App')
st.info('This app buils a machine learning model!')

with st.expander('Dados'):
  st.write('**Dados Brutos**')
  df

with st.expander('Visualizacao de Dados'):
  st.scatter_chart(df,x='bill_length_mm',y='body_mass_g',color='species')

with st.sidebar:
  st.header('Entrada de Atributos')
  island = st.selectbox('Island:', df['island'].unique())
  gender = st.selectbox('Gender:', df['sex'].unique())
  bill_length_mm = st.slider('Bill length(mm):', df['bill_length_mm'].min(), df['bill_length_mm'].max(), df['bill_length_mm'].mean())
  bill_depth_mm = st.slider('Bill depth(mm):', df['bill_depth_mm'].min(), df['bill_depth_mm'].max(), df['bill_depth_mm'].mean())
  
  body_mass_g = st.slider('body_mass(g):', 0,10, 5)
