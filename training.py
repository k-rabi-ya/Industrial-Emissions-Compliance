from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def train_model(data):

    X = data.drop(
        ['Facility Id','City','State','Industry Type (sectors)','compliance'],
        axis=1
    )

    y = data['compliance']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    return model, X_test, y_test