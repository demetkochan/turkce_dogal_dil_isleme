import nltk
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from nltk import tokenize
from operator import itemgetter
import math
from flask import Flask, request, jsonify

app = Flask(__name__)
nltk.download('punkt')


@app.route('/keyword', methods=['GET', 'POST'])
def get_prediction():
    text = request.json.get('text')
    key_number1 = request.json.get('key_number')
    key_number2 = int(key_number1)
    stop_words = get_stop_words('turkish')

    total_words = text.split()
    total_word_length = len(total_words)

    total_sentences = tokenize.sent_tokenize(text)
    total_sent_len = len(total_sentences)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())


    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())

    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

    return jsonify(get_top_n(tf_idf_score, key_number2))

def check_sent(word, sentences):
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key=itemgetter(1), reverse=True)[:n])
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")