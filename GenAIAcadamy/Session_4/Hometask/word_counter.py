#write a funtion that takes a string and returns a dictionary where the keys are words from 
#the string and the values are thier occurances, ignore capitalization and punctuation


import re

def word_occurrences(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    occurrences = {}
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1
    return occurrences

print(word_occurrences("Hi how are you hi hi"))