import random

def play_hangman():
    words = ["python", "programming", "developer", "portfolio", "software"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    print("Jogo da Forca!")
    while attempts > 0 and "_" in guessed:
        print("\nPalavra:", " ".join(guessed))
        print(f"Tentativas restantes: {attempts}")
        guess = input("Digite uma letra: ").lower()

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1

        if "_" not in guessed:
            print("\nParabéns! Você acertou a palavra:", word)
            return

    print("\nVocê perdeu! A palavra era:", word)

if __name__ == "__main__":
    play_hangman()
