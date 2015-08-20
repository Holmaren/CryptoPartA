# COMP90043 Cryptography and Security 
# Cryptography Skeleton Function for Project 
# 
# Candidates will have to implement the following skeleton functions.
# Candidates may create additional skeleton functions by importing the skeleton functions from a seperate file. 
# Do not alter the function declarations in this file, or add additional helper functions in this file.

import random

# TO DO. 
def diffie_hellman_private(numbits):
    """
        diffie_hellman_private

        Returns a private secret integer with `numbits`. 
    """
    private = 0
    return private

# TODO
def diffie_hellman_pair(generator, modulus, private):
    """
        diffie_hellman_pair

        Given a generator, prime modulus and a private integer, produce the public integer. Return a tuple of (Private Integer, Public Integer)
    """
    public = 0
    return (private, public)

# TODO 
def diffie_hellman_shared(private, public, modulus):
    """
        diffie_hellman_shared

        Given a private integer, public integer and prime modulus. Compute the shared key for the communication channel, then return it.
    """
    shared_key = 0
    return shared_key

# TODO
def modexp(base, exponent, modulo):
    """
        modexp

        Given a base, exponent and modulo. Compute the modular exponentiation.
    """
    result = 1

    #First I'm getting the binary representation of the exponent
    binRep=bin(exponent)[2:]
    #Iterating from MSB to LSB
    for i in xrange(len(binRep)):
        curBit=int(binRep[i])
        '''In every step except for MSB we square the result modulo n. But in the first step 			result==1 and the first step is MSB, which is why we don't have to handle this'''
        result=(result*result)%modulo
        #if the current bit is one we also multiply with the base
        if curBit==1:
            result=(result*base)%modulo
        

    return result





