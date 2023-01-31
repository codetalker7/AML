from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

def train_model(model, data_matrix, labels):
    model.fit(data_matrix, labels)

def evaluate_model(model, data_matrix, labels):
    """
    Evaluate ``model`` on ``data``. Computes the accuracy, precision, 
    recall and confusion matrix. This function should be used to evaluate
    a model on the validation data set.

    :param model: The model to evaluate.
    :param data_matrix: The matrix on which the model is to be evaluated.
    :param labels: The labels for the data.
    """
    predictions = model.predict(data_matrix)
    print("model:" , str(model))
    print("accuracy: ", accuracy_score(labels, predictions))
    print("precision: ", precision_score(labels, predictions))
    print("recall: ", recall_score(labels, predictions))
    print("confusion matrix:\n", confusion_matrix(labels, predictions))
    print("-----x-----x-----\n")