python
import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df, column_name):

    # Seaborn
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column_name)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.title(f'Count of {column_name}')
    plt.show()


univariate_analysis(your_df, 'your_column')