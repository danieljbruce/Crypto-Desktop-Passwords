'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator

class TestGenericLabelledKey(unittest.TestCase):

	def testSimpleFunctionality(self):
		print("Running test_FullFunctionality test on test_SimpleKeyGenerator.")
		lclPasswordList1 = PasswordList([])

		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "l345t")
		lclpwd4 = PasswordTuple("Quora", "l3sdfdf45t")
		
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
				
		#self.tryCombo(lclPasswordList1, PasswordTuple("LinkedIn", "Stormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("Dutch Oven", "Stsssormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("", "Sdsdsdtormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("", "Sdsdsdtormy"))
		
		self.basicGenerate(lclPasswordList1, lclpwd3)
		self.basicGenerate(lclPasswordList1, lclpwd4)
		
	def basicGenerate(self, pInputList, pResult):
		lclGen = SimpleLabelledKeyGenerator()
		lclKey = lclGen.generate(pInputList, pResult)
		print(lclKey.toString())
		self.assertEqual(pResult.password(), lclKey.compute(pInputList))
		
	def test_sampleRecoveryWalkthrough(self):
		print("Running test_sampleRecoveryWalkthrough for TestGenericLabelledKey.")
		
		lclGen = SimpleLabelledKeyGenerator()

		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "l345t")
		lclpwd4 = PasswordTuple("Quora", "l3sdfdf45t")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
		
		lclPasswordList2 = lclPasswordList1.getCopy()
		lclPasswordList2.append(lclpwd3)
		
		lclKey2 = lclGen.generate(lclPasswordList2, lclpwd4)
		lclKey1 = lclGen.generate(lclPasswordList1, lclpwd3)
		
		lclResultList = lclPasswordList1.getCopy()
		lclResultList.append(lclKey1.computeReturnTuple(lclResultList)) 
		print(lclResultList.toString())
		
		lclResultList.append(lclKey2.computeReturnTuple(lclResultList))
		print(lclResultList.toString())
		
		lclResultList.append(lclKey2.computeReturnTuple(lclResultList))
		print(lclResultList.toString())
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()