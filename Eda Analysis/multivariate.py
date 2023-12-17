python
import seaborn as sns
import matplotlib.pyplot as plt

def multivariate_correlation(df, columns_list):
    # Select columns of from the DataFrame
    selected_columns = df[columns_list]

    # Calculate correlation matrix
    correlation_matrix = selected_columns.corr()

    # Plotting the correlation matrix as a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Multivariate Correlation Matrix')
    plt.show()
