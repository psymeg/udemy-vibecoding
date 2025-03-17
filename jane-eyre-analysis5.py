import plotly.express as px
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from wordcloud import WordCloud
from textblob import TextBlob
import re
from fpdf import FPDF

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

# Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
wordcloud.to_file("wordcloud.png")

# Sentiment Analysis
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

# Character Mentions
characters = ["jane", "rochester", "adele", "st john", "bertha"]
char_counts = {char: text.count(char) for char in characters}

# Sentence Length Distribution
sentences = sent_tokenize(text)
sentence_lengths = [len(sent.split()) for sent in sentences]

# Form Analysis (Caroline Levine's approach)
def analyze_form(text):
    patterns = {
        "repetition": len(re.findall(r'\b(\w+)\b(?=.*\b\1\b)', text)),
        "parallelism": len(re.findall(r'\b(\w+\s\w+)\b(?=.*\b\1\b)', text)),
        "rhythm": sum(sentence_lengths) / len(sentence_lengths)
    }
    return patterns

form_analysis = analyze_form(text)

# Generate PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Jane Eyre Text Analysis", ln=True, align='C')
pdf.ln(10)

pdf.cell(200, 10, f"Overall Sentiment Score: {sentiment:.2f}", ln=True)
pdf.ln(5)

pdf.cell(200, 10, "Character Mentions:", ln=True)
for char, count in char_counts.items():
    pdf.cell(200, 10, f"{char}: {count}", ln=True)
pdf.ln(5)

pdf.cell(200, 10, "Top 20 Most Common Words:", ln=True)
for word, count in most_common_words:
    pdf.cell(200, 10, f"{word}: {count}", ln=True)
pdf.ln(5)

pdf.cell(200, 10, "Form Analysis (Caroline Levine's Approach):", ln=True)
pdf.ln(5)
pdf.multi_cell(0, 10, "Caroline Levine's approach to form analysis considers how literary structures shape meaning. This analysis includes:")
pdf.ln(5)
pdf.multi_cell(0, 10, "- Repetition: The number of times individual words are repeated throughout the text, which can indicate themes and emphasis.")
pdf.multi_cell(0, 10, "- Parallelism: The recurrence of multi-word phrases that create structural rhythm and highlight key ideas.")
pdf.multi_cell(0, 10, "- Rhythm: The average sentence length, providing insight into the pacing and flow of the narrative.")
pdf.ln(5)

for pattern, value in form_analysis.items():
    pdf.cell(200, 10, f"{pattern}: {value}", ln=True)
pdf.ln(5)

pdf.output("jane_eyre_analysis.pdf")

print("Analysis complete. Results saved to 'jane_eyre_analysis.pdf'")
1
