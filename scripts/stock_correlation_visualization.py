import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def analyze_sentiment_return_correlation(file_path, company_name="Company", show_plot=True):
    # Load the labeled dataset
    df = pd.read_csv(file_path)

    # Convert date column to datetime and sort
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # Calculate daily stock returns (percentage change of 'Close' price)
    df['daily_return'] = df['Close'].pct_change() * 100  # percent

    # Drop rows with missing values
    df.dropna(subset=['daily_return', 'Sentiment'], inplace=True)

    # Correlation analysis between Sentiment score and daily stock return
    correlation, p_value = pearsonr(df['Sentiment'], df['daily_return'])

    print(f"📌 Pearson Correlation between Sentiment and Stock Return for {company_name}: {correlation:.4f}")
    print(f"📌 P-value: {p_value:.4f}")

    # Visualization
    if show_plot:
        plt.figure(figsize=(10, 6))
        sns.regplot(data=df, x='Sentiment', y='daily_return', scatter_kws={'alpha':0.6})
        plt.title(f'{company_name} - Sentiment Score vs Daily Stock Return')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Daily Stock Return (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
