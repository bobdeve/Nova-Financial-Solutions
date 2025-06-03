import pandas as pd

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna()
    df = df.sort_values('Date').reset_index(drop=True)

    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    df = df.dropna()
    df = df[df['Volume'] > 0]

    return df

def save_cleaned_data(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False)
