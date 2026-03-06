def select_features(data):

    X = data.drop('Total reported direct emissions', axis=1)

    y = data['Total reported direct emissions']

    print("Features selected")

    return X, y