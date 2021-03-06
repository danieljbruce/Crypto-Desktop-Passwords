'''
Created on Jul 17, 2015

@author: Owner
'''



from Crypto.Hash import SHA512

class TestHasher(object):
	def toString(self, pBigInt):
		assert(pBigInt >= 0)
		lclStringList = []
		while pBigInt != 0:
			#print(pBigInt)
			lclStringList.append(chr(pBigInt % 128))
			pBigInt -= pBigInt % 128
			assert(int(pBigInt) == pBigInt)
			pBigInt = int(pBigInt / 128)
		assert(pBigInt == 0)
		return ''.join(lclStringList)
		
	def toInt(self, pString):
		total = 0
		lclStringList = list(pString)
		for index, value in enumerate(lclStringList):
			#print((128**index), ord(value))
			total += ((128 ** (index)) * ord(value))
		return total	
		
	def compute(self, pArgument):
		lclTempString = self.toString(pArgument)
		lclTempString = SHA512.new(lclTempString.encode('utf-8')).hexdigest()
		return self.toInt(lclTempString)
	
if __name__ == '__main__':
	lclHasher = TestHasher()
	print(lclHasher.compute(7))