#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import os, sys, re, gzip 
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from pprint import pprint
import webbrowser 

###use with VCF4.1 file please
###test on ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

###graphic interface begin here
fenetre = Tk()
fenetre.geometry()
label = Label(fenetre, text="kowalski's analysis")
bouton=Button(fenetre, text="continu", command=fenetre.quit)
bouton.pack()
fichiervcf=askopenfilename(title="quel fichier voulez-vous ouvrir?",filetypes=[("vcf file",".vcf",),('all files a tes risque et perils','.*')])
    #for the next update
    #("fichier vcf compresser .gz",".vcf.gz"),("fichier vcf compresser vcf.tar.gz",".vcf.tar.gz")
label.pack(fill=BOTH, expand=True)
fenetre.mainloop()

####regex and dictionaries
def analyse(fichiervcf):

    with open(fichiervcf,"r") as fichiervcf2:

        global dicovar
        dicovar={}
        global dico2
        dico2={}
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
            info=re.search("(^\d*|^X|^Y)\s(\d*)\s(.*)\s([ACGT]*)\s([ACGT]*|\.|<.*>)\s(\d*|.)\s(\S*)\s",ligne)
            

        ### getting the damn chromosome("(^\d*|^X|^Y)\s")
            if info :
                chromosome="chromosome "+info.group(1)

        ### getting the damn position("\s(\d*)\s")s
                position=info.group(2)

        ### getting the damn Id("\s(.*)\s")
                identifiant=info.group(3)


        ### getting the damn reference's Nucleobase ("\s([ACGT]*)\s")
                ref=info.group(4)

        ### getting the damn change/variant ("\s([ACGT]*)\s")
                alt=info.group(5)

        ### getting the damn quality ("\s(\d*|.)\s")
                qualite=info.group(6)
                    
        #recuperation du filtre ("\s(\S*)\s")
                filtre=info.group(7)


        ### variations' count  
            ### deletions' count 
                if ((len(ref)>len(alt))or( alt=="-")):
                    deletion+=1
                    variation+=1
                    typevariant="deletion"
            ### insertions' count
                if(len(ref)<len(alt)):
                    insertion+=1
                    variation+=1
                    typevariant="insertion"
            ### substitutions' count
                if (len(ref)==len(alt)):
                    substitution+=1
                    variation+=1
                    typevariant="substitution"


        ####dictionaries
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

                if typevariant in dico2.keys():
                    if chromosome in dico2[typevariant].keys():
                        dico2[typevariant][chromosome].append(liste)
                    else :
                        dico2[typevariant][chromosome]=chromosome
                        dico2[typevariant][chromosome]=liste
                else:
                    dico2[typevariant]={}
                    dico2[typevariant][chromosome]=chromosome
                    dico2[typevariant][chromosome]=liste




        ### number of each variations' type
    global pins
    pins=(insertion/variation)*100
    global pdel
    pdel=(deletion/variation)*100
    global psub
    psub=(substitution/variation)*100


#### file's checking 
if os.path.isfile(fichiervcf) :
    messagebox.showinfo("kowalski's analysis","ok c'est bon c'est un fichier, on continue !")
    with open(fichiervcf,"r") as fichiervcf2 :
        fichiervcf3=str(fichiervcf2)
        fichiervcf4=fichiervcf2.readlines() 


                 #### just checking that the file is not empty
        if ( os.path.getsize(fichiervcf)!=0):
            messagebox.showinfo("kowalski's analysis","c'est un beau bébé il pese "+str(os.path.getsize(fichiervcf))+" octets"+"\n"+"on continue !")
            print("c'est un beau bébé il pese "+str(os.path.getsize(fichiervcf))+" octets")

            
                #### just some kludges with your file for getting his extension
            name=re.search("\s(.{6})(.*)'\s(.{4})\=",fichiervcf3)
            name2=name.group(2)
            print("nom du fichier: "+name2)
            extention=re.search("\.(.+)",name2)
            extention2=extention.group(1)
            messagebox.showinfo("kowalski's analysis","fichier au format "+extention2)


                ### just checking his extension now 
            if (extention2=="vcf.tar.gz" or extention2=="vcf.tgz"or extention2=="vcf" ):
                if(extention2=="vcf.tar.gz" or extention2=="vcf.tgz"):
                    print("le fichier va etre decompresser")
                    with gzip.open(fichiervcf2,"rb") as decompresse:
                        print(decompresse.read())
                    #### to be continued 
                else :
                    contenu=str(fichiervcf4)
                    version=re.search("fileformat=(.{7})",contenu)


                    #### just checking his version 
                if (version.group(1)=="VCFv4.1"):
                    messagebox.showinfo("kowalski's analysis","tis is a v4.1 VCF file great !")
                

                    ### never let a man... a file with a empty body soooo just checking  
                    for line in fichiervcf4:   
                        corps=re.search("^\w",line)
                        if re.search("^(#)",line):
                             continue
                        if corps:
                            messagebox.showinfo("kowalski's analysis","I see.. I see... a head and a body !")
                            break
                        else :
                            messagebox.showerror("kowalski's analysis","nobody! get it ? no body like nobody ")
                            exit()

                    analyse(name2)

                    ### analysis of the file
                    if (messagebox.askquestion("kowalski's analysis","do you want to see your file analysis ?")=="yes"):
                        nbvar=("number of variations= "+ str(variation)+"\n"+"number of substitutions= "+str(substitution)+"\n"+"number of insertions="+str(insertion)+"\n"+"number of deletions= "+str(deletion))
                        pcvar=("rate of substitution= "+str(psub)+"%"+"\n"+"rate of insertion="+str(pins)+"%"+"\n"+"rate of deletions= "+str(pdel)+"%")
                        messagebox.showinfo("kowalski's analysis",nbvar +"\n"+pcvar)

                    ### representation of the number of each variation in a pie chart    
                    if (messagebox.askquestion("kowalski's analysis","I just made a pie do you want to see it ?")=="yes"):
                        labels=["deletions","substitution","insertion"]
                        data=[deletion,substitution,insertion]
                        explode=(0,0,0)
                        plt.pie(data,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90,shadow=True)
                        plt.axis('equal') 
                        plt.show()
                    ### dictionary with chromosome->variation type -> position+references+changes 
                    if (messagebox.askquestion("kowalski's analysis","Do you want to see every variations sort by chromosome ?")=="yes"):
                        top = Toplevel()
                        top.title("kowalski's analysis")
                        scrollbarY = Scrollbar(top)
                        scrollbarY.pack(side=RIGHT, fill=Y)
                        msg = Message(top, text=dicovar)
                        msg.pack(side=LEFT, fill=BOTH,expand=True)
                        button = Button(top, text="Dismiss", command=top.destroy)
                        button.pack()

                    if (messagebox.askquestion("kowalski's analysis","Do you want to see every chromosomes sort by variation ?")=="yes"):
                        top = Toplevel()
                        top.title("kowalski's analysis")
                        scrollbarY = Scrollbar(top)
                        scrollbarY.pack(side=RIGHT, fill=Y)
                        msg = Message(top, text=dico2)
                        msg.pack(side=LEFT, fill=BOTH,expand=True)
                        button = Button(top, text="Dismiss", command=top.destroy)
                        button.pack()
                    else:
                        ### analysis for a single chromosome, you can choose one no more no less 
                        if (messagebox.askquestion("kowalski's analysis","Do you want to see every variations for one chromosome ?")=="yes"):
                            def sel() :
                                select = "kowalski's analysis of chromosome " + str(box.get())
                                label2.config(text = select)
                            box = StringVar()
                            for item in dicovar.keys() :
                                Radiobutton(fenetre, text = item, variable = box, value = item, command = sel).pack()
                            label2 = Label(fenetre)
                            bouton2 = Button(fenetre, text = "Analysis", command = fenetre.quit)
                            bouton2.pack()
                            fenetre.mainloop()
                            messagebox.showinfo("kowalski's analysis", "Here the informations from " + str(box.get()))
                            messagebox.showinfo("kowalski's analysis", dicovar[str(box.get())])
                            top2 = Toplevel()
                            top2.title(" kowalski's analysis")
                            scrollbarY = Scrollbar(top2)
                            scrollbarY.pack(side=RIGHT, fill=Y)
                            msg2 = Message(top2, text=dicovar[str(box.get())])
                            msg2.pack(fill=BOTH,expand=True)
                            button2 = Button(top2, text="Dismiss", command=top2.destroy)
                            button2.pack()

                        ### analysis for a single chromosome, you can choose one no more no less
                        else :
                            if (messagebox.askquestion("kowalski's analysis","Do you want to see every chromosomes for one variation ?")=="yes"):
                                def sel2() :
                                    select2 = "We will analyze the type of variation also known as " + str(box2.get())
                                    label3.config(text = select2)
                                box2 = StringVar()
                                for item in dico2.keys() :
                                    Radiobutton(fenetre, text = item, variable = box2, value = item, command = sel2).pack()
                                label3 = Label(fenetre)
                                bouton3 = Button(fenetre, text = "Analysis", command = fenetre.quit)
                                fenetre.mainloop()
                                messagebox.showinfo("kowalski's analysis", "Here the informations from " + str(box2.get()))
                                messagebox.showinfo("kowalski's analysis", dico2[str(box2.get())])
                                top3 = Toplevel()
                                top3.title("kowalski's analysis")
                                scrollbarY = Scrollbar(top3)
                                scrollbarY.pack(side=RIGHT, fill=Y)
                                msg3 = Message(top3, text=dico2[str(box2.get())])
                                msg3.pack(fill=BOTH,expand=True)
                                button3 = Button(top3, text="Dismiss", command=top3.destroy)
                                button3.pack()


                    ### satisfaction survey
                    if (messagebox.askyesno("kowalski's analysis satisfaction survey","are you satisfied of kowalski's analysis ?  ")):
                        webbrowser.open("https://j.gifs.com/nrDwvl.gif") 
                    else:
                        webbrowser.open("https://j.gifs.com/N9P34z.gif")


                    messagebox.showinfo("kowalski's analysis","thank you for using kowalski!" )               
                    fichiervcf2.close()


                    ### every time you don't respect the law you will end here: error zone
                else :
                    messagebox.showerror("kowalski's analysis","put a file in version 4.1 the others are hasbeen or in the turfu")

            else:
                messagebox.showerror("kowalski's analysis","for the time being, only .vcf files are acepted")
                     
        else :
            messagebox.showerror("kowalski's analysis","empty file")
else :
    messagebox.showerror("kowalski's analysis","one file at a time please, I'm not superman I'm just a program made by a student!")
