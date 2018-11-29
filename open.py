#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re, gzip 
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from pprint import pprint

#a utiliser avec VCF4.1
#teste sur ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

fenetre = Tk()
label = Label(fenetre, text="kowalski's analysis",padx=500,pady=500)
bouton=Button(fenetre, text="continuer", command=fenetre.quit)
bouton.pack()
fichiervcf=askopenfilename(title="quel fichier voulez-vous ouvrir?",filetypes=[("fichier vcf",".vcf",),("fichier vcf compresser .tgz","vcf.tgz"),("fichier vcf compresser vcf.tar.gz","vcf.tar.gz"),('all files a tes risque et perils','.*')])
label.pack()
fenetre.mainloop()
#####ouvrir/recuperer le fichier######
#fichiervcf=sys.argv[1]


def analyse(fichiervcf):

    with open(fichiervcf,"r") as fichiervcf2:
        #tesver=fichiervcf2.readline()
        #print(tesver)
        global dicovar
        dicovar={}
        global liste
        liste=[]
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

        #recuperation de la position("\s(\d*)\s")s
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
    messagebox.showinfo("kowalski's analysis","ok c'est bon c'est un fichier, on continue !")
    with open(fichiervcf,"r") as fichiervcf2 :
        fichiervcf3=str(fichiervcf2)
        fichiervcf4=fichiervcf2.readlines() 


                 ######verifier que le fichier n'est pas vide###### 
        if ( os.path.getsize(fichiervcf)!=0):
            messagebox.showinfo("kowalski's analysis","c'est un beau bébé il pese "+str(os.path.getsize(fichiervcf))+" octets"+"\n"+"on continue !")
            #print("c'est un beau bébé il pese "+str(os.path.getsize(fichiervcf))+" octets")

            
                ######recup de l'extention######
            name=re.search("\s(.{6})(.*)'\s(.{4})\=",fichiervcf3)
            name2=name.group(2)
            print("nom du fichier: "+name2)
            extention=re.search("\.(.+)",name2)
            extention2=extention.group(1)
            messagebox.showinfo("kowalski's analysis","fichier au format "+extention2)
            #print("fichier au format "+extention2)


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
                    messagebox.showinfo("kowalski's analysis","c'est un VCF en version 4.1")
                    #print("c'est un VCF en version 4.1")
                

                    #est-ce que le corps est vide ?
                    for line in fichiervcf4:   
                        corps=re.search("^\w",line)
                        if re.search("^(#)",line):
                             continue
                        if corps:
                            #print("je vois la tete et un corps")
                            messagebox.showinfo("kowalski's analysis","je vois la tete et un corps")
                            break
                        else :
                            #print("pas de corps")
                            messagebox.showerror("kowalski's analysis","pas de corps !")
                            exit()

                    analyse(name2)
                    if (messagebox.askquestion("kowalski's analysis","print analyse du fichier ?")=="yes"):
                        nbvar=("nb variation= "+ str(variation)+"\n"+"nb substitution= "+str(substitution)+"\n"+"nb insertion="+str(insertion)+"\n"+"nb deletions= "+str(deletion))
                        pcvar=("pourcentage de substitution= "+str(psub)+"%"+"\n"+"pourcentage de insertion="+str(pins)+"%"+"\n"+"pourcentage de deletions= "+str(pdel)+"%")
                        messagebox.showinfo("kowalski's analysis",nbvar +"\n"+pcvar)
                    if (messagebox.askquestion("kowalski's analysis","voulez-vous print le grouphique ?")=="yes"):
                        labels=["deletions","substitution","insertion"]
                        data=[deletion,substitution,insertion]
                        explode=(0,0,0)
                        plt.pie(data,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90,shadow=True)
                        plt.axis('equal') 
                        print("pour continuer cliquer sur le bouton continuer")
                        plt.show()  
                    if (messagebox.askquestion("kowalski's analysis","voulez-vous print le dico entier? ?")=="yes"):
                        #messagebox.showinfo("kowalski's analysis",dicovar)
                        top = Toplevel()
                        top.title("titre kowalski's analysis")
                        scrollbarY = Scrollbar(top)
                        scrollbarY.pack(side=RIGHT, fill=Y)
                        scrollbarX = Scrollbar(top)
                        scrollbarX.pack(side=LEFT, fill=X)
                        msg = Message(top, text=dicovar)
                        msg.pack(side=LEFT, fill=BOTH,expand=1)
                        button = Button(top, text="Dismiss", command=top.destroy)
                        button.pack()
                        mainloop()
                        #pprint(dicovar)
                    else:
                        if (messagebox.askquestion("kowalski's analysis","voulez-vous print le dico pour un chromosome particulier ?")=="yes"):


                            ######a corriger pour ajouter des liste deroulantes####
                            #print(dicovar.keys())
                            listchr=[]
                            #scrollbar = Scrollbar(fenetre)
                            #scrollbar.pack(side=RIGHT, fill=Y)
                            #listetk = Listbox(fenetre,width=60,height=10,font=('times',13),yscrollcommand=scrollbar.set)
                            #listetk = Listbox(fenetre,width=60,height=10,font=('times',13))
                            listetk = Listbox(fenetre)
                            listetk.pack()
                            for cle in dicovar.keys():
                                listchr.append(cle)
                                listetk.insert(END,cle)
                            
                            #listetk.config(yscrollcommand=scrollbar.set)
                            #scrollbar.config(command=listetk.yview)
                            listetk.mainloop()

                            #item=listetk.get(listetk.curselection())
                            print("item")
                            print("liste avec tkinter")
                    
                    messagebox.showinfo("kowalski's analysis","merci d'avoir utiliser kowalski !" )
                    #print("merci d'avoir utiliser kowalski ! ")               
                    fichiervcf2.close()
                else :
                    messagebox.showerror("kowalski's analysis","mettre un fichier en version 4.1 les autres sont hasbeen ou dans le turfshowinfou")
                    #print("mettre un fichier en version 4.1 les autres sont hasbeen ou dans le turfu")

            else:
                messagebox.showerror("kowalski's analysis","les fichier accepter sont .vcf ou .vcf.tar.gz ou vcr.tgz")
                #print("les fichier accepter sont .vcf ou .vcf.tar.gz ou vcr.tgz")
                     
        else :
            messagebox.showerror("kowalski's analysis","fichier vide")
            #print("fichier vide")
else :
    messagebox.showerror("kowalski's analysis","seul les fichiers individuels sont autorisé")
    #print("seul les fichiers individuels sont autorisé")