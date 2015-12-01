from random import randint

correct_number = randint(0,10)

turn = 0

def number_guesser():
	global turn
	while turn < 3:
		guess_number = int(raw_input("Guess a Number Between 1 and 10: "))
		turn = turn + 1
		if guess_number == correct_number:
			turn = turn + 2
			print "Holy fuck! You're right!"
		elif guess_number > 10 or guess_number < 1:
			print "I said between 1 and 10, asshole"
		elif guess_number < correct_number:
			print "That's lower than squerrel nuts, go up some son."
		elif guess_number > correct_number:
			print "You're not guessing my dick size, try a lower number."	
		else:
			print "No, try again ffs."

number_guesser()
