import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import string
from string import digits
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pickle
import numpy as np

def main():
    df = pd.read_csv("../Dataset/text_categorization.csv")
    df['remove_punc'] = df['text'].apply(lambda s: s.translate(str.maketrans('', '', string.punctuation)))
    df['remove_digit'] = df['remove_punc'].apply(lambda s: s.translate(str.maketrans('', '', digits)))

    tfidf_vec = TfidfVectorizer(analyzer="word")
    X_tfidf = tfidf_vec.fit_transform(df['remove_digit'].apply(lambda x: np.str_(x)))
    y = df['category']
    x_train, x_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2)
    pickle.dump(tfidf_vec, open('tfidf_vectorize.sav', 'wb'))
    logistic_regression(x_train, x_test, y_train, y_test)


def logistic_regression(x_train, x_test, y_train, y_test):
    log_reg = LogisticRegression()
    logistic_reg = log_reg.fit(x_train, y_train)
    log_reg_cv_score = cross_val_score(logistic_reg, x_test, y_test, cv=10)
    print(log_reg_cv_score.mean())
    pickle.dump(logistic_reg, open('logistic_reg_model.sav', 'wb'))
    print(log_reg_cv_score)
    return (log_reg)

if __name__ == "__main__":
    main()
