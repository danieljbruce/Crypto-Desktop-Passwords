'''
Created on Jul 22, 2015
@author: Daniel Bruce 
'''
import unittest
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from functionality.clsPivotedVault import PivotedVault

class TestPivotedVault(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running the FullFunctionality test for the TestPivotedVault.")
		self.define()
		print("Variables defined.")
		vault = PivotedVault()
		print("1:" + vault.toString())
		vault.addOutput(self.lclpwd6)
		print("2:" + vault.toString())
		vault.addOutput(self.lclpwd5)
		print("3:" + vault.toString())
		vault.addInputList(self.passwordListA1)
		print("4:" + vault.toString())
		vault.addInputList(self.passwordListA2)
		print("5:" + vault.toString())
		vault.addInputList(self.passwordListA3)
		print("6:" + vault.toString())
		vault.addInputList(self.passwordListA4)
		print("7:" + vault.toString())
		vault.removeOutput(self.lclpwd5)
		print("8:" + vault.toString())
		vault.removeOutput(self.lclpwd2)
		print("9:" + vault.toString())
		vault.removeInputList(self.passwordListA1)
		print("10:" + vault.toString())
	
	def define(self):
		self.lclpwd1 = PasswordTuple("Facebook", "q234")
		self.lclpwd2 = PasswordTuple("Google", "778")
		self.lclpwd3 = PasswordTuple("LinkedIn", "P324")
		self.lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
		self.lclpwd5 = PasswordTuple("Foursquare", "hjkhksssssg34")
		self.lclpwd6 = PasswordTuple("Dutch Oven", "hjkhsddkg34")
		
		self.passwordListA0 = PasswordList([])
		
		self.passwordListA1 = PasswordList([])
		self.passwordListA1.append(self.lclpwd1)
		
		self.passwordListA2 = PasswordList([])
		self.passwordListA2.append(self.lclpwd1)
		self.passwordListA2.append(self.lclpwd2)
		
		self.passwordListA3 = PasswordList([])
		self.passwordListA3.append(self.lclpwd1)
		self.passwordListA3.append(self.lclpwd2)
		self.passwordListA3.append(self.lclpwd3)
		
		self.passwordListA4 = PasswordList([])
		self.passwordListA4.append(self.lclpwd1)
		self.passwordListA4.append(self.lclpwd2)
		self.passwordListA4.append(self.lclpwd3)
		self.passwordListA4.append(self.lclpwd4)	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()