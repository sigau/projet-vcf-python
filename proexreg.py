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
	dicovar={}
	liste=[]
	substitution=0
	insertion=0
	deletion=0
	variation=0
	typevariant=""

	for ligne in fichiervcf2:
		info=re.search("(^\d*|^X|^Y)\s(\d*)\s(.*)\s([ACGT]*)\s([ACGT]*)\s(\d*|.)\s(\S*)\s",ligne)
	

#recuperation du chromosome("(^\d*|^X|^Y)\s")
		if info :
			chromosome="chromosome "+info.group(1)
			#print(chromosome) #ok

#recuperation de la position("\s(\d*)\s")
	#if info :
			position=info.group(2)
			#print(position)

#recuperation Id("\s(.*)\s")
	#if info :
			identifiant=info.group(3)
			#print(identifiant)

#recuperation de la base de reference ("\s([ACGT]*)\s")
	#if info :
			ref=info.group(4)
			#print(ref)

#recuperation de la variation ("\s([ACGT]*)\s")
	#if info:
			alt=info.group(5)
			#print(alt)

#recuperation de la qualité ("\s(\d*|.)\s")
	#if info :
			qualite=info.group(6)
			#print(qualite)
			
#recuperation du filtre ("\s(\S*)\s")
	#if info :
			filtre=info.group(7)
			#print(filtre)


#compte des variation 
	#compte des deletions
			if ((len(ref)>len(alt))or( alt=="-")):
				deletion+=1
				variation+=1
				#print("test deletion")
				#print("test variation")
				typevariant="deletion"
	    #compte des insertion
			if(len(ref)<len(alt)):
				insertion+=1
				variation+=1
				#print("test insertion")
				#print("test variation")
				typevariant="insertion"

	    #compte des substituion
			if (len(ref)==len(alt)):
				substitution+=1
				variation+=1
				#print("test substitution")
				#print("test variation")
				typevariant="substitution"



								#####dico doit ressembler à ###########
#deux dico
#print dicopos :
			#chromosome  
							#position sk
											#liste de string (typevariant,ref,alt)
#print dicovar :
			#chromosome  
							#type variant
											#nb du type de variation

																	#ou
#print dico :
			  #chromosome 	
			  				# typevariant 
			  								#nbtypevariant  
			  												#liste de string (position ref alt)
			  												#dicovar[chromosome].getvalues(typevariant)+1
								########fin############
			liste=[position,ref,alt]
			if chromosome in dicovar.keys():
				if typevariant in dicovar[chromosome].keys():
					dicovar[chromosome][typevariant].append(liste)
				else:
					dicovar[chromosome][typevariant]=typevariant
					dicovar[chromosome][typevariant]=liste
			else:
				dicovar[chromosome]={}
				dicovar[chromosome][typevariant]=typevariant
				dicovar[chromosome][typevariant]=liste

			#if chromosome in dicovar.keys():
			#	dicovar[chromosome]["position"].append(position)
			#	dicovar[chromosome]["ref"].append(ref)
			#	dicovar[chromosome]["alt"].append(alt)
			#else :
			#	dicovar[chromosome]={"position":[position], "ref":[ref], "alt":[alt]}

pprint(dicovar)
#print("test final")
print("nb variation= "+ str(variation)+"\n"+"nb substitution= "+str(substitution)+"\n"+"nb insertion="+str(insertion)+"\n"+"nb deletions= "+str(deletion))

# % de chaque type de variation
pins=(insertion/variation)*100
pdel=(deletion/variation)*100
psub=(substitution/variation)*100
print("% substitution= "+str(psub)+"%"+"\n"+"% insertion="+str(pins)+"%"+"\n"+"% deletions= "+str(pdel)+"%")
