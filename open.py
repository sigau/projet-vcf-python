#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re, gzip 
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

#####ouvrir/recuperer le fichier

fichiervcf=open(input("nom du fichier :"),"r")
#print(fichiervcf)
fichiervcf2=str(fichiervcf)

######recup de l'extention

name=re.search("\s(.{6})(.*)'\s(.{4})\=",fichiervcf2)
#print(name.group(2))
name2=name.group(2)
#print(name2)
extention=re.search("\.(.+)",name2)
extention2=extention.group(1)
#print(extention2)

#####verification de l'extention 

if (extention2=="vcf"):
    contenu=fichiervcf.read()
    print (contenu)
    fichiervcf.close()
    
    
if(extention2=="vcf.tar.gz" or extention2=="vcf.tgz"):
    print("merde ça cloche")
    #autoriser le .tgz uniquememnt s'il contient que un seul fichier

else :
    print("les fichier accepter sont .vcf ou .vcf.tar.gz ou vcr.tgz")
