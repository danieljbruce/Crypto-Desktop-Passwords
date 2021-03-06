'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsBasicRecovery import BasicRecovery
from methodology.clsGenericRecovery import GenericRecovery
from methodology.clsGenericLabelledKey import GenericLabelledKey
import pickle

class SimpleVault(object):
	'''
	classdocs
	'''
	def __init__(self, pList = None, pRecoveryMethod = None):
		'''
		Constructor
		'''
		if pList is None:
			pList = []
		if pRecoveryMethod is None:
			pRecoveryMethod = GenericRecovery()
		
		self.recoveryMethod = pRecoveryMethod
		self.list = pList
	
	def getVaultForSaving(self):
		return self
		
	def append(self, pItem):
		if not isinstance(pItem, GenericLabelledKey):
			raise TypeError("Argument passed into append function is not a SimpleLabelledKey.")
		self.removeByInputListIdentifiersAndResultIdentifier(pItem.passwordIdentifierList(), pItem.resultIdentifier())
		# Do this is the vault has no matching mapping signature.
		self.list.append(pItem)
		return
		
	def getList(self):
		return self.list
	
	def removeByName(self, pKeyName):
		for i in self.list:
			if i.name() == pKeyName:
				print("Removing key: ", str(i))
				self.list.remove(i)
		return
	
	def removeByInputList(self, pInputList):
		lclIdentifiers = set(pInputList.keys())#pInputList.getIdentifierList()
		for i in self.list:
			if set(i.passwordIdentifierList()) == lclIdentifiers:
				print("Removing key: ", str(i))
				self.list.remove(i)
		return
	
	def removeByResultIdentifier(self, pResultIdentifier):
		#pResultIdentifier should be a string. 
		for i in self.list:
			if i.resultIdentifier() == pResultIdentifier:
				print("Removing key: ", str(i))
				self.list.remove(i)
		return
	
	def removeByInputListIdentifiersAndResultIdentifier(self, pInputListIdentifiers, pResultIdentifier):
		lclIdentifiers = pInputListIdentifiers
		for i in self.list:
			if set(i.passwordIdentifierList()) == set(lclIdentifiers) and pResultIdentifier == i.resultIdentifier():
				print("Removing key: ", str(i))
				self.list.remove(i)
		return		
	
# 	def passwordIdentifierList(self):
# 		return self.__passwordIdentifierList
# 	
# 	def resultIdentifier(self):
# 		return self.__resultIdentifier	
	def remove(self, pItem):
		return self.list.remove(pItem)
			
	def recover(self, pInputPasswordList):
		return self.recoveryMethod.recover(self, pInputPasswordList)

	def createPickledVault(self):
		return pickle.dump(self.list)
	
	def toString(self):
		returnString = ""
		for i in self.list:
			returnString += i.toString() + "\n"
		return returnString