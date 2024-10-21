import streamlit as st
import seaborn as sns


# Load dataset
df= sns.load_dataset('titanic')

# Display dataset
st.dataframe(df)

