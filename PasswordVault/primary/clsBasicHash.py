'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
import hashlib
from primary.iHashMethodology import iHashMethodology

class BasicHash(iHashMethodology):
	'''
	classdocs
	'''
	def __init__(self, params):
		'''
		Constructor
		'''
	
	def compute(self, pArgument):
		return hashlib.md5(pArgument)