from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import numpy as np
from model_preparation import prepare_data
from model_training import train_model

# Prepare data
X, y = prepare_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model, scaler = train_model(X_train, y_train)

# Predict
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)

# Get confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Method 1: Using sklearn
from sklearn.metrics import recall_score, precision_score

sensitivity = recall_score(y_test, y_pred, average='macro')  # Sensitivity for each class
specificity_score = recall_score(y_test, y_pred, average='macro', pos_label=None)

print(f"\nSensitivity (Macro): {sensitivity:.4f}")

# Method 2: Manual calculation for each class
print("\n" + "="*50)
print("SENSITIVITY & SPECIFICITY FOR EACH CLASS")
print("="*50)

classes = ['Unknown', 'Poor', 'Very Poor', 'Severe', 'Moderate', 'Satisfactory', 'Good']

for i, class_name in enumerate(classes):
    TP = cm[i, i]
    FN = cm[i].sum() - TP
    FP = cm[:, i].sum() - TP
    TN = cm.sum() - TP - FN - FP
    
    sensitivity = TP / (TP + FN) if (TP + FN) > 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
    
    print(f"\n{class_name}:")
    print(f"  Sensitivity (Recall): {sensitivity:.4f}")
    print(f"  Specificity: {specificity:.4f}")
    print(f"  TP: {TP}, FN: {FN}, FP: {FP}, TN: {TN}")