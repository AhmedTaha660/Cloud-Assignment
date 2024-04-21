import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Read the contents of the file
file_path = "/test/random_paragraphs.txt"
with open(file_path, "r") as file:
    text = file.read()

# Tokenize the text
words = word_tokenize(text)

# Remove stopwords
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
