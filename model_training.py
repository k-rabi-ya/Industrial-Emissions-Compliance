from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

scaler = StandardScaler()
model = RandomForestClassifier(random_state=42)

def train_model(X_train, y_train):

    
    X_train_scaled = scaler.fit_transform(X_train)

    
    model.fit(X_train_scaled, y_train)

    print("Model training completed")
    print(model)

    return model, scaler
