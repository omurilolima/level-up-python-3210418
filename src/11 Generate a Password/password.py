import secrets

def password(num_words, wordlist_path='diceware.wordlist.asc'):
    # generate a list with all words
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    # select X random words from de list based on num_words
    words = [secrets.choice(word_list) for i in range(num_words)]

    # return the sequence of words split by space
    return ' '.join(words)

print(password(7))
