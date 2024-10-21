# Terminal --> cd Dashboard -> Enter
# streamlit run Home.py

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as ps
import plotly.graph_objects as go

st.title('Titanic data analysis')

# Load dataset
df= sns.load_dataset('titanic')

# Display dataset
st.dataframe(df)

