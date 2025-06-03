import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_summary(df: pd.DataFrame):
    print(df.describe())
    print("\nMissing values:\n", df.isnull().sum())

def plot_price_trends(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_correlation(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
