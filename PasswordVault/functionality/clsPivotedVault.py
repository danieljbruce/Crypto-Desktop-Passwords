'''
Created on Jul 22, 2015
@author: Daniel Bruce
'''

from functionality.clsIntermediateVault import IntermediateVault
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsSimpleVault import SimpleVault
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator
from methodology.clsSwappingVault import SwappingVault
import pickle

class PivotedVault(object):
	'''
	classdocs
	'''
	
	#The reserved key "3161379751047332383565"
	
	def __init__(self, pVault = SimpleVault(), pIntermediate = BasicBigIntGenerator().generate(), pGenerator = SimpleLabelledKeyGenerator()):
		'''
		Constructor
		'''
		self.pivot = str(pIntermediate)
		self.vault = pVault
		self.keygen = pGenerator
	
	def getVault(self):
		return self.vault

	def getVaultForSaving(self):
		return self.vault.getVaultForSaving()

	def addInputList(self, pInputList):
		#super(ControlledIntermediateVault, self).methodName(arguments)
		#super(ControlledIntermediateVault, self)
		
		#Check for duplicates? Or allow them?
		lclKey = self.keygen.generate(pInputList, ("Intermediate Constant: 3161379751047332383565", self.pivot))
		self.vault.append(lclKey)
		return
	
	def removeInputList(self, pInputList):
		lclList = self.vault.getList()
		for i in lclList:
			pIL = i.passwordIdentifierList() 
			if pIL == pInputList:
				print("Removing input list ", pInputList.toString())
				self.vault.removeByInputList(pInputList)
				return 0
		print("Cannot pop input list.")
		return -1
	
	def addInputListAndPasswords(self, pInputList):
		self.addInputList(pInputList)
		for i in pInputList:
			self.addOutput(i)
		return	
		
	def addOutput(self, pPasswordTuple):
		lclPwdList = {}
		lclPwdList["Intermediate Constant: 3161379751047332383565"] = self.pivot
		lclKey = self.keygen.generate(lclPwdList, pPasswordTuple)
		return self.vault.append(lclKey)
	
	def removeOutput(self, pPasswordTuple):
		lclList = self.vault.getList()
		for i in lclList:
			resId = i.resultIdentifier()
			if resId == pPasswordTuple[0]:
				print("Removing output: ", str(resId))
				self.vault.removeByResultIdentifier(resId)
				return 0
		print("Cannot remove output.")
		return -1
	
	def toString(self):
		returnString = "Pivot: " + str(self.pivot) + "\n"
		returnString += self.vault.toString()
		return returnString
	
	def createPickledVault(self):
		return self.vault.createPickledVault()