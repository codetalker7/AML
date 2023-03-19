import pickle
import textblob
import prepare_functions
from sklearn.feature_extraction.text import TfidfTransformer

# # example to load the model
# import mlflow
# LogisticRegression = mlflow.sklearn.load_model("../assignment2/mlruns/0/a211eafb22c94b63b49575f2a2f25a28/artifacts/model/")

def score(text:str, model, threshold:float) -> tuple:
    # load the vectorizer
    with open("../assignment2/bow_transformer.pickle", 'rb') as f:
        bow_transformer = pickle.load(f)

    sparse_bow = bow_transformer.transform([text])    
    tfidf_transformer = TfidfTransformer().fit(sparse_bow)
    result_matrix = tfidf_transformer.transform(sparse_bow)

    # return tuple of boolean prediction and spam probability
    spamprob = model.predict_proba(result_matrix)[0][1]
    return (bool(spamprob > threshold), spamprob)
