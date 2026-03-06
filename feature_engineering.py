def create_labels(data):

    threshold = data['Total reported direct emissions'].median()

    data['compliance'] = (
        data['Total reported direct emissions'] > threshold
    ).astype(int)

    return data