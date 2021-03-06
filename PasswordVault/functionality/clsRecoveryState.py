'''
Created on Jul 22, 2015

@author: Daniel Bruce
'''
from functionality.clsPivotedVault import PivotedVault
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsSimpleVault import SimpleVault
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsPasswordList import PasswordList

class RecoveryState(object):
	'''
	classdocs
	'''

	def __init__(self, pPasswordList = PasswordList([]), pPivotedVault = PivotedVault([])):
		'''
		Constructor
		'''
		self.passwordList = pPasswordList
		self.pivotedVault = pPivotedVault
		
	def addInputList(self, pInputList):
		#super(ControlledIntermediateVault, self).methodName(arguments)
		#super(ControlledIntermediateVault, self)
		return self.addInputList(pInputList)
	
	def popInputListByName(self):
		
		
	def addOutput(self, pPasswordTuple):
		return self.pivotedVault.addOutput(pPasswordTuple)
	
	def popPasswordByIdentifier(self, pIdentifier):
		return self.passwordList.popByIdentifier(pIdentifier)
		
	def popPassword(self, pPasswordTuple):
		return self.passwordList.pop(pPasswordTuple)
	
	def getPasswordList(self):
		return self.passwordList
	
	def getVault(self):
		return self.pivotedVault