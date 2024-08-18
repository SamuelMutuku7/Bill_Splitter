# put your python code here
word_dictionary = {}
sentence = input()
words = sentence.split()

for word in words:
    word = word.lower()  # Convert each word to lowercase
    word_dictionary[word] = word_dictionary.get(word, 0) + 1

for word, amount in word_dictionary.items():
    print(f'{word} {amount}')


