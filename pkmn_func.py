# The functions I've created will be stored here so I can import it to the app2.py file
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# The function will take the input of the pokemon name , level, and the IVS and EVS
# and show the pokemon's stats at the specified level

data = pd.read_csv('Pokemon.csv')

colors = {
    "Bug": "#A6B91A",
    "Dark": "#705746",
    "Dragon": "#6F35FC",
    "Electric": "#F7D02C",
    "Fairy": "#D685AD",
    "Fighting": "#C22E28",
    "Fire": "#EE8130",
    "Flying": "#A98FF3",
    "Ghost": "#735797",
    "Grass": "#7AC74C",
    "Ground": "#E2BF65",
    "Ice": "#96D9D6",
    "Normal": "#A8A77A",
    "Poison": "#A33EA1",
    "Psychic": "#F95587",
    "Rock": "#B6A136",
    "Steel": "#B7B7CE",
    "Water": "#6390F0",
}



# list[0] increases attack, list[1] increases defense, list[2] increases special attack
# list[3] increases special defense, and list[4] increases speed
layout = go.Layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 250]
        )
    ),
    showlegend=True,
    title="Stat Graph"
)
# Importing the necessary libraries
nature_list = [
        ['Hardy', 'Lonely', 'Adamant', 'Naughty', 'Brave'],
        ['Bold', 'Docile', 'Impish', 'Lax', 'Relaxed'],
        ['Modest', 'Mild', 'Bashful', 'Rash', 'Quiet'],
        ['Calm', 'Gentle', 'Careful', 'Quirky', 'Sassy'],
        ['Timid', 'Hasty', 'Jolly', 'Naive', 'Serious']
    ]

def stats(name, level, nature, iv_hp=0, iv_atk=0, iv_def=0, iv_spatk=0, iv_spdef=0, iv_speed=0,
          ev_hp=0, ev_atk=0, ev_def=0, ev_spatk=0, ev_spdef=0, ev_speed=0):

    """
    This function will make a row that shows the pokemon's stats at a given level
    """

    # Taking the row of the pokemon's name and base stats

    pokemon = data[data['Name'] == name]

    # Copying and inputting the formula from the website here and applying it to each specific stat

    hp = (((2 * pokemon['HP'] + iv_hp + (ev_hp / 4)) * level) / 100) + level + 10

    attack = (((2 * pokemon['Attack'] + iv_atk + (ev_atk / 4)) * level) / 100) + 5

    defense = (((2 * pokemon['Defense'] + iv_def + (ev_def / 4)) * level) / 100) + 5

    special_attack = (((2 * pokemon['Sp. Atk'] + iv_spatk + (ev_spatk / 4)) * level) / 100) + 5

    special_defense = (((2 * pokemon['Sp. Def'] + iv_spdef + (ev_spdef / 4)) * level) / 100) + 5

    speed = (((2 * pokemon['Speed'] + iv_speed + (ev_speed / 4)) * level) / 100) + 5


    # Calculating nature into the equation
    # (based on the nature,
    # 2 stats will increase by 10% and the other decrease by
    # 10%.)


    # Calculate the natures that increase attack
    if nature in nature_list[0]:
        if nature != nature_list[0][0]:
            attack = attack * 1.1
        if nature == nature_list[0][1]:
            defense = defense * 0.9
        elif nature == nature_list[0][2]:
            special_attack = special_attack * 0.9
        elif nature == nature_list[0][3]:
            special_defense = special_defense * 0.9
        elif nature == nature_list[0][4]:
            speed = speed * 0.9

    #  Nature that increases defense
    elif nature in nature_list[1]:
        if nature != nature_list[1][1]:
            defense = defense * 1.1
        if nature == nature_list[1][0]:
            attack = attack * 0.9
        elif nature == nature_list[1][2]:
            special_attack = special_attack * 0.9
        elif nature == nature_list[1][3]:
            special_defense = special_defense * 0.9
        elif nature == nature_list[1][4]:
            speed = speed * 0.9

    # Nature that increases Special Attack
    elif nature in nature_list[2]:
        if nature != nature_list[2][2]:
            special_attack = special_attack * 1.1
        if nature == nature_list[2][0]:
            attack = attack * 0.9
        elif nature == nature_list[2][1]:
            defense = defense * 0.9
        elif nature == nature_list[2][3]:
            special_defense = special_defense * 0.9
        elif nature == nature_list[2][4]:
            speed = speed * 0.9

    # Nature that increases Special Defense
    elif nature in nature_list[3]:
        if nature != nature_list[3][3]:
            special_defense = special_defense * 1.1
        if nature == nature_list[3][0]:
            attack = attack * 0.9
        elif nature == nature_list[3][1]:
            defense = defense * 0.9
        elif nature == nature_list[3][2]:
            special_attack = special_attack * 0.9
        elif nature == nature_list[3][4]:
            speed = speed * 0.9

    # Nature that increases Speed
    elif nature in nature_list[4]:
        if nature != nature_list[4][4]:
            speed = speed * 1.1
        if nature == nature_list[4][0]:
            attack = attack * 0.9
        elif nature == nature_list[4][1]:
            defense = defense * 0.9
        elif nature == nature_list[4][2]:
            special_attack = special_attack * 0.9
        elif nature == nature_list[4][3]:
            special_defense = special_defense * 0.9

    total = attack + defense + special_attack + special_defense + speed

    # Creating the dictionary for the stats
    statdict = {
        'Name': name,
        'Level': level,
        'HP': hp,
        'Attack': attack,
        'Defense': defense,
        'Sp. Atk': special_attack,
        'Sp. Def': special_defense,
        'Speed': speed,
        'Total': total,
        'Nature': nature
    }
    # Making the dictionary into a dataframe and dropping all the decimals on the stats
    statframe = pd.DataFrame(statdict).astype('int', errors='ignore')

    return statframe


# Function for individual pokemon stat graphs

def plot_pkmn_stats(
        name, level, nature, ev_hp, ev_atk, ev_def, ev_spatk, ev_spdef, ev_speed
):

    statframe = stats(
        name, level, nature,
        ev_hp=ev_hp,
        ev_atk=ev_atk,
        ev_def=ev_def,
        ev_spatk=ev_spatk,
        ev_spdef=ev_spdef,
        ev_speed=ev_speed
    )

    pkmn_stat = statframe[statframe['Name'] == name]
    obj = go.Scatterpolar(

        r=[
            pkmn_stat['HP'].values[0],
            pkmn_stat['Attack'].values[0],
            pkmn_stat['Defense'].values[0],
            pkmn_stat['Sp. Atk'].values[0],
            pkmn_stat['Sp. Def'].values[0],
            pkmn_stat['Speed'].values[0],
            pkmn_stat['HP'].values[0]
        ],

        theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'HP'],
        marker=dict(color=colors[data[data['Name'] == name]['Type 1'].values[0]]),
        fill='toself',
        name=pkmn_stat['Name'].values[0]
    )

    return obj


def scatterplot_stats(type, x_axis, y_axis, size):
    typedata = data[(data['Type 1'] == type) | (data['Type 2'] == type)]

    fig = px.scatter(
        typedata,
        x=x_axis,
        y=y_axis,
        size=size,
        color='Generation',
        hover_name='Name',
        color_continuous_scale=px.colors.sequential.Viridis
    )

    return fig

# Plots histogram for individual input
def hist_stats_ind(type, stat):
    typedata = data[(data['Type 1'] == type) | (data['Type 2'] == type)]
    fig = px.histogram(typedata[stat])

    return fig

# Plots histogram for multiple inputs
def hist_stats_mul(type, type_2, stat):
    typedata = data[(data['Type 1'] == type) | (data['Type 2'] == type)]
    typedata2 = data[(data['Type 1'] == type_2) | (data['Type 2'] == type_2)]

    typedata = typedata.assign(**{"Type 1": type})
    typedata2 = typedata2.assign(**{"Type 1": type_2})
    concat = pd.concat([typedata, typedata2])

    fig = px.histogram(concat, x=stat, color='Type 1')

    return fig