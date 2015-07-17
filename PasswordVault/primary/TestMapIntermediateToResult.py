'''
Created on Jul 16, 2015

@author: Owner
'''
import unittest
from primary.clsBasicHash import BasicHash
from primary.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from primary.clsBasicStringIntConverter import BasicStringIntCoverter

class TestMapIntermediateToResult(unittest.TestCase):


	def test_FullFunctionality(self):
		print("Running test FullFunctionality on TestMapIntermediateToResult.")
		
		lclHash = BasicHash(BasicStringIntCoverter())
		lclMap = BasicMapIntermediateToResult(lclHash, 7, 14)
		#print(lclMap.compute(7))
		self.assertEqual(lclMap.compute(7), 14)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_F']
	unittest.main()