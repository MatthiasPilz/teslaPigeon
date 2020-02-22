import utility as ut
import streamlit as st
import pandas as pd
import numpy as np

def run():
    user_input = st.text_input("enter location")

    if user_input == "":
        st.map()
    elif user_input == "Regents Park":
        df = pd.DataFrame(
            np.random.randn(40, 2) / [250, 250] + [51.52803, -0.155], columns=['lat', 'lon'])

        st.map(df, zoom = 14)
    elif user_input == "test":
        #df = pd.DataFrame(
        #    np.random.randn(40, 2) / [250, 250] + [51.52803, -0.155], columns=['lat', 'lon'])
        st.deck_gl_chart(
            viewport = {
                'latitude': 51.52803,
                'longitude': -0.155,
                'zoom': 14,
                'pitch': 90,
            },
            layers = [
                {
                    'type': 'HexagonLayer',
                    'data': df,
                    'radius': 200,
                    'elevationScale': 4,
                    'elevationRange': [0, 1000],
                    'pickable': True,
                    'extruded': True,
                },
                {
                    'type': 'ScatterplotLayer',
                'data': df,
                }
            ]
        )