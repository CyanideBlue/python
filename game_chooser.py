

def game_chooser():
	choice = raw_input("For a (L)ist of available games\
	please select L. Otherwise please enter your game \
	number to begin:  ")
	if choice == "L":
		print "(0)ne. Guess my Number (explicit)."
		game_chooser()
	elif choice != "L" and choice != "0":
		print "That's not a fucking option. \
		Select L for (L)ist, otherwise enter \
		the number of the game you'd like to \
		play, fuckass."
		game_chooser()
	elif choice == "0":
		import guessing_game
		game_chooser()
	else:
		print "I don't know how but you broke \
		it. Fuck you!"


game_chooser()
