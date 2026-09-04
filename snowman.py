import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")

    while mistakes < len(STAGES) - 1:

        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
            print(f"The word was: {secret_word}")
            break

    else:
        display_game_state(mistakes, secret_word, guessed_letters)
        print("The snowman melted!")
        print(f"The word was: {secret_word}")

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Word:", displayed_word)



if __name__ == "__main__":
    play_game()



