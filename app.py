import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import pkmn_func as pf
import numpy as np


st.title('Pokemon stats Plots')
st.write("This web-app will show the correlation between the chosen stats of selected types over Generations.")

st.header("Select Type(s)")
type_list1 = pf.data['Type 1'].unique()
type_list2 = np.insert(type_list1, 0,  'None')

type = st.selectbox("Choose Type", type_list1)
show = st.checkbox("Use 2nd Type")
if show:
    type2 = st.selectbox("Choose 2nd Type", type_list2)
else:
    type2 = "None"


st.subheader("Scatterplot")

stat_x = st.selectbox("Choose stat for X-axis", ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
stat_y = st.selectbox("Choose stat for Y-axis", ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
stat_size = st.selectbox("Choose stat for Size of plot", ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

start_scatter = st.button("Create Scatterplot")

st.subheader("Histogram")

compared_stat = st.selectbox("Choose stats", ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

start_hist = st.button("Create Histogram")

if start_scatter:
    if type2 == 'None':

        st.subheader(f"{type}")
        st.plotly_chart(pf.scatterplot_stats(type, x_axis=stat_x, y_axis=stat_y, size=stat_size))

    else:
        st.subheader(f"{type}")
        st.session_state['Graph'] = st.plotly_chart(pf.scatterplot_stats(type, x_axis=stat_x, y_axis=stat_y, size=stat_size), theme='streamlit')
        st.subheader(f"{type2}")
        st.plotly_chart(pf.scatterplot_stats(type2, x_axis=stat_x, y_axis=stat_y, size=stat_size))


if start_hist:
    if type2 == 'None':
        st.subheader(f"{type}")
        st.plotly_chart(pf.hist_stats_ind(type, compared_stat))

    else:
        st.subheader(f"{type} vs {type2}")
        st.plotly_chart(pf.hist_stats_mul(type, type2, compared_stat))


