"""
train_model.py

This file contains the core training logic for the phishing URL detection model.

Responsibilities:
- Initialize a Random Forest Classifier using given hyperparameters
- Train the model on the provided training data
- Save the trained model as a .pkl file for reuse
- Return the trained model object

Design:
The actual training implementation is kept here so it can be reused across
notebooks and deployment (e.g., Flask app). The notebook controls data loading,
hyperparameter selection, and evaluation, while this file handles how the model
is trained and saved.
"""

from sklearn.ensemble import RandomForestClassifier
import joblib as jl

def model_train(hyperparameters,x_train,y_train):
    rf = RandomForestClassifier(**hyperparameters)
    model = rf.fit(x_train,y_train)
    jl.dump(model,"../models/random_forest.pkl")

    return model
    


