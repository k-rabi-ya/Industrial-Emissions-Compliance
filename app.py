from data_loading import load_data
from data_cleaning import clean_data
from feature_selection import select_features
from correlation_analysis import spearman_correlation
from random_forest_model import train_random_forest
from visualization import feature_importance

def main():

    data = load_data()

    data = clean_data(data)

    spearman_correlation(data)

    X, y = select_features(data)

    model = train_random_forest(X, y)

    feature_importance(model, X)

if __name__ == "__main__":
    main()