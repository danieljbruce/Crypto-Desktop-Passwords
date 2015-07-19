'''
Created on Jul 18, 2015

@author: Daniel Bruce
'''
import copy
from methodology.clsPasswordList import PasswordList
from methodology.clsPasswordTuple import PasswordTuple

class BasicLabelledKey(object):
	# This class's data is a 4-tuple (identifier list, result identifier, methodology, method key)
	'''
	classdocs
	'''

	def __init__(self, pPasswordIdentifierList, pResultIdentifier, pMethod, pKey):
		'''
		Constructor
		'''
		self.passwordIdentifierList = pPasswordIdentifierList
		self.resultIdentifier = pResultIdentifier
		self.method = pMethod
		self.key = pKey
	
	def passwordIdentifierList(self):
		return self.passwordList
	
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
				lclPasswordList.popByIdentifier(i)
		# The list should contain exactly the same items mentioned in self.passwordIdentifierList.
		return self.key.compute(lclPasswordList)
	
	def computeReturnTuple(self, pPasswordList):
		return PasswordTuple(self.resultIdentifier, self.compute(pPasswordList))
	
	def encode(self):
		return (self.passwordIdentifierList, self.resultIdentifier, self.method, self.key.encode())