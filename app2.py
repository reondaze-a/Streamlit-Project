import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import pkmn_func as pf


# State for reserving the previous runs
if 'Table' not in st.session_state:
    st.session_state['Table'] = pd.DataFrame(columns=[
        'Name', 'Level', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total', 'Nature'])

naturelist = pd.Series([x for l in pf.nature_list for x in l])

st.title('Calculate Pokemon stats')

st.markdown("This app is used to calculate the stats of a pokemon at a certain level, as well as compare "
            "them to one another. A radar plot will be shown to visualize the numbers and have a better "
            "perspective of it.")

name = st.selectbox("Select Pokemon", pf.data['Name'])
nature_select = st.selectbox("Select nature", naturelist)

# Enter EVs through input
st.write("Enter EVs")
ev_hp = st.number_input('HP', 0, 255)
ev_atk = st.number_input('Attack', 0, 255)
ev_def = st.number_input('Defense', 0, 255)
ev_spatk = st.number_input('Sp. Atk', 0, 255)
ev_spdef = st.number_input('Sp. Def', 0, 255)
ev_speed = st.number_input('Speed', 0, 255)

total_evs = ev_hp + ev_atk + ev_def + ev_spatk + ev_spdef + ev_speed

level = st.slider('Pokemon level', 1, 100, 5)

if total_evs <= 510:
    start_button = st.button('Calculate')

    if start_button:
        pokemon = pf.plot_pkmn_stats(
            name, level, nature_select,
            ev_hp,
            ev_atk,
            ev_def,
            ev_spatk,
            ev_spdef,
            ev_speed

        )
        df = pf.data[pf.data['Name'] == name]
        st.write(df)

        st.plotly_chart(go.Figure(data=pokemon, layout=pf.layout))

        stat_frame = pf.stats(
            name, level, nature_select,
            ev_hp=ev_hp,
            ev_atk=ev_atk,
            ev_def=ev_def,
            ev_spatk=ev_spatk,
            ev_spdef=ev_spdef,
            ev_speed=ev_speed
        )

        st.session_state['Table'] = pd.concat([
            st.session_state['Table'],
            stat_frame],
            axis=0
        )


elif total_evs > 510:
    st.write('Total EVs must not exceed 510.')
    start_button = st.button('Calculate', disabled=True)


st.write(st.session_state['Table'])


