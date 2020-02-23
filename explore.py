import utility as ut
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

def run():
    ph1 = st.empty()
    ph2 = st.empty()
    ph3 = st.empty()

    '''
    if ut.state.flag_rerunMap == False:
        ph3.map()
        ut.state.flag_rerunMap = True
        ut.rerun()
    '''

    q = ph1.selectbox("What are you looking for?", ("Locations", "Animals", "Plants"))
    user_input = ""
    if q == "Locations":
        user_input = ph2.text_input("enter location")
    elif q == "Animals":
        user_input = ph2.text_input("enter animal")
    elif q == "Plants":
        user_input = ph2.text_input("enter plant")

    if user_input == "":
        df = pd.DataFrame(np.array([[51.52903, -0.155]]), columns=['lat', 'lon'])
        ph3.map(df, zoom = 14)
        ph3.map()
    elif user_input == "Regents Park":
        df = pd.DataFrame(
            np.random.randn(40, 2) / [250, 250] + [51.52903, -0.155], columns=['lat', 'lon'])
        ph3.map(df, zoom = 14)
    elif user_input == "Magpie":
        df = pd.DataFrame(
            np.random.randn(20, 2) / [300, 300] + [51.52903, -0.155], columns=['lat', 'lon'])
        ph3.map(df, zoom = 14)
    elif user_input == "test":
        df = pd.DataFrame(
            np.random.randn(20, 2) / [300, 300] + [51.52903, -0.155], columns=['lat', 'lon'])
        ph3.map(df, zoom = 14)