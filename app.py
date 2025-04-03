import flask
from flask import Flask
from flask import render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000,debug=True)