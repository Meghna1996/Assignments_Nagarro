import random

def guess_game():
	secret_number = random.randint(0,5)
	tries = 0
	max_tries = 5
	while tries < max_tries:
	    number = int(input("Guess a number b/w(0,5): "))
	    if number == secret_number:
	        print("You guessed the number!")
	        break;
	    tries+=1

	if( tries == max_tries ):
	    print("Better luck next time")

guess_game()