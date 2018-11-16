#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re, gzip 
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

#####ouvrir/recuperer le fichier######
fichiervcf=sys.argv[1]

               ######verifier que c'est un fichier######
if os.path.isfile(fichiervcf) :
    print("c'est un fichier")
    with open(fichiervcf,"r") as fichiervcf2 :
        fichiervcf3=str(fichiervcf2)


                 ######verifier que le fichier n'est pas vide###### 
        if ( os.path.getsize(fichiervcf)!=0):
            print(os.path.getsize(fichiervcf))

            
            ######verifier qu'il n'y a pas que le header #########
           # for ligne in fichiervcf2.read() :
            #notheader=re.search("^([^#])\s",fichiervcf2.read())
            #if notheader :
                #print("regex ok")
            #else :
                #print ("ne contient que le header")


                ####verifier la version###
            tesver=fichiervcf2.read()
            version=re.search("fileformat=(.*)\s",tesver)
            if (version.group(1)=="VCFv4.1"):
                print("version 4.1")
                
                 ######recup de l'extention######
                name=re.search("\s(.{6})(.*)'\s(.{4})\=",fichiervcf3)
                name2=name.group(2)
                print(name2)
                extention=re.search("\.(.+)",name2)
                extention2=extention.group(1)
                print(extention2)


                #####verification de l'extention ######
                if (extention2=="vcf") :
                    print("ouvrir le fichier ?")
                    rep=input("yes/no :")
                    if (rep=="yes" or rep=="Yes" or rep=="YES" or rep=="y" or rep=="Y"):
                        print (tesver)
                    fichiervcf2.close()
                    
                elif(extention2=="vcf.tar.gz" or extention2=="vcf.tgz"):
                    print("le fichier va etre decompresser")
                    #autoriser le .tgz uniquememnt s'il contient que un seul fichier
                    decompresse=gzip.open(fichiervcf2,"r")
                    contenu=decompresse.read()
                    print (contenu)
                    decompresse.close()
                    
                else :
                    print("les fichier accepter sont .vcf ou .vcf.tar.gz ou vcr.tgz")

            else:
                print("mettre un fichier en version 4.1 les autres sont hasbeen ou dans le turfu")
                     
        else :
            print("fichier vide")
else :
    print("seul les fichiers individuels sont autorisé")
    