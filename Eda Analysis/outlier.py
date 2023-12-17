import seaborn as sns
import matplotlib.pyplot as plt

#takes the DataFrame and Column name as a parameters
def plot_outliers(df, col_name):
    sns.boxplot(x=df[col_name])
    plt.show
    