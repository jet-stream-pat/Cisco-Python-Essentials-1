secret_word = "chupacabra"

user_word = input("Guess the secret word. ")

while user_word != secret_word:
    print("Guess again. ")
    user_word = input("Guess the secret word. ")
    if user_word == secret_word:
        print("You've successfully left the loop.")
        break
