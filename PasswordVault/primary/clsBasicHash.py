'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

from Crypto.Hash import SHA512
from primary.iHashMethodology import iHashMethodology

class BasicHash(iHashMethodology):
	'''
	classdocs
	'''
	def __init__(self, pStringIntConverter):
		'''
		Constructor
		'''
		self.stringIntConverter = pStringIntConverter
		
	def compute(self, pArgument):
		lclTempString = self.stringIntConverter.toString(pArgument)
		lclTempString = SHA512.new(lclTempString.encode('utf-8')).hexdigest()
		return self.stringIntConverter.toInt(lclTempString)
		#lclHashFunction = SHA512.new()
		#lclString = str(pArgument)
		#lclHashValue = lclHashFunction.update(lclString)
		#lclHashDigest = lclHashValue.hexDigest()
		#lclHash = int(lclHashDigest)
		#return lclHash