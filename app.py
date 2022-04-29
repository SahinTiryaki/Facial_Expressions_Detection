# import libraries
import streamlit as st
import numpy as np
import cv2 
from PIL import Image
from face import extractFaces, classify_face

st.title(':cry: Facial Expressions Detection :smile:')
image = Image.open("./media/facial_expressions.jpg")
st.image(image, caption='Facial Expressions', width=500)

# facial expressions
facial_expressions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']


webcam_title = st.title("Webcam Live Feed")
run = st.button("Run camera")
stop = st.button("stop camera")

i=0

FRAME_WINDOW = st.image([])
last_status = ""
if run:
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if ret:
            # face alignment
            # face detection
            face, bbox = extractFaces(frame)

            # no face or multiple faces
            if type(face)==str:
                frame = cv2.putText(frame, face, (70,100), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                frame = cv2.rectangle(frame, (bbox[0],bbox[1]), (bbox[2]+bbox[0],bbox[1]+bbox[3]), (0,255,0), 2)

                if i %30 == 0:
                    result = classify_face(face)       
   
                    frame = cv2.putText(frame, facial_expressions[result], (70,100), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)
                    last_status = result
                else:
                    frame = cv2.putText(frame, facial_expressions[last_status], (70,100), cv2.FONT_HERSHEY_SIMPLEX, 

                    1, (0, 255, 0), 2, cv2.LINE_AA)
            FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if stop:
            run = False
            camera.release()