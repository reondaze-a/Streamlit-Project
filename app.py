import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Calculate pokemon stats')

level = st.slider(1, 100, 5)
start_button = st.button('Calculate')

if start_button:
