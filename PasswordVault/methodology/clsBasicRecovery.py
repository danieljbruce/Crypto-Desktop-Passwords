'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import copy

class BasicRecovery(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
	
	def recover(self, pVault, pInputList):
		lclResultList = copy.copy(pInputList)
		flag = False
		while not flag:
			flag = True
			print("Rubenstein"+lclResultList.toString())
			#testVar = input("Ask user for something outer loop.")
			for key in pVault.getList():
				lclResult = key.computeReturnTuple(pInputList)
				lclIdList = lclResultList.getIdentifierList()
				#print(lclResultList.toString(), lclIdList, lclResult.toString())
				condition1 = lclResult.password() != -1
				condition2 = not lclResult.identifier() in lclIdList
				#print(lclResultList.toString(), lclIdList, condition1, condition2)
				#testVar = input("Ask user for something.")
				if condition1 and condition2:
					flag = False
					lclResultList.append(lclResult)
					#print(lclResultList.toString())
					break
		print("finish")			
		return lclResultList