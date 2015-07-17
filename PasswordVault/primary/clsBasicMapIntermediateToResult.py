'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper

class BasicMapIntermediateToResult(object):
	'''
	classdocs
	'''
	def __init__(self, pOneWayHashFunction, pIntermediate, pResult):
		'''
		Constructor
		'''
		self.oneWayHashFunction = pOneWayHashFunction
		lclHashed = pOneWayHashFunction.compute(pIntermediate)
		self.differenceMapper = BasicDifferenceMapper(lclHashed, pResult)
	
	def compute(self, pIntermediate):
		lclHashed = self.oneWayHashFunction.compute(pIntermediate)
		return self.differenceMapper.compute(lclHashed)