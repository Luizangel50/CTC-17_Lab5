import Board
from Helper import calculateFitness, calculateNeighbors
from time import time
from copy import copy, deepcopy
from random import random, randint


# Array with board's sizes
SIZES_BOARD = [8]

# Population size
POP_SIZE = 30

# Maximum number of generations
# created by the algorithm
MAX_GENERATION = 100

# Crossover constant (number between 0 and 1): Binomial crossover
CR = 0.15

# Mutation constant (number between 0 and 1)
MU = 0.001

def main():
	"""Main function"""

	# For each board's size, execute the Differential Evolution genetic algorithm,
	# print the final state, the final cost of the final state and the execution time
	for boardSize in SIZES_BOARD:

		print "*************************", boardSize, "X", boardSize, "BOARD", "*************************"
		board = Board.Board(boardSize, POP_SIZE)

		initialTime = time()
		differentialEvolution(board)
		finalTime = time() - initialTime

		bestFitness = [0, 0]
		for i in range(0, board.popSize):
			if calculateFitness(board, i) > bestFitness[1]:
				bestFitness = [i, calculateFitness(board, i)]
		
		print "One best solution:", board.population[bestFitness[0]]
		print "Final Fitness:", bestFitness[1]
		print "Population size:", POP_SIZE
		print "Number of generations:", MAX_GENERATION
		print "Crossover constant:", CR
		print "Mutation constant:", MU
		print "Execution time:", finalTime
		print

def differentialEvolution(board):
	"""Function that implements the Differential Evolution genetic algorithm"""

	# For each generation
	for j in range(0, MAX_GENERATION):

		# For each population element
		for i in range(0, board.popSize):

			# Select a pair element to make a child element
			pairElement = selectPairElement(board, i)

			# Change genes between the parents
			crossoverElements(board, i, pairElement)

			# Possible mutation may occur
			mutation(board, i)
			

def selectPairElement(board, currentElement):
	"""Function that select a different element from currentElement
	that will combine with currentElement to make a childElement"""

	# Select a random pairElement that is different from currentElement
	while True:
		pairElement = randint(0, board.popSize - 1)
		if currentElement != pairElement:
			return pairElement


def crossoverElements(board, currentElement, pairElement):
	"""Function that combines the 'genes' from each parent element to make
	a childElement and analyse if the child improves the parent's Fitness"""

	childElement = []
	for i in range(0, board.boardSize):

		# If a random number is minor than the crossover constant,
		# take the 'gene' from pairElement; otherwise, take the 'gene' from currentElement
		if random() < CR:
			childElement.append(board.population[pairElement][i])
		else:
			childElement.append(board.population[currentElement][i])

	currentFitness = calculateFitness(board, currentElement)
	parentElement = list(board.population[currentElement])

	board.population[currentElement] = list(childElement)
	newFitness = calculateFitness(board, currentElement)

	# Analyse if childElement is better than currentElement
	if newFitness < currentFitness:
		board.population[currentElement] = list(parentElement)


def mutation(board, currentElement):
	"""Function that aplies to a population element a mutation on some
	of its 'gene'"""

	# If a random number is minor than the mutation constant,
	# so will occur a mutation on the element; otherwise, nothing happens
	if random() < MU:
		randomIndex = randint(0, board.boardSize - 1)
		randomValue = randint(0, board.boardSize - 1)
		board.population[currentElement][randomIndex] = randomValue


if __name__ == "__main__":
	main()