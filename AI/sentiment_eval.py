import joblib

sentence = input("Enter Sentence: ")
tfidf_vec = joblib.load('tfidf_vector.sav')

logistic_reg = joblib.load('logistic_reg_model.sav')

vec = tfidf_vec.transform([sentence])
logistic_reg_pred = logistic_reg.predict(vec)

print(logistic_reg_pred)