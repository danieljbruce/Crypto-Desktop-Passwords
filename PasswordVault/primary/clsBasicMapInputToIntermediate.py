'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper

class BasicMapInputToIntermediate(object):
	'''
	classdocs
	'''
	def __init__(self, pDifferenceMapper = BasicDifferenceMapper(), pStringJoinerAndCombiner = BasicStringJoinerAndCombiner()):
		'''
		Constructor
		'''
		self.stringJoinerAndCombiner = pStringJoinerAndCombiner
		self.differenceMapper = pDifferenceMapper
	
	def defineMap(self, pPasswordList, pIntermediate):
		lclJoinedAndCombinedInput = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		self.differenceMapper.defineMap(lclJoinedAndCombinedInput, pIntermediate)
	
	def compute(self, pPasswordList):
		lclJandC = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		return self.differenceMapper.compute(lclJandC)
	
	def encodeMap(self):
		return self.differenceMapper.difference