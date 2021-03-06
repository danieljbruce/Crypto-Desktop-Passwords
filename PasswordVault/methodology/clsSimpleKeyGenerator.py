'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper
from methodology.clsDLPHash import DLPHash
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsBasicKey import BasicKey
from methodology.iKeyGenerator import iKeyGenerator
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from methodology.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from methodology.clsSimpleKey import SimpleKey

class SimpleKeyGenerator(object):
	'''
	classdocs
	'''

	def __init__(self):#, pConverter = BasicStringIntConverter(), pStringJoinerAndCombiner = BasicStringJoinerAndCombiner(), pDifferenceMapper = BasicDifferenceMapper(), pHash = DLPHash())#pMapInputToIntermediate = SimpleMapInputToIntermediate(), pMapIntermediateToResult = SimpleMapIntermediateToResult()):#pConverter, pStringJoiner, pCombiner):
		'''
		Constructor
		'''
		
		#self.stringJoinerAndCombiner = pStringJoinerAndCombiner
		#self.differenceMapper = pDifferenceMapper
		#self.hash = pHash
		#self.converter = pConverter
		
		#self.converter
		
		#self.stringJoiner = pStringJoiner
		
		#self.combiner = pCombiner	
		
	def generate(self, pInputPasswordList, pResult):
		lclDifferenceMapper = BasicDifferenceMapper()
		lclHashMap = DLPHash()
		lclConverter = BasicStringIntConverter()
		lclStringJoinerAndCombiner = BasicStringJoinerAndCombiner() 
		
		lclHashedValue = lclHashMap.compute(lclStringJoinerAndCombiner.joinAndCombine(pInputPasswordList))
		lclDifferenceMapper.defineMap(lclHashedValue, lclConverter.toInt(pResult))
		lclValidationCode = lclHashMap.compute(lclHashedValue) 
		return SimpleKey(lclValidationCode, lclDifferenceMapper, lclHashMap)
	
