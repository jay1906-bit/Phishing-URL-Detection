# Phishing URL Detection using Machine Learning

This project implements a machine learning system to detect whether a URL is **phishing or legitimate** based on URL-based features.

The main focus of the project is **feature engineering, model training, evaluation**, and a **simple Flask interface** to demonstrate the model.

---

## Project Highlights

- Manual feature extraction from URLs
- Random Forest classification model
- High phishing detection recall
- Flask web interface for live prediction
- Clean and modular project structure

---

## Feature Engineering

The following URL-based features are extracted:

- URL length  
- IP address presence  
- Hyphen count  
- Dot count  
- `@` symbol presence  
- HTTPS usage  
- Subdomain count  
- Suspicious keyword count  
- Encoded character count  
- Query length  

These features capture common phishing URL patterns.

---

## Model

- **Algorithm:** Random Forest Classifier  
- **Train-Test Split:** 80–20  
- **Class Imbalance Handling:** Balanced class weights  

### Performance (Test Set)

- **Accuracy:** 94%  
- **Phishing Recall:** 97%  

The model prioritizes catching phishing URLs while keeping false positives low.

---

## Flask Web Interface

A simple Flask app allows users to:
- Enter a URL
- Instantly see whether it is **Phishing** or **Legitimate**

This is intended for **demonstration purposes**.

---

## How to Run

```bash
pip install flask numpy scikit-learn joblib
python app.py
http://127.0.0.1:5000
```
---
## Dataset

PhiUSIIL Phishing URL Dataset UCI
- https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- Source : UCI Machine Learning Repository

---
## Author

Jayasri s
B.Tech Artificial Intelligence & Data Science
