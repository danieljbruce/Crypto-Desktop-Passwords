'''
Created on Jul 20, 2015

@author: Daniel Bruce
'''
import copy

class GenericRecovery(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
	def recover(self, pVault, pInputList):
		lclResultList = pInputList.getCopy()
		flag = False
# 		print("Vault contents:")
# 		print(pVault.toString())
		while not flag:
			flag = True
# 			print("The password list is " + lclResultList.toString())
			#testVar = input("Ask user for something outer loop.")
			for key in pVault.getList():
				lclResult = key.computeReturnTuple(lclResultList)
				lclIdList = lclResultList.getIdentifierList()
# 				print("Key case:")
# 				print(key.toString())
				#print(lclResultList.toString(), lclIdList, lclResult.toString())
				condition1 = lclResult.password() != -1
				condition2 = not lclResult.identifier() in lclIdList
# 				print(lclResultList.toString(), lclIdList, lclResult.toString(), condition1, condition2)
				#testVar = input("Ask user for something.")
				if condition1 and condition2:
					flag = False
					lclResultList.append(lclResult)
					#print(lclResultList.toString())
					break
			print()
# 		print("finish")			
		return lclResultList		