import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from wordcloud import WordCloud
from textblob import TextBlob
import re

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

# Plot word frequency
plt.figure(figsize=(10,5))
plt.bar([word[0] for word in most_common_words], [word[1] for word in most_common_words])
plt.xticks(rotation=45)
plt.title("Top 20 Most Common Words in Jane Eyre")
plt.show()

# Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Sentiment Analysis
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f"Overall Sentiment Score: {sentiment}")

# Character Mentions
characters = ["jane", "rochester", "adele", "st john", "bertha"]
char_counts = {char: text.count(char) for char in characters}
plt.figure(figsize=(8,4))
plt.bar(list(char_counts.keys()), list(char_counts.values()))
plt.title("Character Mentions in Jane Eyre")
plt.show()

# Sentence Length Distribution
sentences = sent_tokenize(text)
sentence_lengths = [len(sent.split()) for sent in sentences]
plt.figure(figsize=(10,5))
plt.hist(sentence_lengths, bins=30, edgecolor='black')
plt.title("Sentence Length Distribution in Jane Eyre")
plt.xlabel("Words per Sentence")
plt.ylabel("Frequency")
plt.show()
