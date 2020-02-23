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


    if user_input == "":
        df = pd.DataFrame(
            np.random.randn(1, 2) / [250, 250] + [51.52903, -0.155], columns=['lat', 'lon'])
        st.map(df, zoom = 14)
    elif user_input == "Regents Park":
        n = randint(10,100)
        df = pd.DataFrame(
            np.random.randn(n, 2) / [250, 250] + [51.52903, -0.155], columns=['lat', 'lon'])
        st.map(df, zoom = 14)
    else:
        n = randint(10,100)

        df = pd.DataFrame(
            np.random.randn(n, 2) / [300, 300] + [51.52903, -0.155], columns=['lat', 'lon'])
        st.map(df, zoom = 14)
