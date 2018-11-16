#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

fichiervcf=sys.argv[1]
with open(fichiervcf,"r") as fichiervcf2:
#tesver=fichiervcf2.readline()
#print(tesver)

	for ligne in fichiervcf2:
		info=re.search("(^\d*|^X|^Y)\s(\d*)\s(.*)\s([ACGT]*)\s([ACGT]*)\s(\d*|.)\s(\S*)\s",ligne)
	

#recuperation du chromosome("(^\d*|^X|^Y)\s")
		if info :
			chromosome=info.group(1)
			print(chromosome) #not ok

#recuperation de la position("\s(\d*)\s")
	#if info :
			position=info.group(2)
			print(position)

#recuperation Id("\s(.*)\s")
	#if info :
			identifiant=info.group(3)
			print(identifiant)

#recuperation de la base de reference ("\s([ACGT]*)\s")
	#if info :
			ref=info.group(4)
			print(ref)

#recuperation de la variation ("\s([ACGT]*)\s")
	#if info:
			alt=info.group(5)
			print(alt)

#recuperation de la qualité ("\s(\d*|.)\s")
	#if info :
			qualite=info.group(6)
			print(qualite)

#recuperation du filtre ("\s(\S*)\s")
	#if info :
			filtre=info.group(7)
			print(filtre)

print("test final")
    