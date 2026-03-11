from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from feature_selection import X_test, y_test
from model_training import model, scaler

# Scale test data
X_test_scaled = scaler.fit_transform(X_test)

# Predict
y_pred = model.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))