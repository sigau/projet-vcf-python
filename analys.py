#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###kowalski, analysis !

import os, sys, re, gzip 
from pprint import pprint

subtitution=0
insertion=0
deletion=0
variation=0

for var in contenu :
    #compte des deletion 
    if ((len(ref)>len(alt))or( alt=="-")):
        deletion+=1
        variation+=1

    #compte des insertion
    if((len(ref)<len(alt)):
        insertion+=1
        variation+=1

    #compte des substituion
    if ((len(ref)=len(alt)):
        substitution+=1
        variation+=1

pprint(
        
