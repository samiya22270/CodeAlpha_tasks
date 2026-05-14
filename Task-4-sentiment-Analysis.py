# Task 4 - Sentiment Analysis

# Import Libraries
from textblob import TextBlob
import pandas as pd

# Sample Reviews Dataset
reviews = [
    "This product is amazing and very useful!",
    "I am extremely happy with the service.",
    "The quality is bad and disappointing.",
    "It is an average product.",
    "Excellent experience, highly recommended!",
    "Worst purchase ever."
]

# Create DataFrame
data = pd.DataFrame({
    "Reviews": reviews
})

# Function for Sentiment Analysis
def get_sentiment(text):
    
    analysis = TextBlob(text)
    
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    
    elif polarity < 0:
        return "Negative"
    
    else:
        return "Neutral"

# Apply Sentiment Analysis
data["Sentiment"] = data["Reviews"].apply(get_sentiment)

# Display Results
print(data)

# Save Results to CSV
data.to_csv("sentiment_results.csv", index=False)

print("\nSentiment Analysis Completed Successfully!")
