from flask import Flask, render_template, request, jsonify
from utils import make_prediction

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    email_text = request.form.get('content')
    prediction =  make_prediction(email_text)
    return render_template("index.html", prediction=prediction, email_text=email_text)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email_text = data['content']
    prediction =  make_prediction(email_text)
    return jsonify({'prediction': prediction, 'email_text': email_text}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)