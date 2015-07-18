'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class BasicDifferenceMapper(object):
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
	
	def defineMap(self, pSource, pTarget):
		self.difference = pTarget - pSource
		
	def compute(self, pSource):
		return pSource + self.difference
	
	def toEncoding(self):
		return self.difference