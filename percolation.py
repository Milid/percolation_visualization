
from collections import defaultdict
class Percolation:

	
	def __init__(self, n):
		self.n = n
		self.length = n * n
		self.id = [i  for i in range(self.length + 2)]
		self.openSites = [False for i in range(self.length + 2)]
		self.openSites[0], self.openSites[self.length + 1] = True, True
		
		self.unions = defaultdict(set)
		self.unions[0].add(0)
		
		self.newFillingUnion = None

		
		
		self.totalOpenSites = 0

	def getIndex(self, row, col):
		return self.n * row + col + 1

	def getRowCol(self, index):
		return (index - 1) // self.n, (index - 1) % self.n

	def open(self, row, col):
		self.newFillingUnion = None
		self.totalOpenSites += 1
		index = self.getIndex(row, col)
		self.openSites[index] = True
		self.unions[index].add(index)
		if row == 0:
			self.union(index, 0)
		if row == self.n-1:
			self.unions[index].add(self.length + 1)
		neighbors = self.getNeighborRowCol(row, col)
		for i, j in neighbors:
			if self.isOpen(i, j):
				self.union(index, self.getIndex(i, j))

	def openIndex(self, index):

		self.totalOpenSites += 1
		row, col = self.getRowCol(index)
		self.openSites[index] = True
		self.unions[index].add(index)
		if row == 0:
			self.union(index, 0)
		if row == self.n-1:
			self.unions[index].add(self.length + 1)
		neighbors = self.getNeighborRowCol(row, col)
		for i, j in neighbors:
			if self.isOpen(i, j):
				self.union(index, self.getIndex(i, j))




	def getNeighborRowCol(self, r, c):
		return ([(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if i in range(self.n) and j in range(self.n) ])

	def getNeighborIndices(self, row, col):
		neighbors = []
		neigborRowCols = self.getNeighborRowCol(row, col)
		for i, j in neigborRowCols:
			neighbors.append(self.getIndex(i, j))
		return neighbors

	def getNeighbors(self, row, col):
		neighbors = []
		neighborIndices = self.getNeighborIndices(row, col)
		for i in neighborIndices:
			neighbors.append(self.id[i])

		return neighbors







	def union(self, p, q):

		
		parentP = self.find(p)
		parentQ = self.find(q)
		if parentP == parentQ:
			return                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

		minSizeParent, maxSizeParent = parentP, parentQ
		if len(self.unions[parentP]) > len(self.unions[parentQ]):
			minSizeParent, maxSizeParent = parentQ, parentP
		if minSizeParent == 0:
			minSizeParent, maxSizeParent = maxSizeParent, minSizeParent


		


		
		self.id[minSizeParent] = self.id[maxSizeParent]
		if len(self.unions[minSizeParent]) == 1:
			self.unions[maxSizeParent].add(minSizeParent)

			
		else:
			self.unions[maxSizeParent] = self.unions[maxSizeParent].union(self.unions[minSizeParent])

		del self.unions[minSizeParent]
		#print(f'unions = {self.unions}')



	def isOpen(self, row, col):
		index = self.getIndex(row, col)
		return self.openSites[index]

	def find(self, index):
		
		while index != self.id[index]:
			index = self.id[index]
		return index
	


	
	def isFull(self,row, col):
		index = self.getIndex(row, col)
		return index in unions[0]

	def numberOfOpenSites(self):
		return self.totalOpenSites

	
	
	def printAsMatrix(self, low_ind, high_ind, arr, width):
		for i in range(low_ind, high_ind):

			print(i, ':', arr[i], ', ', end = '')
			if i % width == 0:
				print('\n')

	def printSite(self, row, col):
		index = self.getIndex(row, col)
		print(f'index = {index}')
		print(f'id = {self.id[index]}; open = {self.openSites[index]}; full = {self.full[index]}; size = {self.size[index]} ')
		print()


	def isFilled(self, index):
		return index in unions[0]

	def isFilled_1(self, index):
		return self.percolated[index]
	
	def percolates(self):
		return self.length + 1 in self.unions[0]



import random
class Trial:

	def __init__(self, n):

		self.n = n
		self.nGrid = Percolation(n)
		self.queueToOpen = [i for i in range(1, n*n + 1)]
		random.shuffle(self.queueToOpen)

	def getNGrid(self):
		return self.nGrid

	def getRandomIndex(self):
		index = 0
		while self.nGrid.openSites[index]:
			index = random.randint(1, self.nGrid.length)
		return index

	def getIndexFromQueue(self):
		if self.queueToOpen:
			index = self.queueToOpen.pop()
			return index

	
	def openSite(self, index):
		
		self.nGrid.openIndex(index)
		
	def getNumberOfOpenSites(self):
		return self.nGrid.numberOfOpenSites()

	def performTrial(self):
		while True:
			if self.nGrid.percolates():
				break

			index = self.getIndexFromQueue()
			self.openSite(index)


		return self.getNumberOfOpenSites()
