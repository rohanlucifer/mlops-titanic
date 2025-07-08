from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET"])
def home():
    return "ML Ops Titanic API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json.get("data")
    if not input_data or len(input_data) != 6:
        return jsonify({"error": "Input 'data' must be a list of 6 features: [Pclass, Sex, Age, SibSp, Parch, Fare]"}), 400

    # If 'Sex' is passed as string (e.g., "male"/"female"), convert to numeric
    sex = input_data[1]
    if isinstance(sex, str):
        sex_map = {"male": 0, "female": 1}
        sex_num = sex_map.get(sex.lower())
        if sex_num is None:
            return jsonify({"error": "Sex must be 'male' or 'female'"}), 400
        input_data[1] = sex_num

    try:
        features = np.array(input_data, dtype=float).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run flask app on all interfaces at port 5000
    app.run(host="0.0.0.0", port=5000)

