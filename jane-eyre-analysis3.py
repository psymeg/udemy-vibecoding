import plotly.express as px
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from wordcloud import WordCloud
from textblob import TextBlob
import re

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load the text
with open("jane-eyre-autobiography.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Preprocess text
text = text.lower()
text = re.sub(r'[^a-zA-Z\s]', '', text)
nltk.download('punkt')
nltk.download('stopwords')
words = word_tokenize(text)
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Word Frequency Analysis
word_counts = Counter(filtered_words)
most_common_words = word_counts.most_common(20)

# Plot word frequency with Plotly
fig = px.bar(x=[word[0] for word in most_common_words], y=[word[1] for word in most_common_words], 
             labels={'x': 'Word', 'y': 'Frequency'}, title="Top 20 Most Common Words in Jane Eyre")
fig.show()

# Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
wordcloud.to_file("wordcloud.png")

# Sentiment Analysis
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f"Overall Sentiment Score: {sentiment}")

# Character Mentions
characters = ["jane", "rochester", "adele", "st john", "bertha"]
char_counts = {char: text.count(char) for char in characters}
fig = px.bar(x=list(char_counts.keys()), y=list(char_counts.values()),
             labels={'x': 'Character', 'y': 'Mentions'}, title="Character Mentions in Jane Eyre")
fig.show()

# Sentence Length Distribution
sentences = sent_tokenize(text)
sentence_lengths = [len(sent.split()) for sent in sentences]
fig = px.histogram(x=sentence_lengths, nbins=30, 
                   labels={'x': 'Words per Sentence', 'y': 'Frequency'}, 
                   title="Sentence Length Distribution in Jane Eyre")
fig.show()

