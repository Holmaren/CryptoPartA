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
    result = 0 
    return result
