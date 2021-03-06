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
		self.__keyName = str(pKeyName)
		self.__passwordIdentifierList = pPasswordIdentifierList
		self.__resultIdentifier = pResultIdentifier
		self.__key = pKey
	
	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__	
	
	def name(self):
		return self.__keyName
	
	def passwordIdentifierList(self):
		return self.__passwordIdentifierList
	
	def resultIdentifier(self):
		return self.__resultIdentifier
	
	def key(self):
		return self.__key
	
	def inputIsSufficient(self, pPasswordList):
		# Returns false if insufficient data was provided and true otherwise
		lclPasswordIds = list(pPasswordList.keys()) #pPasswordList.getIdentifierList()
# 		print("List comparision:")
# 		print(str(lclPasswordIds), " versus ", str(self.__passwordIdentifierList))
		for i in self.__passwordIdentifierList:
			flag = False
			for j in lclPasswordIds:
				if i == j:
					flag = True
			if flag == False:
				return False
		return True
	
	def compute(self, pPasswordList):
		lclPasswordList = {}
		
		#print(self.__passwordIdentifierList)
		#print(set(pPasswordList.keys()))
		for i in set(self.__passwordIdentifierList).intersection(set(pPasswordList.keys())):
			lclPasswordList[i] = pPasswordList[i]
		
		if len(lclPasswordList) < len(self.__passwordIdentifierList):
			#print("Insufficient input.")
			return -1
		
		assert(len(lclPasswordList) == len(self.__passwordIdentifierList))
		
		lclReturnPassword = self.__key.compute(lclPasswordList)
		return lclReturnPassword
		
		# if set(list(pPasswordList.keys())).intersection(b2)
# 		self.__passwordIdentifierList
# 		
# 		lclPasswordIds = lclPasswordList.getIdentifierList()
# 		
# 		if not self.inputIsSufficient(lclPasswordList):
# 			#print("Insufficient input.")
# 			return -1
# 		
# 		for i in lclPasswordIds:
# 			if i not in self.__passwordIdentifierList:
# 				lclPasswordList.popByIdentifier(i)
# 		
# 		assert(str(lclPasswordList.getIdentifierList()) == str(self.__passwordIdentifierList))
		
		
# 		lclIdList = []
# 		for i in pPasswordList.getList():
# 			lclIdList.append(i.identifier())
# 		
# 		# lclIdList is now a list of identifiers that match the pPasswordList
# 		for i in self.__passwordIdentifierList:
# 			if not i in lclIdList:
# 				print("Not enough passwords.")
# 				return -1
# 		# We have validated at this point that the passwords in pPasswordList are enough for our computation.
# 		
# 		# We now trim the list.
# 		lclPasswordList = pPasswordList.getCopy()
# 		for i in lclPasswordList.getList():
# 			if not i.identifier() in self.__passwordIdentifierList:
# 				lclPasswordList.popByIdentifier(i)
# 		# The list should contain exactly the same items mentioned in self.__passwordIdentifierList.
# 		if str(lclPasswordList.getIdentifierList()) != str(self.__passwordIdentifierList):
# 			print("GenericLabelledKey compute error")
# 			print(str(lclPasswordList.getIdentifierList()))
# 			print(str(self.__passwordIdentifierList))
# 			print(self.__key.compute(lclPasswordList))
# 		assert(str(lclPasswordList.getIdentifierList()) == str(self.__passwordIdentifierList))
# 		#print(lclPasswordList.toString())

	
	def computeReturnTuple(self, pPasswordList):
		lclComputed = self.compute(pPasswordList)
		if lclComputed == -1:
			return -1
		return (self.__resultIdentifier, lclComputed)
	
	def toString(self):
		# print (self.__passwordIdentifierList)
		return "(" + self.__keyName + "," + str(self.__passwordIdentifierList) + "," + str(self.__resultIdentifier) + "," + self.__key.toString() + ")"