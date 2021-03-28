from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import torch
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-squad")
model = AutoModelForQuestionAnswering.from_pretrained("savasy/bert-base-turkish-squad")
nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)


@app.route('/questionAns', methods=['GET', 'POST'])
def get_prediction():
    text = request.json.get('text')
    question = request.json.get('question')

    answer = nlp(question=question, context=text)
    return jsonify({"result": list(answer.values())[-1]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
