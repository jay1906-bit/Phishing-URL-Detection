from flask import Flask, render_template, request
import joblib
import numpy as np
import sys
import os

# allow imports from src
sys.path.append(os.path.abspath("."))

from src.feature_extraction import FeatureExtractor

app = Flask(__name__)

# load trained model once
model = joblib.load("models/random_forest.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]

    extractor = FeatureExtractor(url)
    features = extractor.feature_vector().reshape(1, -1)

    prediction = model.predict(features)[0]

    if prediction == 0:
        result = "Phishing URL ❌"
    else:
        result = "Legitimate URL ✅"

    return render_template("index.html", prediction=result, input_url=url)


if __name__ == "__main__":
    app.run(debug=True)
