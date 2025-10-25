'''
Suggestions for Improvement:

- The check for the winning condition (`if not len(guessed_letters) == len(secret_word)`) is incorrect, as it compares the number of guessed letters to the word length
without ensuring all letters in the secret word are guessed. Instead, verify if all letters in `secret_word` are in `guessed_letters`.
## I renamed the variable to be less misleading and implemented a for loop accordingly

- While the code checks for single-letter inputs and empty guesses, it could also validate that the input is an alphabetical character (e.g., using `guess.isalpha()`).
##DONE

- Some lines (e.g., comments in `game_logic.py`) could be formatted to adhere to PEP 8, such as keeping lines under 79 characters and adding consistent spacing around operators.
##DONE

- In `snowman.py`, the replay logic checks for both "Y" and "y" separately, which is redundant. Simplify this by converting the input to uppercase or lowercase for comparison.
##DONE

'''


import stages
import random
import fontclass

# List of secret words
WORDS = ["snowman", "meltdowns", "github", "git", "masterschool"]

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
	print(fontclass.Fontclass.OKBLUE, "Word: ", display_word, fontclass.Fontclass.ENDC)
	print("\n")

def play_game():
	game_end = False
	temp_winning_check_counter = 0
	correct_letters = []
	missed_letters = []
	mistakes = 0
	secret_word = get_random_word()
	max_mistakes = 4
	print(fontclass.Fontclass.HEADER+"Welcome to Snowman Meltdown!"+fontclass.Fontclass.ENDC)
	print("Your job is to guess the word, hangman-style.")
	#Display the initial game state.
	while not game_end:
		display_game_state(mistakes, secret_word, correct_letters)
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
		if not guess.isalpha():
			print("Please neither numbers nor special characters, just plain old alphabet (UTF-7, if you must know).")
			continue
		print("You guessed:", guess)
		if guess in correct_letters:
			#Make sure no double correct entry happens, no punishment
			print(fontclass.Fontclass.WARNING + "You already guessed that one, hit again!"+fontclass.Fontclass.ENDC)
			continue
		if guess in missed_letters:
			#Make sure no double incorrect entry happens, w/ punishment
			print(fontclass.Fontclass.WARNING + "You already guessed that one, be careful!"+fontclass.Fontclass.ENDC)
		if guess in secret_word:
			print(fontclass.Fontclass.OKGREEN +"Good shot!"+fontclass.Fontclass.ENDC)
			#Append correct guesses to comparison list
			correct_letters.append(guess)
			# Reset the win-check counter for this round
			temp_winning_check_counter = 0
			for char in secret_word:
				if char in correct_letters:
					temp_winning_check_counter += 1
			if temp_winning_check_counter == len(secret_word):
				print(fontclass.Fontclass.OKGREEN + "You have guessed correctly!" + fontclass.Fontclass.ENDC)
				print(f"The word we were looking for is {secret_word}!")
				print("And you have saved the poor snowman!")
				game_end = True
			else:
				print(f"{max_mistakes - mistakes} misses left.")
		else:
			mistakes += 1
			if not mistakes == max_mistakes:
				print(fontclass.Fontclass.WARNING + "No, try again!"+fontclass.Fontclass.ENDC)
				missed_letters.append(guess)
				print(f"{fontclass.Fontclass.WARNING}{max_mistakes - mistakes} misses left."+fontclass.Fontclass.ENDC)
			else:
				print(f"{fontclass.Fontclass.WARNING}{max_mistakes - mistakes} misses left."+fontclass.Fontclass.ENDC) #losing condition
				display_game_state(mistakes, secret_word, correct_letters)
				print("The jig is up!")
				print("All the snow has melted ...")
				game_end = True

