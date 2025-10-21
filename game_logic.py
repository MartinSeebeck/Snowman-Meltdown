import stages
import random

# List of secret words
WORDS = ["git", "github", "python", "snowman", "meltdown"]

def get_random_word():
	"""Selects a random word from the list."""
	return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
	# Display the snowman stage for the current number of mistakes.
	print(stages.STAGES[mistakes])
	# Build a display version of the secret word.
	display_word = ""
	for letter in secret_word:
		if letter in guessed_letters:
			display_word += letter + " "
		else:
			display_word += "_ "
	print("Word: ", display_word)
	print("\n")

def play_game():
	game_end = False
	guessed_letters = []
	missed_letters = []
	mistakes = 0
	secret_word = get_random_word()
	max_mistakes = 4
	print("Welcome to Snowman Meltdown!")
	print("Your job is to guess the word, hangman-style.")
	#Display the initial game state.
	while not game_end:
		display_game_state(mistakes, secret_word, guessed_letters)
		# Prompt user for guess
		guess = input("Guess a single letter: ").lower()
		if guess == "":
			#Make sure no accidental miss happens, no punishment
			print("No guess recorded.")
			continue
		if len(guess) > 1:
			#Make sure no double or triple entry messes up the gameplay, no punishment
			print("Just single letters allowed.")
			continue
		print("You guessed:", guess)
		if guess in guessed_letters:
			#Make sure no double correct entry happens, no punishment
			print("You already guessed that one, hit again!")
			continue
		if guess in missed_letters:
			#Make sure no double incorrect entry happens, w/ punishment
			print("You already guessed that one, be careful!")
		if guess in secret_word:
			print("Good shot!")
			#Append correct guesses to comparison list
			guessed_letters.append(guess)
			if not len(guessed_letters) == len(secret_word): #winning condition
				print(f"{max_mistakes - mistakes} misses left.")
			else:
				print("You have guessed correctly!")
				print(f"The word we were looking for is {secret_word}!")
				print("And you have saved the poor snowman!")
				game_end = True
		else:
			mistakes += 1
			if not mistakes == max_mistakes:
				print("No, try again!")
				missed_letters.append(guess)
				print(f"{max_mistakes - mistakes} misses left.")
			else:
				print(f"{max_mistakes - mistakes} misses left.") #losing condition
				display_game_state(mistakes, secret_word, guessed_letters)
				print("The jig is up!")
				print("All the snow has melted ...")
				game_end = True

