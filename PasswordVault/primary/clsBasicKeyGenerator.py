'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''


class clsBasicKeyGenerator(iKeyGenerator):
	'''
	classdocs
	'''

	def __init__(self, pJoiner, pGenerator, pHasher, pCombiner, pFirstDifferenceMethod, pLastDifferenceMethod):
		'''
		Constructor
		'''
		self.generator = pGenerator
		self.joiner = pJoiner
		self.hasher = pHasher
		self.combiner = pCombiner
		self.firstDifferenceMethod = pFirstDifferenceMethod
		self.lastDifferenceMethod = pLastDifferenceMethod
	
	def generateKey(self, pPasswordList, pResult):
		# Generate a large BigInt
		
		# Process 1:
		# Calculate the hash of the bigInt
		
		
		# Calculate the difference between the hash result and pResult to be stored
		
		
		# Process 2:
		# Combine the pPassword list into a BigInt using the joiner and combiner specified
		
		
		# Calculate the difference between the the combined output and the generated bigInt
		
		
		# Return the key which includes the 
		
		
		return ""
	
	def useKey(self, pPasswordList):
		return ("", "")