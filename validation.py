from sklearn.metrics import confusion_matrix, accuracy_score

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)

    tn, fp, fn, tp = cm.ravel()

    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    accuracy = accuracy_score(y_test, y_pred)

    print("Sensitivity:", sensitivity)
    print("Specificity:", specificity)
    print("Accuracy:", accuracy)
    print("Confusion Matrix:")
    print(cm)