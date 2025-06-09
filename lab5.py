from collections import Counter
from operator import itemgetter
import re

def read_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b[а-яё]+\b', text)
    return words

def count_words(words):
    return Counter(words)

def find_matches(query, word_counts):
    result = []
    for word, count in word_counts.items():
        if query in word:
            result.append((word, count))
    result.sort(key=itemgetter(1), reverse=True)
    return result[:20]

words = read_words("war_and_peace.txt")
word_counts = count_words(words)

query = input("Введите запрос: ").lower()

if len(query) < 3:
    print("Запрос слишком короткий.")
else:
    matches = find_matches(query, word_counts)
    print("\nНайденные слова:")
    for word, count in matches:
        print(f"{word} — {count}")