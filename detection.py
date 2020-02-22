import utility as ut
import streamlit as st

import wikipediaapi

from PIL import Image

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.applications.nasnet import NASNetMobile
from keras.applications.nasnet import preprocess_input
from keras.applications.nasnet import decode_predictions

from keras.applications.mobilenet_v2 import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.applications.mobilenet_v2 import decode_predictions

def run():
    wiki_wiki = wikipediaapi.Wikipedia('en')

    imgFileBuffer = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
    if imgFileBuffer is not None:
        image = Image.open(imgFileBuffer)
    if st.button("run demonstration"):
        st.image(image, use_column_width=True)
        with st.spinner("classifying image..."):
            label = predict(imgFileBuffer)
            result = str(label[1])

        ## hardcoded event for spotting a jay
        if result == "jay":
            st.balloons()
            st.success("YOU FOUND A JAY!")

        ## retrieve wiki info
        page_py = wiki_wiki.page(result)
        content_title = "**" + page_py.title.capitalize() + "**"
        st.markdown(content_title)

        if len(page_py.summary) < 300:
            content_summary = page_py.summary
        else:
            content_summary = page_py.summary[0:300] + "..."
        st.markdown(content_summary)
        st.markdown("*Wikipedia/" + result + "*")

            #st.markdown("Jays are several species of medium-sized, usually colorful and noisy, passerine birds in the crow family, Corvidae. The names jay and magpie are somewhat interchangeable, and the evolutionary relationships are rather complex.")
            #st.markdown(result)

def predict(inputFile):
    #model = VGG16()
    #model = NASNetMobile()
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