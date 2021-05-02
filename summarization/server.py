import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/summarization', methods=['GET', 'POST'])
def get_prediction():
    text = request.json.get('text')
    nltk.download('punkt')
    stopWords = set(stopwords.words("turkish"))
    words = word_tokenize(text)
    frequency = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in frequency.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")