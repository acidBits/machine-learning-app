import streamlit as st

st.title('Machine Learning App')
st.info('This app buils a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
st.write(df.head(10))
