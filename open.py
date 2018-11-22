#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re, gzip 
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

#####ouvrir/recuperer le fichier######
fichiervcf=sys.argv[1]

def analyse(fichiervcf):

    with open(fichiervcf,"r") as fichiervcf2:
        #tesver=fichiervcf2.readline()
        #print(tesver)

        global substitution
        substitution=0
        global insertion
        insertion=0
        global deletion
        deletion=0
        global variation
        variation=0
        global typevariant
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
                #compte des substitution
                if (len(ref)==len(alt)):
                    substitution+=1
                    variation+=1
                    #print("test substitution")
                    #print("test variation")
                    typevariant="substitution"

    #print("test final")
    #print("nb variation= "+ str(variation)+"\n"+"nb substitution= "+str(substitution)+"\n"+"nb insertion="+str(insertion)+"\n"+"nb deletions= "+str(deletion))

        # ù de chaque type de variation
    global pins
    pins=(insertion/variation)*100
    global pdel
    pdel=(deletion/variation)*100
    global psub
    psub=(substitution/variation)*100
    #print("% substitution= "+str(psub)+"%"+"\n"+"% insertion="+str(pins)+"%"+"\n"+"% deletions= "+str(pdel)+"%")




######verifier que c'est un fichier######
if os.path.isfile(fichiervcf) :
    print("c'est un fichier")
    with open(fichiervcf,"r") as fichiervcf2 :
        fichiervcf3=str(fichiervcf2)
        fichiervcf4=fichiervcf2.readlines() 


                 ######verifier que le fichier n'est pas vide###### 
        if ( os.path.getsize(fichiervcf)!=0):
            print("c'est un beau bébé il pese "+str(os.path.getsize(fichiervcf))+" octets")

            
                ######recup de l'extention######
            name=re.search("\s(.{6})(.*)'\s(.{4})\=",fichiervcf3)
            name2=name.group(2)
            print("nom du fichier: "+name2)
            extention=re.search("\.(.+)",name2)
            extention2=extention.group(1)
            print("fichier au format "+extention2)


                #####verification de l'extention ######
            #autoriser le .tgz uniquememnt s'il contient que un seul fichier ?
            if (extention2=="vcf.tar.gz" or extention2=="vcf.tgz"or extention2=="vcf" ):
                if(extention2=="vcf.tar.gz" or extention2=="vcf.tgz"):
                    print("le fichier va etre decompresser")
                    with gzip.open(fichiervcf2,"r") as decompresse:
                        print(decompresse)
                    ####a completer#####

                else :
                    #fichiervcf4=fichiervcf2.readlines()
                    contenu=str(fichiervcf4)
                    version=re.search("fileformat=(.{7})",contenu)


                    ######verification de la version####
                if (version.group(1)=="VCFv4.1"):                     
                    print("c'est un VCF en version 4.1")
                

                    #est-ce que le corps est vide ?
                    for line in fichiervcf4:   
                        corps=re.search("^\w",line)
                        if re.search("^(#)",line):
                             continue
                        if corps:
                            print("je vois la tete et un corps")
                            break
                        else :
                            print("pas de corps")
                            exit()

                    analyse(name2)
                    print("print analyse du fichier ?")
                    rep=input("yes/no :")
                    if (rep=="yes" or rep=="Yes" or rep=="YES" or rep=="y" or rep=="Y"):
                        print("nb variation= "+ str(variation)+"\n"+"nb substitution= "+str(substitution)+"\n"+"nb insertion="+str(insertion)+"\n"+"nb deletions= "+str(deletion))
                        print("% substitution= "+str(psub)+"%"+"\n"+"% insertion="+str(pins)+"%"+"\n"+"% deletions= "+str(pdel)+"%")                        
                    fichiervcf2.close()

                else :
                    print("mettre un fichier en version 4.1 les autres sont hasbeen ou dans le turfu")

            else:
                print("les fichier accepter sont .vcf ou .vcf.tar.gz ou vcr.tgz")
                     
        else :
            print("fichier vide")
else :
    print("seul les fichiers individuels sont autorisé")