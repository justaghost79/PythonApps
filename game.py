def load_word():
    word = "DOG"
    return word
def start_round(loaded_word):
    hidden_word = "_ " * len(loaded_word)
    print("Round started")
    print("\n")
    print(hidden_word)

    guessed = False

    tries = 6

    while not guessed and tries > 0:
        guess = input("Guess a letter or the full word you little scamp!")


loaded_word = load_word()
start_round(loaded_word)