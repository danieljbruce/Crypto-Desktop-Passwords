'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import copy

class BasicRecovery(object):
	'''
	classdocs
	'''
	def __init__(self, params):
		'''
		Constructor
		'''
	
	def recoverList(self, pVault, pInputList):
		lclResultList = copy.copy(pInputList)
		flag = False
		while not flag:
			flag = True
			for key in pVault.list:
				lclResult = key.computeReturnTuple(pInputList)
				if lclResult.identifier() not in lclResultList and lclResult.password() != -1:
					flag = False
					lclResultList.append(lclResult)