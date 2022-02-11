import random
import time

# guess the number game - limited guesses w/ hot, cold hints

print("Welcome to the number guessing game. The game where you guess the number.")

up_bound = int(input("What's the upper bound for your guess range?: "))

the_int = random.randint(1, up_bound)

guess_count = 0
guess_lim = 5

print("\nThinking of a random number ", end="")

time.sleep(1)

for i in range(3):
    print(". ", end="", flush=True)
    time.sleep(1)

print("\n")

while guess_count < guess_lim:
    the_guess = int(input("What number guess ye?: ")
    guess_count += 1


