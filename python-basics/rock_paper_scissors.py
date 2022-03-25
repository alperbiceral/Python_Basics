import random

print("Rock Paper Scissors".upper())
wins = 0
loses = 0
ties = 0
choice = 0
numChoice = 0

def displayResult(numChoice, AIChoice, wins, loses, ties):
	result = (numChoice - AIChoice) % 3

	if result == 0:
		print("It is a tie")
		ties += 1
	elif result == 1:
		print("You win!")
		wins += 1
	elif result == 2:
		print("Computer wins!")
		loses += 1

	return wins, loses, ties


def displayAIChoice(AIChoice):
	if AIChoice == 0:
		print("Rock")
	elif AIChoice == 1:
		print("Paper")	
	elif AIChoice == 2:
		print("Scissors")

def status(wins, loses, ties):
	global choice
	print(str(wins) + " wins, " + str(loses) + " loses," + str(ties) + " ties.")
	choice = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ")

while True:
	status(wins, loses, ties)

	if choice == "p":
		numChoice = 1
		print("Paper versus...")
	elif choice == "r":
		print("Rock versus...")
		numChoice = 0
	elif choice == "s":
		print("Scissors versus...")
		numChoice = 2
	elif choice == "q":
		print("Quiting...")
		break
	else:
		print("\nr, p, s or q are the valid inputs. Please try again.\n")
		continue

	AIChoice = random.randint(0, 3)
	displayAIChoice(AIChoice)
	wins, loses, ties = displayResult(numChoice, AIChoice, wins, loses, ties)
