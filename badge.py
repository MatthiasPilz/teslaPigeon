import streamlit as st
import time

from PIL import Image

def run():
    ph1 = st.empty()
    badgeFake = Image.open('./data/thumbnail_AppDummy1.png')
    ph1.image(badgeFake, use_column_width=True)

    time.sleep(5)
    ph1.image(badgeFake, use_column_width=True)
