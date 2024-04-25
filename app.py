import streamlit as st
import pandas as pd
import plotly.express as px
import pkmn_func as pf

st.header('Calculate pokemon stats')

st.markdown("This app is used to calculate the stats of a pokemon at a certain level, as well as compare "
            "them to one another. A radar plot will be shown to visualize the numbers and have a better "
            "perspective of it.")

level = st.slider(1, 100, 5)
start_button = st.button('Calculate')

#if start_button:
