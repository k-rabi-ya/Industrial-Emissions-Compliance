from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

scaler = StandardScaler()

def train_model(X_train, y_train):
    X_train_scaled = scaler.fit_transform(X_train)

    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }


    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, scoring='accuracy')

    print("Starting Grid Search... please wait.")
    grid_search.fit(X_train_scaled, y_train)

    print("\n" + "="*30)
    print("BEST PARAMETERS FOUND:")
    print(grid_search.best_params_)
    print("="*30 + "\n")

    return grid_search.best_estimator_, scaler