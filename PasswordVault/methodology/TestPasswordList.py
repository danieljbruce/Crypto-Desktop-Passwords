'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList


class TestPasswordList(unittest.TestCase):

	def test_FullFunctionality(self):
		print("Running test Full Functionality in TestPasswordList")
		pwd1 = PasswordTuple("Facebook", "224")
		pwd2 = PasswordTuple("Google", "onion32")
		plist = PasswordList([])
		plist.append(pwd1)
		plist.append(pwd2)
		self.assertEqual(plist.size(), 2)
		#self.assertEqual(plist.popByIdentifier("Google").password(), "onion32")
		#self.assertEqual(plist.popByIdentifier("Facebook").password(), "224")
		
	def test_getCopy(self):
		print("Running test_getCopy in TestPasswordList")
		pwd1 = PasswordTuple("Facebook", "224")
		pwd2 = PasswordTuple("Google", "onion32")
		pwd3 = PasswordTuple("LinkedIn", "ddonion32")
		pwd4 = PasswordTuple("Quora", "onion32324")
		
		print(pwd1.toString())
		print(pwd2.toString())
		
		qlist = PasswordList([])
		print(qlist.toString())
		qlist.append(pwd1)
		print(qlist.toString())
		qlist.append(pwd2)
		print(qlist.toString())
		print(qlist.getCopy().toString())
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_FullFunctionality']
	unittest.main()