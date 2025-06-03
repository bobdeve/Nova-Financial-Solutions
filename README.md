# Stock Market Data Analysis and Sentiment Exploration

## 📊 Project Overview

This project focuses on analyzing historical stock data and news headlines to gain insights into market behavior and sentiment. It includes data cleaning, exploratory data analysis (EDA), and sentiment analysis techniques applied to raw headline and stock data.

---

## ✅ Key Components

### 1. 📄 Headline Data (News)
- Cleaned raw news headlines by removing noise, stopwords, and irrelevant characters.
- Performed sentiment analysis to classify headlines into **positive**, **negative**, or **neutral** sentiments.
- Prepared the data for future integration with market indicators.

### 2. 📈 Historical Stock Data
- Datasets include historical price data for major companies like:
  - **Apple (AAPL)**
  - **Google (GOOGL)**
  - **Meta (META)**
  - **Amazon (AMZN)**
  - **Tesla (TSLA)**
- Cleaned missing values and standardized formats for consistency.
- Performed EDA to explore:
  - Price trends over time
  - Volume analysis
  - Moving averages
  - Correlation between stocks

---

## 🛠 Tools & Libraries
- **Python**
- **Pandas**
- **Matplotlib / Seaborn**
- **NLTK / TextBlob** (for sentiment analysis)
- **Jupyter Notebooks**

---

## 🚀 What's Next
- Combine sentiment scores with historical stock data
- Build a predictive model for stock movements based on news sentiment

📊 Task 3: Sentiment-Return Correlation Analysis
This task involves analyzing the relationship between daily news sentiment and stock market movements for seven major tech companies.

✅ Steps Completed:
Sentiment Labeling

Converted numerical sentiment scores into categorical labels: Positive, Negative, and Neutral.

Stored in a new column: Sentiment_Label.

Data Aggregation

Aggregated news sentiment per day per company, calculating:

Average sentiment score

Most common sentiment label (mode)

Stock Return Calculation

Computed daily stock returns using percentage change in the Close price.

Added a new column: Daily_Return.

Correlation Analysis

Merged aggregated daily sentiment with daily stock returns.

Calculated Pearson correlation coefficients to quantify the relationship between:

Daily average sentiment score and stock returns

Daily sentiment label and stock returns (label converted to numerical scale)

Applied to 7 Companies

Tesla (TSLA)

Apple (AAPL)

Microsoft (MSFT)

Google (GOOG)

NVIDIA (NVDA)

Amazon (AMZN)

Meta (META)

📁 Output Files
Each company now has an updated CSV with:

Aggregated daily sentiment

Calculated stock return

Sentiment-return correlation statistics
