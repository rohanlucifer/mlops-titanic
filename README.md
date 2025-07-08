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

mlops-titanic/
├── data/
│ └── titanic.csv # Sample dataset
├── src/
│ ├── train.py # Trains and saves model.pkl
│ └── predict.py # Flask API app
├── Dockerfile # Container definition
├── deployment.yaml # Kubernetes Deployment
├── service.yaml # Kubernetes Service
└── README.md # This file


---

## 🚀 Quickstart

### 1. 🧪 Train the Model
```bash
python3 src/train.py

Generates model.pkl.

2. 🐳 Build the Docker Image

docker build -t mlops-titanic:latest .


3. 🔁 Deploy to kind Cluster

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml



4. 🌐 Port Forward the Service

kubectl port-forward svc/ml-service 8080:80

Now the API is accessible at http://localhost:8080.


5. 📤 Make a Prediction

curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [3, "female", 22, 1, 0, 7.25]}'

✅ Expected response:

{"prediction": 1}

🔍 API Endpoints
Method	Endpoint	Description
GET	/	Health check
POST	/predict	Submit features, get prediction
