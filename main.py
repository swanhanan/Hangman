
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
LIVES = 6

print(logo)

# Create blanks
display = ["".join("_") for _ in range(word_length)]
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # if the letter is not in the chosen_word, print out the letter
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        LIVES -= 1
        if LIVES == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[LIVES])