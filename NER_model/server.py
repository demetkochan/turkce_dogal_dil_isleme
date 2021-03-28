from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
from collections import OrderedDict
from flask import Flask, request, jsonify

app = Flask(__name__)

model = AutoModelForTokenClassification.from_pretrained("savasy/bert-base-turkish-ner-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-ner-cased")
ner = pipeline('ner', model=model, tokenizer=tokenizer)


@app.route('/ner', methods=['GET', 'POST'])
def get_prediction():
    text = request.json.get('text')
    text = ner(text)

    word = []
    entity = []
    for t in text:
        word.append(list(t.values())[0])
        entity.append(list(t.values())[2])

    text_dictionary = OrderedDict(zip(word, entity))

    return jsonify(text_dictionary)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
