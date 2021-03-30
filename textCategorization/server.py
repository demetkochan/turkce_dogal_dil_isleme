import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

load_vec = joblib.load("tfidf_vectorize.sav")
lr_model = joblib.load("logistic_reg_model.sav")


@app.route('/categorize', methods=['GET', 'POST'])
def get_prediction():
    text = request.json.get('text')
    vec = load_vec.transform([text])

    return jsonify({"result": lr_model.predict(vec)[0]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
