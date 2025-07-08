# 🖼️ MLOps Image Classifier API

This is an end-to-end image classification API using PyTorch and Flask, deployable to Kubernetes.

---

## 🔍 Features

- Pre-trained ResNet18 image classifier
- Upload any image and get top-1 predicted class
- Built with PyTorch + Flask
- Dockerized and Kubernetes-ready

---

## 🚀 Usage

### 1. Build Docker Image

```bash
docker build -t mlops-image-classifier:latest .


2. Run Locally

docker run -p 5000:5000 mlops-image-classifier

3. Test API

curl -X POST http://localhost:5000/predict \
  -F image=@dog.jpg

Output:

{"prediction": "Labrador retriever"}

☸️ Kubernetes Deployment

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward svc/classifier-service 8080:80

Then access:

curl -X POST http://localhost:8080/predict -F image=@cat.jpg

🧠 Requirements

    Python 3.9+

    Docker

    Kubernetes (kind or minikube)

    curl for testing

🔥 Author

Rohan Shahi
MLOps + Cloud/DevOps 🌐
