
import math

from percolation import Percolation, Trial




class PercolationStats:

	def __init__(self, n):
		
		self.n = n
		
		
		self.trialResults = []
		self.trialFractions = []

		self.trials = 0
	
		


	def add_res(self, open_sites):
		self.trials += 1
		self.trialResults.append(open_sites)
		self.trialFractions.append(open_sites / self.n ** 2)


	def mean(self):

		if self.trials > 0:
			return self.trials and sum(self.trialFractions) / self.trials
		return 0
	
	
	def stddev(self):
		if self.trials == 0:
			return 0

		mean = self.mean()
		
		denom = self.trials - 1 if self.trials > 1 else self.trials
		
		stddev_sq = sum((t - mean)**2 for t in self.trialFractions) / denom
		
		return math.sqrt(stddev_sq)

	def confidenceInt(self):
		if self.trials > 0:
			mean = self.mean()
			addend_minuend = 1.96 * self.stddev()/math.sqrt(self.trials)

			return mean - addend_minuend, mean + addend_minuend
		return 0, 0

	
	def __repr__(self):
		conf_int_lo, conf_int_hi = self.confidenceInt()
		return f'mean = {round(self.mean(), 4)},\
		 stddev = {round(self.stddev(), 4)},\
		 confidence interval = ({round(conf_int_lo, 4)}, {round(conf_int_hi, 4)})' 

	def getStats(self):
		mean, stddev = self.mean(), self.stddev() 
		conf_lo, conf_hi = self.confidenceInt()

		return self.trials, round(mean, 4), round(stddev, 4), round(conf_lo, 4), round(conf_hi, 4)


