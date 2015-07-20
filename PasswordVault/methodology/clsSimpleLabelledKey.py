'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsDLPHash import DLPHash
from methodology.clsPasswordTuple import PasswordTuple
import copy

class SimpleLabelledKey(object):
	'''
	classdocs
	'''
	def __init__(self, pKeyName, pPasswordIdentifierList, pResultIdentifier, pMethod, pKey, pValidationCode):
		'''
		Constructor
		'''
		self.keyName = str(pKeyName)
		self.passwordIdentifierList = pPasswordIdentifierList
		self.resultIdentifier = pResultIdentifier
		self.method = pMethod
		self.key = pKey
		self.validationCode = pValidationCode
	
	def name(self):
		return self.keyName
	
	def passwordIdentifierList(self):
		return self.passwordIdentifierList
	
	def resultIdentifier(self):
		return self.resultIdentifier
	
	def method(self):
		return self.method
	
	def key(self):
		return self.key
	
	def compute(self, pPasswordList):
		# Returns -1 if insufficient data was provided.
		lclIdList = []
		for i in pPasswordList.list:
			lclIdList.append(i.identifier())
		# lclIdList is now a list of identifiers that match the pPasswordList
		for i in self.passwordIdentifierList:
			if not i in lclIdList:
				return -1
		# We have validated at this point that the passwords in pPasswordList are enough for our computation.
		
		# We now trim the list.
		lclPasswordList = copy.copy(pPasswordList)
		for i in lclPasswordList.list:
			if not i.identifier() in self.passwordIdentifierList:
				lclPasswordList.getByIdentifier(i)
		# The list should contain exactly the same items mentioned in self.passwordIdentifierList.
		print(lclPasswordList.toString())
		
		return self.key.compute(lclPasswordList)
	
	def computeReturnTuple(self, pPasswordList):
		return PasswordTuple(self.resultIdentifier, self.compute(pPasswordList))
	
	def toString(self):
		# print (self.passwordIdentifierList)
		return "(" + self.keyName + "," + str(self.passwordIdentifierList) + "," + self.resultIdentifier + "," + self.method + "," + self.key.toString() + ")"