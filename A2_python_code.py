import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

file_path = "/test/random_paragraphs.txt"
with open(file_path, "r") as file:
    text = file.read()

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

word_freq = Counter(filtered_words)

for word, freq in word_freq.items():
    print(f"{word}: {freq}")
