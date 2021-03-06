'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsBasicRecovery import BasicRecovery
from methodology.clsGenericRecovery import GenericRecovery
from methodology.clsGenericLabelledKey import GenericLabelledKey

#Obselete Class

class GenericVault(object):
	'''
	classdocs
	'''
	def __init__(self, pList = [], pRecoveryMethod = GenericRecovery()):
		'''
		Constructor
		'''
		self.recoveryMethod = pRecoveryMethod
		self.list = []
		
	def append(self, pItem):
		if not isinstance(pItem, GenericLabelledKey):
			raise TypeError("Argument passed into append function is not a SimpleLabelledKey.")
		self.list.append(pItem)
		
	def getList(self):
		return self.list
	
	def popByName(self, pKeyName):
		for i in self.list:
			if i.name() == pKeyName:
				return self.list.pop(i)
	
	def pop(self):
		return self.list.pop()
			
	def recover(self, pInputPasswordList):
		return self.recoveryMethod.recover(self, pInputPasswordList)
	
	def toString(self):
		returnString = ""
		for i in self.list:
			returnString += i.toString() + "\n"
		return returnString