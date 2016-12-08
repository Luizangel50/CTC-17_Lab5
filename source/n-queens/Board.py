import sys
from random import randint

class Board:
	"""Class that especifies states of a chess board for n-queens problem"""


	def __init__(self, boardSize, popSize):
		"""Constructor"""

		self.boardSize = boardSize									# Boards of (size x size) cells with (size) queens, with size > 4
		self.maximumFitness = self.boardSize*(self.boardSize-1)/2	# Maximum fitness value cost for the kind of board used
		self.popSize = popSize										# Number of elements on the population
		self.population = self.initializePopulation()				# Current state of the board

	
	def initializePopulation(self):
		"""Function that initializes the population of boards with a array in which each index represents
		a column and the value associated represents the row (initial generation)"""

		population = []

		# For each element of population, select a
		# random state configuration
		for i in range(0, self.popSize):
			element = []

			for j in range(0, self.boardSize):
				element.append(randint(0, self.boardSize - 1))

			population.append(element)

		return population
