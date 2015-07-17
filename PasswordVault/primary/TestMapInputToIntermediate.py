'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''

import clsBasicCombiner
import cls

class TestMapInputToIntermediate(object):
	'''
	classdocs
	'''

	def __init__(self, params):
		'''
		Constructor
		'''
	
	def test_FullFunctionality(self):
		print("Running test FullFunctionality on TestMapIntermediateToResult.")
		
		lclStringJoiner = BasicStringJoiner()
		lclBasicCombiner = BasicCombiner()
		
		lclHash = BasicHash(BasicStringIntCoverter())
		lclMap = BasicMapIntermediateToResult(lclHash, 7, 14)
		#print(lclMap.compute(7))
		self.assertEqual(lclMap.compute(7), 14)