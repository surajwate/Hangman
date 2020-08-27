import random
import string

print("H A N G M A N")

while True:

    print('Type "play" to play the game, "exit" to quit:', end=" ")
    play = input()

    if play == "exit":
        break
    elif play == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(word_list)
        correct_guess = (len(random_word)) * "-"  # All the characters you have guessed correctly
        guessed_list = []  # All the words you have guess (correct or incorrect both)


        def get_input(correct_guess, guessed_list):
            while True:
                print()
                print(correct_guess)
                print("Input a letter:", end=" ")
                answer = input()
                if len(answer) != 1:
                    print("You should input a single letter")
                elif answer not in string.ascii_lowercase:
                    print("It is not an ASCII lowercase letter")
                elif answer in guessed_list:
                    print("You already typed this letter")
                else:
                    return answer


        count = 8
        while count > 0:
            letter = get_input(correct_guess, guessed_list)
            if letter in random_word:
                new_word = ""  # To make changes in correct_guess word in current loop
                if letter in correct_guess:  # or letter in guessed_list:
                    print("You already typed this letter")
                for i in range(len(random_word)):
                    if letter == random_word[i]:
                        new_word = new_word + letter  # Add letter for correct_guess word
                    elif correct_guess[i] != "-":
                        new_word = new_word + correct_guess[
                            i]  # Update new_word if character already present in correct_guess word
                    else:
                        new_word = new_word + "-"
                correct_guess = new_word  # Assign all changes from this loop in correct_guess word

                if "-" not in correct_guess:
                    print("You guessed the word!")
                    print("You survived!")
                    break

            elif letter not in random_word:
                print("No such letter in the word")
                count -= 1

            if letter not in guessed_list:
                guessed_list.append(letter)

        if "-" in correct_guess:
            print("You are hanged!\n")
            exit()

            

