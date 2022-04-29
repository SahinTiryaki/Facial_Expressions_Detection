import mediapipe as mp
import cv2 
from PIL import Image
import numpy as np
import tensorflow as tf
# face detection configurations
mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence = 0.4, model_selection = 1)

# face mesh for eyes and nose etc.
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.4, min_tracking_confidence=0.4, max_num_faces=2, static_image_mode=True)

# classify face as a angry, happy etc.
def get_predict_model(model_path):
    return tf.keras.models.load_model(model_path)

classify_model = get_predict_model(model_path="./models/classify_model.h5")


def classify_face(img):
    img = img/255
    pred = classify_model.predict_generator(img.reshape((1,150,150,3)))
    return pred.argmax(axis=1)[0]



# extract face on entire image
def extractFaces(img,requiredSize = (150, 150)):
        # convert the image from BGR to RGB space 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # get face detection result
        results_face = faceDetection.process(imgRGB)
        # find number of faces on image
        faces = results_face.detections # Number of faces
        
        # return it if faces variable is None
        if faces == None:
            return ["There is no face here!", 0]

        # return it if there is not a face
        elif len(faces) == 0:
            return ["There is no face here!", 0]
        
        elif len(faces)>1:
            return ["Multiple face!", int(len(faces))]
        # return it if there is a face
        elif len(faces) == 1:
            # loop on the detected faces
            for id, detection in enumerate(faces):
                # height and width of image
                h, w, _  = img.shape
                # get bounding box of face
                bbox = detection.location_data.relative_bounding_box
                # convert values in bbox float to integer
                bbox = int(bbox.xmin * w), int(bbox.ymin * h), \
                    int(bbox.width * w), int(bbox.height * h)
                
                # crop face using bbox
                face = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
                # convert face to Image object
                face = Image.fromarray(face)
                # resize face by 160x160 for FaceNet
                face = face.resize(requiredSize)
                # convert all values in face array to float
                face = np.asfarray(face)

                return face,bbox