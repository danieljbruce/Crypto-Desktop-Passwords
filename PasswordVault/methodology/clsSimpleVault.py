'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsBasicRecovery import BasicRecovery
from methodology.clsGenericRecovery import GenericRecovery
from methodology.clsGenericLabelledKey import GenericLabelledKey

class SimpleVault(object):
	'''
	classdocs
	'''
	def __init__(self, pList = None, pRecoveryMethod = GenericRecovery()):
		'''
		Constructor
		'''
		if pList is None:
			pList = []
		
		self.recoveryMethod = pRecoveryMethod
		self.list = pList
		
	def append(self, pItem):
		if not isinstance(pItem, GenericLabelledKey):
			raise TypeError("Argument passed into append function is not a SimpleLabelledKey.")
		self.list.append(pItem)
		return
		
	def getList(self):
		return self.list
	
	def removeByName(self, pKeyName):
		for i in self.list:
			if i.name() == pKeyName:
				self.list.remove(i)
		return
	
	def removeByInputList(self, pInputList):
		lclIdentifiers = pInputList.getIdentifierList()
		for i in self.list:
			if set(i.passwordIdentifierList()) == set(lclIdentifiers):
				print(i.toString(), str(pInputList.toString()))
				self.list.remove(i)
		return
	
	def removeByResult(self, pResult):
		for i in self.list:
			if i.resultIdentifier() == pResult:
				print(str(i))
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
	
	def toString(self):
		returnString = ""
		for i in self.list:
			returnString += i.toString() + "\n"
		return returnString