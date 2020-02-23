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
            np.random.randn(40, 2) / [250, 250] + [51.52903, -0.155])
        ph3.pydeck_chart(pdk.Deck(
        map_style = 'mapbox://styles/mapbox/light-v9',
        initial_view_state = pdk.ViewState(
        latitude = 37.76,
        longitude = -122.4,
        zoom = 11,
        pitch = 50, ),
        layers = [  pdk.Layer(     'HexagonLayer', data = df,
        get_position = '[lon, lat]',
        radius = 200,
        elevation_scale = 4,
        elevation_range = [0, 1000],
        pickable = True,
        extruded = True,  ),
        pdk.Layer(
        'ScatterplotLayer',
        data = df,
        get_position = '[lon, lat]',
        get_color = '[200, 30, 0, 160]',
        get_radius = 200,    ),], ))