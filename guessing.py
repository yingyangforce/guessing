import random

# guess the number game - limited guesses w/ hot, cold hints

up_bound = 10

theint = random.randint(1, up_bound)

num_guess = 0

guess_lim = 5

while num_guess < guess_lim:

