import math


def calculateFitness(board, elementPop):
	"""Function that calculates the fitness for a board's state"""

	fitness = 0

	for i in range(0, board.boardSize):
		fitness += calculateNeighbors(board, elementPop, i)

	return board.maximumFitness - fitness

def calculateNeighbors(board, elementPop, currentCell):
	"""Auxiliar function that return the number of neighbors
	of currentCell on the board"""

	neighbors = 0
	rowMainDiagonal = board.population[elementPop][currentCell] + 1
	rowSecondaryDiagonal = board.population[elementPop][currentCell] - 1

	for i in range(currentCell + 1, board.boardSize):

		# Verify the same row
		if board.population[elementPop][i] == board.population[elementPop][currentCell]:
			neighbors += 1

		# Verify the main diagonal
		if rowMainDiagonal < board.boardSize and board.population[elementPop][i] == rowMainDiagonal:
			neighbors += 1

		rowMainDiagonal += 1

		# Verify the secondary diagonal
		if rowSecondaryDiagonal >= 0 and board.population[elementPop][i] == rowSecondaryDiagonal:
			neighbors += 1

		rowSecondaryDiagonal -= 1

	return neighbors
