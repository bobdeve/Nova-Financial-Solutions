import pandas as pd

def merge_news_and_stock(news_path, stock_path, output_path):
    """
    Merge news sentiment data with historical stock data based on matching dates.

    Args:
        news_path (str): Path to the cleaned news CSV file.
        stock_path (str): Path to the cleaned stock CSV file.
        output_path (str): Path where the merged CSV will be saved.

    Returns:
        pd.DataFrame: Merged DataFrame combining news and stock data.
    """
    
    news_df = pd.read_csv(news_path)
    stock_df = pd.read_csv(stock_path)

    # Parse news dates, handling mixed timezone-aware and naive timestamps
    news_df['date'] = pd.to_datetime(news_df['date'], utc=True, errors='coerce')
    mask = news_df['date'].isna()
    if mask.any():
        news_df.loc[mask, 'date'] = pd.to_datetime(news_df.loc[mask, 'date'], errors='coerce')

    # Keep only the date part (drop time and timezone)
    news_df['date'] = news_df['date'].dt.date

    # Parse stock dates (assumed naive dates, no timezone)
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

    # Drop rows with missing dates
    news_df.dropna(subset=['date'], inplace=True)
    stock_df.dropna(subset=['Date'], inplace=True)

    # Merge on dates
    merged_df = pd.merge(news_df, stock_df, how='left', left_on='date', right_on='Date')

    # Save merged data
    merged_df.to_csv(output_path, index=False)

    return merged_df
