'''
Created on Jul 15, 2015

@author: Owner
'''
from methodology.iHashMethodology import iHashMethodology

class SaltedHash(iHashMethodology):
    '''
    classdocs
    '''
    def __init__(self, pSalt):
        '''
        Constructor
        '''
        self.m_salt = pSalt
    
    def compute(self, pArgument):
        return self.m_salt + pArgument