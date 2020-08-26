import random

print("H A N G M A N")
word = input("Guess the word:")
word_list = ['python', 'java', 'kotlin', 'javascript']

random_word = random.choice(word_list)

if word == random_word:
    print("You survived!")
else:
    print("You are hanged!")