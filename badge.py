import streamlit as st
import time
import utility as ut

from PIL import Image

def run():
    ph1 = st.empty()

    if not ut.state.flag_rareComplete:
        badgeEmpty = Image.open('./data/badgePending.png')
        ph1.image(badgeEmpty, use_column_width=True)

        time.sleep(3)
        badgeRareDetail = Image.open('./data/rare.png')
        ph1.image(badgeRareDetail, use_column_width=True)
    else:
        badgeComplete = Image.open('./data/badgeComplete.png')
        ph1.image(badgeComplete, use_column_width=True)

        time.sleep(2)
        badgeBeatrix = Image.open('./data/beatrix.png')
        ph1.image(badgeBeatrix, use_column_width=True)

