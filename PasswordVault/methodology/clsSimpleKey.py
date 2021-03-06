'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsDLPHash import DLPHash

class SimpleKey(object):
	'''
	classdocs
	'''
	
	def __init__(self, pValidationCode, pDifferenceMapper, pHash, pJoinerAndCombiner = BasicStringJoinerAndCombiner(), pConverter = BasicStringIntConverter()):#, pInputToIntermediate = BasicMapInputToIntermediate(), pIntermediateToResult = BasicMapIntermediateToResult()):
		'''
		Constructor
		'''
		self.validationCode = pValidationCode
		self.differenceMapper = pDifferenceMapper
		self.hash = pHash
		self.converter = pConverter
		self.joinerAndCombiner = pJoinerAndCombiner
		
		#self.inputToIntermediate = pInputToIntermediate
		#self.intermediateToResult = pIntermediateToResult
		
	def compute(self, pPasswordList):
		lclJoinedAndCombined = self.joinerAndCombiner.joinAndCombine(pPasswordList)
		lclHashed = self.hash.compute(lclJoinedAndCombined)
		if self.hash.compute(lclHashed) != self.validationCode:
			print("Validation not passed.")
			return -1
		lclResultAsInt = self.differenceMapper.compute(lclHashed)
		return self.converter.toString(lclResultAsInt)
	
	def toString(self):
		return "(simple, " + self.hash.toString() + ", " + self.differenceMapper.toString() + ")"