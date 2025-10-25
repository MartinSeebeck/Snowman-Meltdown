import stages
import game_logic
import fontclass


if __name__ == "__main__":
	game_logic.play_game()
	print("*********************")
	encore = input(fontclass.Fontclass.OKCYAN + "Do you want to play once more? (Y/N) "+fontclass.Fontclass.ENDC)
	encore = encore.upper()
	if encore == "Y":
		print(fontclass.Fontclass.OKCYAN + "Your wish is granted."+fontclass.Fontclass.ENDC)
		game_logic.play_game()
	else:
		print("Thank you for playing!")

