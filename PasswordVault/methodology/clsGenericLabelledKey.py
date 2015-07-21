'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''

from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsDLPHash import DLPHash
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
import copy

class GenericLabelledKey(object):
	'''
	classdocs
	'''
	def __init__(self, pKeyName, pPasswordIdentifierList, pResultIdentifier, pKey):
		'''
		Constructor
		'''
		self.keyName = str(pKeyName)
		self.passwordIdentifierList = pPasswordIdentifierList
		self.resultIdentifier = pResultIdentifier
		self.key = pKey
	
	def name(self):
		return self.keyName
	
	def passwordIdentifierList(self):
		return self.passwordIdentifierList
	
	def resultIdentifier(self):
		return self.resultIdentifier
	
	def key(self):
		return self.key
	
	def inputIsSufficient(self, pPasswordList):
		# Returns false if insufficient data was provided and true otherwise
		lclPasswordIds = pPasswordList.getIdentifierList()
# 		print("List comparision:")
# 		print(str(lclPasswordIds), " versus ", str(self.passwordIdentifierList))
		for i in self.passwordIdentifierList:
			flag = False
			for j in lclPasswordIds:
				if i == j:
					flag = True
			if flag == False:
				return False
		return True
	
	def compute(self, pPasswordList):
		lclPasswordList = pPasswordList.getCopy()
		lclPasswordIds = lclPasswordList.getIdentifierList()
		
		if not self.inputIsSufficient(lclPasswordList):
			#print("Insufficient input.")
			return -1
		
		for i in lclPasswordIds:
			if i not in self.passwordIdentifierList:
				lclPasswordList.popByIdentifier(i)
		
		assert(str(lclPasswordList.getIdentifierList()) == str(self.passwordIdentifierList))
		
# 		lclIdList = []
# 		for i in pPasswordList.getList():
# 			lclIdList.append(i.identifier())
# 		
# 		# lclIdList is now a list of identifiers that match the pPasswordList
# 		for i in self.passwordIdentifierList:
# 			if not i in lclIdList:
# 				print("Not enough passwords.")
# 				return -1
# 		# We have validated at this point that the passwords in pPasswordList are enough for our computation.
# 		
# 		# We now trim the list.
# 		lclPasswordList = pPasswordList.getCopy()
# 		for i in lclPasswordList.getList():
# 			if not i.identifier() in self.passwordIdentifierList:
# 				lclPasswordList.popByIdentifier(i)
# 		# The list should contain exactly the same items mentioned in self.passwordIdentifierList.
# 		if str(lclPasswordList.getIdentifierList()) != str(self.passwordIdentifierList):
# 			print("GenericLabelledKey compute error")
# 			print(str(lclPasswordList.getIdentifierList()))
# 			print(str(self.passwordIdentifierList))
# 			print(self.key.compute(lclPasswordList))
# 		assert(str(lclPasswordList.getIdentifierList()) == str(self.passwordIdentifierList))
# 		#print(lclPasswordList.toString())
		
		lclReturnPassword = self.key.compute(lclPasswordList)
		return lclReturnPassword
	
	def computeReturnTuple(self, pPasswordList):
		return PasswordTuple(self.resultIdentifier, self.compute(pPasswordList))
	
	def toString(self):
		# print (self.passwordIdentifierList)
		return "(" + self.keyName + "," + str(self.passwordIdentifierList) + "," + self.resultIdentifier + "," + self.key.toString() + ")"