def load_word():
    word = "DOG"
    return word
def start_round(loaded_word):
    hidden_word = "_ " * len(loaded_word)
    print("Round started")
    print("\n")
    print(hidden_word)

loaded_word = load_word()
start_round(loaded_word)