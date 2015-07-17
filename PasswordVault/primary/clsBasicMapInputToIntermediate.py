'''
Created on Jul 15, 2015

@author: Owner
'''
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper

class BasicMapInputToIntermediate(object):
	'''
	classdocs
	'''
	def __init__(self, pStringJoinerAndCombiner, pPasswordList, pIntermediate):
		'''
		Constructor
		'''
		lclJoinedAndCombinedInput = pStringJoinerAndCombiner.joinAndCombine(pPasswordList)
		self.differenceMapper = BasicDifferenceMapper(lclJoinedAndCombinedInput, pIntermediate)
		self.stringJoinerAndCombiner = pStringJoinerAndCombiner
		
	
	def compute(self, pPasswordList):
		lclJandC = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		return self.differenceMapper.compute(lclJandC)