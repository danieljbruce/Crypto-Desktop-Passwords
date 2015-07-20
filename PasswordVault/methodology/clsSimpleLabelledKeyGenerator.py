'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleKey import SimpleKey
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsSimpleLabelledKey import SimpleLabelledKey
from methodology.clsGenericLabelledKey import GenericLabelledKey
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

class SimpleLabelledKeyGenerator(object):
	'''
	classdocs
	'''

	def __init__(self, pKeyGen = SimpleKeyGenerator()):
		'''
		Constructor
		'''
		self.keyGen = pKeyGen
	
	def generate(self, pPasswordList, pResult, pName = BasicBigIntGenerator(64).generate()):
		lclKey = self.keyGen.generate(pPasswordList, pResult.password())
		return GenericLabelledKey(str(pName), pPasswordList.getIdentifierList(), pResult.identifier(), lclKey)
		