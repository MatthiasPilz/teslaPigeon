import utility as ut
import streamlit as st
import cv2
import time
import wikipediaapi
from PIL import Image
import os

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.applications.mobilenet_v2 import decode_predictions

'''
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.applications.nasnet import NASNetMobile
from keras.applications.nasnet import NASNetLarge
from keras.applications.nasnet import preprocess_input
from keras.applications.nasnet import decode_predictions
'''

def run():
    ph1 = st.empty()
    ph2 = st.empty()
    ph3 = st.empty()
    ph4 = st.empty()
    ph5 = st.empty()
    ph6 = st.empty()
    ph7 = st.empty()

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    imgFileBuffer = ph1.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
    if imgFileBuffer is not None:
        image = Image.open(imgFileBuffer)
    if ph2.button("identify!"):
        ph3.image(image, use_column_width=True)

        #with st.spinner("classifying image..."):
        label = predict(imgFileBuffer)
        result = str(label[1])

    ## give special message if identification gives non-living object
        if label[0][:8] > "n02655020":
            st.warning("Careful, you might be off-track buddy :)")
            st.warning("We give you the wiki page anyway :P")
        else:
            ## hardcoded event for spotting a jay
            if result == "jay":
                st.balloons()
                ph4.success("YOU FOUND A JAY!")

            if result == "magpie":
                if not ut.state.flag_rareComplete:
                    st.balloons()
                    ph4.success("YOU FOUND A MAGPIE!")
                    image_badge = cv2.imread("./data/NotARobin_NewBadge.png")[...,::-1]
                    ph3.image(image_badge, use_column_width=True)
                    time.sleep(5)
                    ph3.image(image, use_column_width=True)
                    ut.state.flag_rareComplete = True
                else:
                    st.warning("You already collected a magpie.")
                    ph3.image(image, use_column_width=True)


        ## retrieve wiki info
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(result)
        content_title = "**" + page_py.title.capitalize() + "**"
        ph5.markdown(content_title)

        if len(page_py.summary) < 300:
            content_summary = page_py.summary
        else:
            content_summary = page_py.summary[0:300] + "..."
        ph6.markdown(content_summary)
        ph7.markdown("*Wikipedia/" + result + "*")


def predict(inputFile):
    model = MobileNetV2()
    image = load_img(inputFile, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    return label
