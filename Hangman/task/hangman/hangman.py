import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']

random_word = random.choice(word_list)
word = input("Guess the word " + random_word[0:3] + (len(random_word)-3)*"-" + ":")

if word == random_word:
    print("You survived!")
else:
    print("You are hanged!")