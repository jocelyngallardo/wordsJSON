import json

with open('words.json') as words:
    word_data = json.load(words)
    
#print(word_data[0]['word'])
for data in word_data:
    if data['part of speech'] == 'verb':
        print(data['word'])
        
num_noun = 0

for data in word_data:
    if data['part of speech'] == 'noun':
        num_noun+=1
print(num_noun)