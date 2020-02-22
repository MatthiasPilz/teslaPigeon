import utility as ut
import streamlit as st

from PIL import Image

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

def run():
    imgFileBuffer = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
    if st.button("run demonstration"):
        if imgFileBuffer is not None:
            image = Image.open(imgFileBuffer)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            with st.spinner("classifying image..."):
                label = predict(imgFileBuffer)
                result = "**" + label[1] + "** (" + str(label[2] * 100)[:5] + "%)"
            st.balloons()
            st.markdown(result)

def predict(inputFile):
    model = VGG16()
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