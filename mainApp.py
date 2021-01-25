from flask import Flask, jsonify, request
from tensorflow import keras
import numpy as np

app = Flask(__name__)
model = keras.models.load_model("rating_model.h5")

@app.route("/sample")
def running():
    return "Flask is running!"

@app.route("/rate", methods=["POST"])
def rate():
    data = request.json
    data_sample = data["encoding"]

    x = np.asarray(data_sample).astype('float32').reshape((1, 128))
    x = x.tolist()

    prediction = model.predict(x)

    return jsonify({"rating": str(prediction[0,0])})
    

if __name__ == '__main__':
    app.run()
