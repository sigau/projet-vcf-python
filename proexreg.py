#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/


info=re.search("(^\d*|^X|^Y)\s(\d*)\s(.*)\s([ACGT]*)\s([ACGT]*)\s")

#recuperation du chromosome("(^\d*|^X|^Y)\s")
if info :
    chromosome=info.group(1)


#recuperation de la position("\s(\d*)\s")
if info :
    position=info.group(2)

#recuperation Id("\s(.*)\s")
if info :
    identifiant=info.group(3)

#recuperation de la base de reference ("\s([ACGT]*)\s")
if info :
    position=info.group(4)

#recuperation de la variation ("\s([ACGT]*)\s")
if info:
    alt=info.group(5)

#recuperation de la qualité ("\s(\d*|.)\s")
if info :
    qualite=info.group(6)

#recuperation du filtre ("\s(\S*)\s")
if info :
    filtre=info.group(7)
    
