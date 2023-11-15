print('Input 3 words.')

words = []

for i in range(3):
    word = input('Enter a word: ')
    words.append(word)

print('Common letters for given words are:', set(words[0]) & set(words[1]) & set(words[2]))