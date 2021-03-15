import cv2
from flask import Flask, jsonify, request
from tensorflow import keras
import numpy as np
import face_recognition

app = Flask(__name__)
model = keras.models.load_model("rating_model.h5")
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

@app.route("/sample")
def running():
    return "Flask is running!"

@app.route("/getEncoding", methods=["POST"])
def Encode():
    data = request.json
    image = data["image"]

    encoding = face_recognition.face_encodings(image)[0] # Rates only the first face in the image

    return encoding

@app.route("/rate", methods=["POST"])
def rate():

    image = request.files['image'].read()
    #filename = secure_filename(image.filename)

    img = cv2.imdecode(np.frombuffer(image, dtype=np.uint8), -1)
    # data_sample = data["encoding"]

    # detect MultiScale / faces
    faces = classifier.detectMultiScale(img)

    # get the first face only
    face = faces[0]
    x = np.asarray(data_sample).astype("float32").reshape((1, 128))
    x = x.tolist()

    prediction = model.predict(x)

    return jsonify({"rating": str(prediction[0,0])})
    

if __name__ == "__main__":
    app.run()
