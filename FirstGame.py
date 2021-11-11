

""""









						Welcome to my first offical program





																			
																								"""




input ("Press enter at any point to continue throughout the game.")
nameuser = input ("What is your name? ")
print ("I wish they paid me enough to care.")
input()
play = input ("Do you want to play a game? [Y/N]: ")
if play.lower() == ("y"):
	game = input ("Awesome, what game do you want to play? \n Guess the number [1] \n Mad Lib [2] \n Triva [3] \n: ")
elif play.lower() == ("n"):
	sure1 = input ("Are you sure? [Y/N]: ")
	if sure1.lower() == ("y"):
		print ("Ok, screw you then")
		game = "testing"
	elif sure1.lower() == ("n"):
		play1 = input ("So you do want to play? [Y/N]: ")
		if play1.lower() == ("y"):
			game = input ("Awesome, what game do you want to play? \n Guess the number [1] \n Mad Lib [2] \n Triva [3] \n: ")
		elif play1.lower() == ("n"):
			print ('Fine I guess...')
			game = "tetsing"

if game == ("1"):
	import random 
	number = random.randint(1, 10)
	tries = 1
	guess = int (input("I'm thinking of a number between 1-10, guess what it is: " ))
	if guess > number:
		print ("Lower you moron!")
	elif guess < number:
		print ("Higher you moron!")
	elif guess == number:
		print ("You got it first try!!")
	while guess != number:
		tries += 1
		guess = int(input("Try again: "))
		if guess < number:
			print ("Higher you idiot!")
		elif guess > number:
			print ("Lower you idiot!")
		elif guess == number:
			print ("You guessed it! And it only took you", tries, "tries!")
elif game == ("2"):
	print ("Awesome! You want to play Mad Libs!")
	input ()
	print ("This game is simple, just input what is asked")
	input ()
	noun1 = input("Noun: ")
	state = input("State: ")
	verb1 = input("Verb (past tense): ")
	noun2 = input("Noun: ")
	name = input ("Proper name: ")
	noun3 = input("Noun: ")
	noun4 = input("Noun: ")
	body = input("Body Part: ")
	adj = input("Adjective: ")
	relative = input ("Relative: ")
	act = input ("Activity: ")
	food = input ("Fast Food Resturant: ")
	adj2 = input ("Verb (Past tense): ")
	month = input ("Month: ")
	verb3 = input ("Verb: ")
	noun5 = input ("Noun: ")
	verb4 = input ("Verb (Past tense): ")
	adj3 = input( "Adjective: ")
	verb5 = input ("Verb: ")
	obj = input ("Object: ")
	noun6 = input("Plural Noun: ")
	verb2 = input("Verb( -ing): ")
	print ("You're finally done")
	input()
	seelib = input ('Would you like to see your Mad Lib?[Y/N]')
	if seelib.lower() == "y":
		print ("A", noun1, "in",state, "was arrested this morning after he", verb1, "in front of", noun2 ,".", name , ", had a history of", verb2 , ", but no one - not even his" , noun3 , "- ever imagined he'd" , verb3 , "with a", noun4, "stuck in his", body, ".", "'I always thought he was", adj + ", but never thought he'd do something like this. Even his", relative, "was surprised.' After a breif", act, "cops followed him to a", food +", where he reportedly", adj2, "in the fry machine. In", month+ ", a woman was charged with a similar crime. But rather than", verb3, "with a", noun5 + ", she", verb4, "with a", adj3, "dog. Either way, we imagine that after witnessing him", verb5, "with a", noun5, "there are probably a whole lot of", noun6, "that are going to need some therapy.")
	elif seelib.lower() == "n":
		print ("I mean... I guess you wasted all that time for nothing then.")
elif game == ("3"):
	score = 0
	total = 4
	print ("What kind of loser chooses trivia?")
	input ()
	triviagame = input ("Whatever, what would you like to do trivia about?: \n Math [1] \n Computers [2] \n The Programmer[3] \n :")
	if triviagame == ("1"): 
		print ("Math? Yeah... you really are a nerd")
		input()
		ans = input ("solve for x: 2x - 4y = 9? \n x = ")
		if ans == ("9/2"):
			print ("Correct!")
			score += 1
		else:
			print ("You're an idiot!")
		ans = input ("solve for x: 7 - 2 + x = 12 \n x = ")
		if ans == ("7"):
			print ("Correct!")
			score += 1
		else:
			print ("You're an idiot!")
		ans = input ("What is 20% of 30 dollars? ")
		if ans == ("6"):
			print ("Correct!")
			score += 1
		else:
			print ("You're an idiot!")
		ans = input ("30 is 60% of what number? ")
		if ans == ("50"):
			print ("Correct!")
			score += 1
		else:
			print ("You're an idiot!")
		print ("You have finished the math quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
	elif triviagame == ("2"):
		print ("Computers? Ok nerd.")
		input()
		ans = input ("What command do you use to output a string in python? " )
		if ans == ("print"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("What command am is being used to get your answer? ")
		if ans == ("input"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("What command would you use to declare a variable? ")
		if ans == ("="):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("What command would you use to determine if a variable is equal to something? ")
		if ans == ("=="):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		print ("You have finished the computer quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
	elif triviagame == ("3"):
		print ("You think you know about the man behind the scenes? Lets find out!")
		input()
		ans = input ("What is the programmers first name? ")
		if ans == ("Jai'Mir"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("What month was the programmer born in? ")
		if ans.lower == ("may"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("How many siblings does the programmer have? ")
		if ans == ("5"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
		ans = input ("Does the programmer have a pet [Y/N]? ")
		if ans.lower == ("y"):
			print ("Correct!")
			score += 1
		else:
			print ("No, you idiot.")
			print ("You have finished the programmer quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
#Do you want to play another game?
input()
playagain = input ("Do you want to play another game? [Y/N]: ")
while playagain == ("y"):
	play = input("What would you like to play next? \n Guess the number [1] \n Mad Lib [2] \n Triva [3] \n: ")
	if play == ("1"):
		import random 
		number = random.randint(1, 10)
		tries = 1
		guess = int (input("I'm thinking of a number between 1-10, guess what it is: " ))
		if guess > number:
			print ("Lower you moron!")
		elif guess < number:
			print ("Higher you moron!")
		elif game == number:
			print ("You got it first try!!!")
		while guess != number:
			tries += 1
			guess = int(input("Try again: "))
			if guess < number:
				print ("Higher you idiot!")
			elif guess > number:
				print ("Lower you idiot!")
			elif guess == number:
				print ("You guessed it! And it only took you", tries, "tries!")
		playagain = input ("Do you want to play another game? [Y/N]: ")
	if play == ("2"):
		print ("Awesome! You want to play Mad Libs!")
		input ()
		print ("This game is simple, just input what is asked")
		input ()
		noun1 = input("Noun: ")
		state = input("State: ")
		verb1 = input("Verb (past tense): ")
		noun2 = input("Noun: ")
		name = input ("Proper name: ")
		noun3 = input("Noun: ")
		noun4 = input("Noun: ")
		body = input("Body Part: ")
		adj = input("Adjective: ")
		relative = input ("Relative: ")
		act = input ("Activity: ")
		food = input ("Fast Food Resturant: ")
		adj2 = input ("Verb (Past tense): ")
		month = input ("Month: ")
		verb3 = input ("Verb: ")
		noun5 = input ("Noun: ")
		verb4 = input ("Verb (Past tense): ")
		adj3 = input( "Adjective: ")
		verb5 = input ("Verb: ")
		obj = input ("Object: ")
		noun6 = input("Plural Noun: ")
		verb2 = input("Verb( -ing): ")
		print ("You're finally done")
		input()
		seelib = input ('Would you like to see your Mad Lib?[Y/N]')
		if seelib.lower() == "y":
			print ("A", noun1, "in",state, "was arrested this morning after he", verb1, "in front of", noun2 ,".", name , ", had a history of", verb2 , ", but no one - not even his" , noun3 , "- ever imagined he'd" , verb3 , "with a", noun4, "stuck in his", body, ".", "'I always thought he was", adj + ", but never thought he'd do something like this. Even his", relative, "was surprised.' After a breif", act, "cops followed him to a", food +", where he reportedly", adj2, "in the fry machine. In", month+ ", a woman was charged with a similar crime. But rather than", verb3, "with a", noun5 + ", she", verb4, "with a", adj3, "dog. Either way, we imagine that after witnessing him", verb5, "with a", noun5, "there are probably a whole lot of", noun6, "that are going to need some therapy.")
		elif seelib.lower() == "n":
			print ("I mean... I guess you wasted all that time for nothing then.")
		playagain = input ("Do you want to play another game? [Y/N]: ")
	if play == ("3"):
		score = 0
		total = 4
		print ("What kind of loser chooses trivia?")
		input ()
		triviagame = input ("Whatever, what would you like to do trivia about?: \n Math [1] \n Computers [2] \n The Programmer[3] \n :")
		if triviagame == ("1"): 
			print ("Math? Yeah... you really are a nerd")
			input()
			ans = input ("solve for x: 2x - 4y = 9? \n x = ")
			if ans == ("9/2"):
				print ("Correct!")
				score += 1
			else:
				print ("You're an idiot!")
			ans = input ("solve for x: 7 - 2 + x = 12 \n x = ")
			if ans == ("7"):
				print ("Correct!")
				score += 1
			else:
				print ("You're an idiot!")
			ans = input ("What is 20% of 30 dollars? ")
			if ans == ("6"):
				print ("Correct!")
				score += 1
			else:
				print ("You're an idiot!")
			ans = input ("30 is 60% of what number? ")
			if ans == ("50"):
				print ("Correct!")
				score += 1
			else:
				print ("You're an idiot!")
			print ("You have finished the math quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
		elif triviagame == ("2"):
			print ("Computers? Ok nerd.")
			input()
			ans = input ("What command do you use to output a string in python? " )
			if ans == ("print"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("What command am is being used to get your answer? ")
			if ans == ("input"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("What command would you use to declare a variable? ")
			if ans == ("="):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("What command would you use to determine if a variable is equal to something? ")
			if ans == ("=="):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			print ("You have finished the computer quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
		elif triviagame == ("3"):
			print ("You think you know about the man behind the scenes? Lets find out!")
			input()
			ans = input ("What is the programmers first name? ")
			if ans == ("Jai'Mir"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("What month was the programmer born in? ")
			if ans.lower == ("may"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("How many siblings does the programmer have? ")
			if ans == ("5"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
			ans = input ("Does the programmer have a pet [Y/N]? ")
			if ans.lower == ("y"):
				print ("Correct!")
				score += 1
			else:
				print ("No, you idiot.")
				print ("You have finished the programmer quiz! \n You've answered a total of", score, "questions right!" "\n You got a", score/total*100, "%")
		playagain = input ("Do you want to play another game? [Y/N]: ")
if playagain == ("n"):
	print ("Thank you for playing", nameuser + "!")
		
		
	



