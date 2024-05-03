import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(data: pd.DataFrame):
    """
    Visualize the input data using various plots.

    Args:
        data (pd.DataFrame): The input data to be visualized.
    """
    # create various plots
    data.hist()
    plt.show()

    data.boxplot()
    plt.show()

    data.corr().plot(kind='heatmap')
    plt.show()
