from flask import Flask, request
import mlflow
import json
import score

app = Flask(__name__)

# load the model
LogisticRegression = mlflow.sklearn.load_model("mlruns/0/a211eafb22c94b63b49575f2a2f25a28/artifacts/model/")

@app.post('/score')
def getscore():
    (prediction, propensity) = score.score(request.form['text'], LogisticRegression, 0.5)
    return json.dumps({
        "prediction": prediction,
        "propensity": propensity
    })

