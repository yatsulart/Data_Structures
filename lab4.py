from collections import Counter

def read_words(file_name):
    words = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word:
                words.append(word)
    return words

def is_valid(word, letters_count):
    word_count = Counter(word)
    for letter in word_count:
        if word_count[letter] > letters_count.get(letter, 0):
            return False
    return True

def find_words(given_word, word_list):
    result = []
    given_count = Counter(given_word)
    for w in word_list:
        if is_valid(w, given_count):
            result.append(w)
    result.sort(key=len, reverse=True)
    return result

print("Яцула Артем Романович, 090301-ПОВа-о24")
user_input = input("Введите слово: ")

words = read_words("nouns.txt")

matches = find_words(user_input, words)

print("\nСлова, которые можно составить:")
for w in matches:
    print(w)
