import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def process_and_plot_sentiment(input_path, output_path, show_plot=True, company_name="Company"):
    # 📥 Load the merged CSV
    merged_df = pd.read_csv(input_path)
    
    # 🧠 Define sentiment categorization logic
    def categorize_sentiment(score):
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'

    # 🏷️ Apply sentiment labels
    merged_df['Sentiment_Label'] = merged_df['Sentiment'].apply(categorize_sentiment)

    # 💾 Save the labeled dataset
    merged_df.to_csv(output_path, index=False)

    # 📊 Plot (optional)
    if show_plot:
        sns.countplot(data=merged_df, x='Sentiment_Label', palette='pastel')
        plt.title(f"{company_name} News Sentiment Categories")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.show()
