from flask import Flask, request, jsonify
from PIL import Image
import torchvision.transforms as transforms
import torch
import torchvision.models as models
import io
import json
import os

app = Flask(__name__)

# Load pre-trained model
model = models.resnet18(pretrained=True)
model.eval()

# Load ImageNet classes
with open(os.path.join(os.path.dirname(__file__), "imagenet_classes.json")) as f:
    classes = json.load(f)

# Preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

@app.route("/", methods=["GET"])
def home():
    return "Image Classification API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image = Image.open(file.stream).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
        class_name = classes[str(predicted.item())]

    return jsonify({"prediction": class_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

