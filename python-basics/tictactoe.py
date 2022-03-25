import sys

board = {"top-L":" ", "top-M":" ", "top-R":" ",
	"mid-L":" ", "mid-M":" ", "mid-R":" ",
	"bot-L":" ", "bot-M":" ", "bot-R":" "}

def displayer(board):
	lineseperator = 0
	for i in board.values():
		print(i + "|", end="")
		lineseperator += 1

		if lineseperator % 3 == 0:
			print("\n------")


def controller(board):
	choice = input("Enter X or O: ")
	coordinate = input("Enter coordinate: ")
	try:
		if board[coordinate] != " ":
			print("That coordinate is already filled")
			return

		if choice == "X":
			board[coordinate] = "X"
		elif choice == "O":
			board[coordinate] = "O"
	except KeyError:
		print("Enter a valid input in the next time")

	if board["top-L"] == board["top-M"] and board["top-M"] == board["top-R"] and (board["top-R"] == "X" or board["top-R"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()
	elif board["mid-L"] == board["mid-M"] and board["mid-M"] == board["mid-R"] and (board["mid-R"] == "X" or board["mid-R"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()
	elif board["bot-L"] == board["bot-M"] and board["bot-M"] == board["bot-R"] and (board["bot-R"] == "X" or board["bot-R"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()
	elif board["bot-L"] == board["mid-L"] and board["top-L"] == board["bot-L"] and (board["top-L"] == "X" or board["top-L"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()
	elif board["top-M"] == board["bot-M"] and board["mid-M"] == board["bot-M"] and (board["top-M"] == "X" or board["top-M"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()
	elif board["bot-R"] == board["mid-R"] and board["top-R"] == board["bot-R"] and (board["top-R"] == "X" or board["top-R"] == "O"):
		displayer(board)
		print("TIC-TAC-TOE")
		sys.exit()

while True:
	displayer(board)
	controller(board)
