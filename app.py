from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "model", "knn_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "model", "scaler.pkl"), "rb"))
features = pickle.load(open(os.path.join(BASE_DIR, "model", "selected_features.pkl"), "rb"))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    confidence = None
    error = None

    if request.method == "POST":
        try:
            values = [float(request.form[f]) for f in features]
            data = np.array(values).reshape(1, -1)

            data_scaled = scaler.transform(data)
           # prediction = model.predict(data_scaled)[0]
            #confidence = round(model.predict_proba(data_scaled).max() * 100, 2)
            raw_pred = model.predict(data_scaled)[0]
            confidence = round(model.predict_proba(data_scaled).max() * 100, 2)

# Label mapping
            if raw_pred == 1:
                prediction = "Cancerous"
            else:
                prediction = "Non-Cancerous"


            print("Prediction:", prediction, "Confidence:", confidence)

        except Exception as e:
            error = str(e)
            print("ERROR:", error)

    return render_template(
        "predict.html",
        features=features,
        prediction=prediction,
        confidence=confidence,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
