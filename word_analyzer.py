import json

with open('words.json') as words:
    word_data = json.load(words)
    
print(word_data[0])