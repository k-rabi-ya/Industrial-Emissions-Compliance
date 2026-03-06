import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def feature_importance(model, X):

    importance = model.feature_importances_

    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': importance
    })

    print(feature_importance)

    plt.figure()
    sns.barplot(
        x='Importance',
        y='Feature',
        data=feature_importance
    )

    plt.title("Feature Importance")
    plt.show()