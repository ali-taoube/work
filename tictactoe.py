import random
global gameOver
gameOver = False
board = [[1,2,3],[4,5,6],[7,8,9,]]
currentPlayer = "X"
userInput = 0

def drawBoard():
	global board
	global userInput
	if board.count("X") + board.count("O") == 0:
		print('\033[H\033[J')
		print(' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]))
		print('-----------')
		print(' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]))
		print('-----------')
		print(' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]))
	if gameOver:
		return currentPlayer
	else:
		userInput = raw_input("Make a move: ")

print drawBoard()

def wwcd(matrix):
	global GameOver        
	x = 0
	y = 0
	if matrix[x][y] == matrix[x][y + 1] == matrix[x][y + 2]:
		gameOver = True
		return matrix[0][0]
	elif matrix[x][y] == matrix[x + 1][y] == matrix[x + 2][y]:
		gameOver = True                
		return matrix[x][y]
	elif matrix[x][y] == matrix[x + 1][y + 1] == matrix[x + 2][y + 2]:
		gameOver = True                
		return matrix[x][y]
	elif matrix[x][y + 2] == matrix[x + 1][y + 1] == matrix[x + 2][y]:
		gameOver = True                
		return matrix[0][2]
	elif board.count("X") + board.count("O") < 9:
		gameOver = True
		return "Tie!"

def switchTurn():
        global currentPlayer
        if currentPlayer == "X":
                currentPlayer = "O"
        else:
                currentPlayer = "X"

def processInput():
	global userInput
	global board
	global currentPlayer
	
	if userInput == "1":
		board[0][0] = currentPlayer
		switchTurn()
	if userInput == "2":
		board[0][1] = currentPlayer
		switchTurn()
	if userInput == "3":
		board[0][2] = currentPlayer
		switchTurn()
	if userInput == "4":
		board[1][0] = currentPlayer
		switchTurn()
	if userInput == "5":
		board[1][1] = currentPlayer
		switchTurn()
	if userInput == "6":
		board[1][2] = currentPlayer
		switchTurn()
	if userInput == "7":
		board[2][0] = currentPlayer
		switchTurn()
	if userInput == "8":
		board[2][1] = currentPlayer
		switchTurn()
	if userInput == "9":
		board[2][2] = currentPlayer
		switchTurn()

def playGame():
	while not gameOver:
		drawBoard()
		processInput()
		wwcd(board)

playGame()					

