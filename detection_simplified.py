# USAGE
# python deep_learning_with_opencv.py --image images/jemma.png --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt

# import the necessary packages
import numpy as np
import cv2
import os
import streamlit as st

def file_selector(folder_path='./data/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

def run():
	filename = file_selector()
	if st.button("run demonstration"):
		# load the input image from disk
		image = cv2.imread(filename)[...,::-1]
		st.image(image, caption='Uploaded Image.', use_column_width=True)
		with st.spinner("classifying image..."):
			label = predict(image)
		st.markdown(label)

def predict(image):
	with open('class_list.txt', 'r') as file:
		classes = file.read().split(",")
		print(classes)

	blob = cv2.dnn.blobFromImage(image, 1, (224, 224))
	net = cv2.dnn.readNetFromCaffe("bvlc_googlenet.prototxt", "bvlc_googlenet.caffemodel")

	net.setInput(blob)
	preds = net.forward()

	idxs = np.argsort(preds[0])[::-1][:5]

	return classes[idxs[0]]