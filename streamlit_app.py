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
  bill_length_mm = st.slider('Bill length(mm):', 32.1, 59.6, 43)
  bill_depth_mm = st.slider('Bill depth(mm):',13.10, 25.50, 17.16)
  flipper_length_mm = st.slider('Flipper length(mm):',181,231,205)
  body_mass_g = st.slider('body_mass(g):', 2700, 6300, 4000)
