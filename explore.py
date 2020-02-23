import utility as ut
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from random import randint

def run():
    q = st.selectbox("What are you looking for?", ("Locations", "Animals", "Plants"))
    user_input = ""
    if q == "Locations":
        user_input = st.text_input("enter location")
    elif q == "Animals":
        user_input = st.text_input("enter animal")
    elif q == "Plants":
        user_input = st.text_input("enter plant")

    start_loc=[51.5262, -0.1607]
    zoo_loc = [51.5353,-0.1534]

    if user_input == "":
        df = pd.DataFrame(
            np.array([start_loc]), columns=['lat', 'lon'])
        st.map(df, zoom = 13)
    elif user_input == 'lion' or user_input == 'tiger' or user_input == 'giraffe':
        df = pd.DataFrame(
            np.array([zoo_loc]), columns=['lat', 'lon'])
        st.map(df, zoom = 13) 
    elif user_input == 'pigeon' or user_input == 'rat' or user_input == 'grass':
        n = randint(100,200)
        df = pd.DataFrame(
            np.random.randn(n, 2) / [200, 200] + start_loc, columns=['lat', 'lon'])
        st.map(df) 
    else:
        n = randint(10,70)
        df = pd.DataFrame(
            np.random.randn(n, 2) / [200, 200] + start_loc, columns=['lat', 'lon'])
        st.map(df)
