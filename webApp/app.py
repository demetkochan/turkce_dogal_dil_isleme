from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/",methods=["GET"])
def home():
    return render_template("SignPage.html")

@app.route("/sentiment", methods=['POST'])
def sentiment():
    url =  "http://localhost:5000/sentiment"
    payload = {"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

@app.route("/kelimecikarma", methods=['POST'])
def keywordExtraction():
    url =  "http://localhost:5000/keyword"
    payload = {"text": request.form["input_text"],"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

@app.route("/konutanimlama", methods=['POST'])
def categorization():
    url =  "http://localhost:5000/categorization"
    payload = {"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

@app.route("/sorucevap", methods=['POST'])
def questionAnswer():
    url =  "http://localhost:5000/questionAns"
    payload = {"text": request.form["input_text"],"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

@app.route("/ozetleme", methods=['POST'])
def summarization():
    url =  "http://localhost:5000/summarization"
    payload = {"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

@app.route("/varliktanima", methods=['POST'])
def ner():
    url =  "http://localhost:5000/ner"
    payload = {"text": request.form["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2000)
