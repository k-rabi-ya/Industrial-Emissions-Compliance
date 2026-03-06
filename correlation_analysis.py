import seaborn as sns
import matplotlib.pyplot as plt

def spearman_correlation(data):

    corr = data.corr(method='spearman')

    print("Spearman Correlation Matrix")
    print(corr)

    plt.figure()
    sns.heatmap(corr, annot=True)
    plt.title("Spearman Correlation Heatmap")
    plt.show()