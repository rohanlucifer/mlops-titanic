# 🚢 MLOps Titanic Survival Prediction API

This project is an end-to-end MLOps implementation of a machine learning model that predicts survival on the Titanic. It includes model training, packaging, and deployment to a local Kubernetes cluster (`kind`) with an exposed REST API using Flask.

---

## 📦 Features

- Machine Learning with `scikit-learn`
- REST API built using `Flask`
- Dockerized for containerized deployments
- Kubernetes-ready with manifests
- Predict endpoint: `/predict`
- Health-check endpoint: `/`
- Local deployment using `kind` cluster
- Port-forwarding to test via `curl`

---

## 🧠 Model Info

- **Dataset**: Titanic (sampled version)
- **Features Used**:
  - `Pclass` (Passenger class)
  - `Sex` (encoded to 0 = male, 1 = female)
  - `Age`
  - `SibSp` (Siblings/Spouses aboard)
  - `Parch` (Parents/Children aboard)
  - `Fare`
- **Model**: `RandomForestClassifier` from `sklearn`

---

## 🗂️ Project Structure


