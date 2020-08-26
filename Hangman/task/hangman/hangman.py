import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']

random_word = random.choice(word_list)

your_guess = (len(random_word)) * "-"  # All the characters you have guessed

count = 8

while count > 0:
    print()
    print(your_guess)
    print("Input a letter:", end=" ")
    letter = input()
    if letter in random_word:
        new_word = ""  # To make changes in your_guess word in current loop
        if letter in your_guess:
            print("No improvements")
            count -= 1
        for i in range(len(random_word)):
            if letter == random_word[i]:
                new_word = new_word + letter  # Add letter for your_guess word
            elif your_guess[i] != "-":
                new_word = new_word + your_guess[i]  # Update new_word if character already present in your_guess word
            else:
                new_word = new_word + "-"
        your_guess = new_word  # Assign all changes from this loop in your_guess word

        if "-" not in your_guess:
            print("You guessed the word!")
            print("You survived!")
            break

    elif letter not in random_word:
        print("No such letter in the word")
        count -= 1

if "-" in your_guess:
    print("You are hanged!")
    exit()
