import stages
import game_logic


if __name__ == "__main__":
	game_logic.play_game()
	print("*********************")
	encore = input("Do you want to play once more? (Y/N) ")
	if encore == "Y":
		print("Your wish is granted.")
		game_logic.play_game()
	elif encore == "y":
		print("Your wish is granted.")
		game_logic.play_game()
	else:
		print("Thank you for playing!")

