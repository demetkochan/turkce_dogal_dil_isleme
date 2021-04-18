from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/sentiment", methods=['POST'])
def sentiment():
    url =  "http://localhost:5000/sentiment"
    payload = {"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2000)
