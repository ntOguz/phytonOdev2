import random
import string

def is_letter(char):
    return char.isalpha()

def count_palindromes(text):
    palindromes = [word for word in text.split() if word == word[::-1]] 
    return len(palindromes)  


def count_uppercase(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

def letter_frequency_analysis(text):
    text = text.lower()
    frequencies = {}
    total_letters = 0
    for char in text:
        if char.isalpha():
            total_letters += 1
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    
    letter_percentages = {char: (count / total_letters * 100) for char, count in frequencies.items()}
    return letter_percentages

def word_count(text):

    words = text.split()
    return len(words)

def sentence_count(text):
    sentences = text.split('.')
    print(sentences)
    return len(sentences)-1

def symbol_count(text):
    symbols = [char for char in text if not char.isalnum()and not char.isspace()]
    return len(symbols)


def get_most_common_letter(text):
    frequencies = letter_frequency_analysis(text)
    return max(frequencies, key=frequencies.get)

def print_info():
    print("İsim ve soyisim: Nazım Turan Oğuz")
    print("Öğrenci numarası: 211213080")
    print("\n"+"Yeni Dünya da çok eğleneceğiz"+"\n")

def generate_random_text(length=100):
    random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return random_text


input_text = "Be yourself in the virtual world. Get scanned and experience the true potential of the Metaverse"

