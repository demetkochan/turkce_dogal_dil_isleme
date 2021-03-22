import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn import svm

import pickle

from sklearn.model_selection import cross_val_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def read_dataset(dataset):
    text = pd.read_csv(dataset,header = None,error_bad_lines=False,delimiter=';')
    text.columns = ["Yorum", "Duygu"]
    return (text)


def support_vector_tfidf(x_train, x_test, y_train, y_test):
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='scale')
    sup_vec = SVM.fit(x_train, y_train)
    sup_vec_cv_score = cross_val_score(sup_vec, x_test, y_test, cv=10)
    pickle.dump(sup_vec, open('sup_vec_model.sav', 'wb'))
    print(sup_vec)


    pickle.dump(sup_vec, open('sup_vec_tfidf_model.sav', 'wb'))
    print(sup_vec_cv_score)

    return (SVM)



def naive_bayes_tfidf(x_train, x_test, y_train, y_test):
    from sklearn import naive_bayes
    nb = naive_bayes.MultinomialNB()
    naive_bayes = nb.fit(x_train, y_train)
    naive_bayes_cv_score = cross_val_score(naive_bayes, x_test, y_test, cv=10)
    pickle.dump(naive_bayes, open('naive_bayes_model.sav', 'wb'))
    print(naive_bayes_cv_score)
    return (nb)



def knn_tfidf(x_train, x_test, y_train, y_test):
    knn = KNeighborsClassifier()
    knn_vec = knn.fit(x_train, y_train)
    knn_cv_score = cross_val_score(knn_vec, x_test, y_test, cv=10)
    pickle.dump(knn_vec, open('knn_vec_model.sav', 'wb'))
    print(knn_cv_score)


def logistic_regression_tfidf(x_train, x_test, y_train, y_test):
    log_reg = LogisticRegression()
    logistic_reg = log_reg.fit(x_train, y_train)
    log_reg_cv_score = cross_val_score(logistic_reg, x_test, y_test, cv=10)
    pickle.dump(logistic_reg, open('logistic_reg_model.sav', 'wb'))
    print(log_reg_cv_score)
    return (log_reg)


def decision_tree_tfidf(x_train, x_test, y_train, y_test):
    dec_tree = DecisionTreeClassifier()
    decision_tree = dec_tree.fit(x_train, y_train)
    dec_tree_cv_score = cross_val_score(decision_tree, x_test, y_test, cv=10)
    pickle.dump(decision_tree, open('decision_tree_model.sav', 'wb'))
    print(dec_tree_cv_score)
    return (dec_tree)


def random_forest_tfidf(x_train, x_test, y_train, y_test):
    rfc = RandomForestClassifier()
    random_forest = rfc.fit(x_train, y_train)
    rfc_cv_score = cross_val_score(random_forest, x_test, y_test, cv=10)
    pickle.dump(random_forest, open('random_forest_model.sav', 'wb'))
    print(rfc_cv_score)
    return (rfc)



def main():
    dataset = '../dataset/HUMIRSentimentDatasets.csv'
    text = read_dataset(dataset)
    tfidf_vect = TfidfVectorizer(analyzer="word")
    x_tfidf = tfidf_vect.fit_transform(text['Yorum'].apply(lambda x: np.str_(x)))
    y = text['Duygu'].values
    x_train, x_test, y_train, y_test = train_test_split(x_tfidf, y, test_size=0.2)


    pickle.dump(tfidf_vect, open('tfidf_vector.sav', 'wb'))
    #knn_tfidf(x_train, x_test, y_train, y_test)
    logistic_regression_tfidf(x_train, x_test, y_train, y_test)
    #random_forest_tfidf(x_train, x_test, y_train, y_test)
    #decision_tree_tfidf(x_train, x_test, y_train, y_test)
    #naive_bayes_tfidf(x_train, x_test, y_train, y_test)

    #pickle.dump(tfidf_vect, open('tfidf_vector.sav', 'wb'))
    #knn_tfidf(x_train, x_test, y_train, y_test)
    #logistic_regression_tfidf(x_train, x_test, y_train, y_test)
    #random_forest_tfidf(x_train, x_test, y_train, y_test)
    #decision_tree_tfidf(x_train, x_test, y_train, y_test)
    #naive_bayes_tfidf(x_train, x_test, y_train, y_test)

    #support_vector_tfidf(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    main()

