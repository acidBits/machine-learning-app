import streamlit as st
import pandas as pd

st.title('Machine Learning App')
st.info('This app buils a machine learning model!')

with st.expander('Data'):
  st.write('**Dados Brutos**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
