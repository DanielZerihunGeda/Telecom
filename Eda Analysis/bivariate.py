python
import seaborn as sns

def bivariate_analysis(df, col_A, col_B):
    # Seaborn Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=col_A, y=col_B)
    plt.xlabel(col_A)
    plt.ylabel(col_B)
    plt.title(f'Bivariate Analysis: {col_A} vs {col_B}')
    plt.show()
