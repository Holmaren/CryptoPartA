#!/usr/bin/python

import part1_crypto as p1
import sys



if len(sys.argv)<2:
	print "Not enough arguments"
	exit(1)

whichFunc=sys.argv[1]

if whichFunc=="Epow":
	if len(sys.argv)<5:
		print "Not enough arguments"
		exit(1)
	base=int(sys.argv[2])
	exp=int(sys.argv[3])
	mod=int(sys.argv[4])

	ans=p1.modexp(base,exp,mod)

	print "Func ans:" + str(ans)
	print "Pow ans:" + str((base**exp)%mod)


if whichFunc=="DH":
	priv=p1.diffie_hellman_private(10)
	print "Priv: " + str(priv)
	print p1.diffie_hellman_pair(5,15,priv)
	print p1.diffie_hellman_shared(priv,67,15)



