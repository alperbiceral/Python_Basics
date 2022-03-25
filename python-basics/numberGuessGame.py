
import random
name = input("What is your name? ")
guessRight = 5
minLimit = 0
maxLimit = 20
print("Well " + name + ", guess a number. You will have " + str(guessRight) + " rights to guess between 0-20.")
correctNo = random.randint(minLimit, maxLimit)

def sayMyGuess(right, counter):
	print("You have " + str(right - counter) + " to go.")

counter = 0
found = False
while counter != guessRight:
	try:
		guess = int(input("Guess: "))
		if guess > maxLimit or guess < minLimit:
			print("Please guess the number between " + str(minLimit) + "-" + str(maxLimit))
			sayMyGuess(guessRight, counter)
			continue
		elif guess < correctNo:	
			print("Too low...")
			counter += 1
			sayMyGuess(guessRight, counter)
		elif guess > correctNo:
			print("Too high...")
			counter += 1
			sayMyGuess(guessRight, counter)
		else:
			print("OMG, you found :)")
			found = True
			break
	except ValueError:
		print("Please enter a number. This does not count as a guess.")
		sayMyGuess(guessRight, counter)
		continue

if not found:
	print("Correct answer is: " + str(correctNo))
