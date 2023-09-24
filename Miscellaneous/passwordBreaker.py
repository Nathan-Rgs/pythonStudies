import time, random

guess = ""
password = input("Type the password that you want me to discover: ")

# possible_inputs = [
#     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç",
#     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
#     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç",
#     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
#     "!", "@", "#", "$", "%", "&", "*", "_", "-", "+", "=", "?", "(", ")", "'", '"', "{", "}"
# ]

possible_inputs = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç"
]

while (guess != password):
    start = time.time()
    guess = ""
    for char in password:
        # guessChar = possible_inputs[random.randint(0, 81)]
        guessChar = possible_inputs[random.randint(0, 26)]
        guess = str(guessChar) + str(guess)
        print(guess)
end = time.time()

print(f"Password discovered: {guess}")
print(f"Time spent for discovering: {end - start} seconds")
