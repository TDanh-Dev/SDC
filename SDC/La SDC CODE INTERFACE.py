





from sre_constants import LITERAL_UNI_IGNORE
from tkinter import *
import pygame

#Ajouter de la musique
pygame.mixer.init()







#paramètres de la fenetre
window = Tk()
window.title("La Secte Des Clowns")
window.geometry("1920x1080")
window.minsize(1920,1080)
window.config( background ='black')

#Emplacement du fichier
import os
directory = os.getcwd()
print("c'est ça" + directory)


window.iconbitmap(r'MASQUE-CLOWNS.ico')


#création du titre
frame = Frame(window, bg= "black")
frame.pack(expand=YES)

title = Label(frame, text = "La Secte Des Clowns", font=("Trash Toys 02", 50), bg = "black", fg = "white")
title.pack()



#ajout d'image
width = 300
height = 300
image = PhotoImage(file="MASQUE-CLOWN.png").zoom(35).subsample(32)
canvas = Canvas(window, width=width, height=height,bg='black')
canvas.create_image(width,height/2, image=image)
canvas.pack(expand=YES)





#DEMANDER NOM
def DEMANDER_NOM() : 
    title.pack_forget()
    STARTBUTTON.pack_forget()
    canvas.pack_forget()
    frame.pack_forget()
    framestart.pack_forget()

    global EnterFrame
    EnterFrame = Frame(window, bg="grey")
    EnterFrame.pack(expand=YES)

    global VALIDERFrame
    VALIDERFrame = Frame(window,bg="grey")
    VALIDERFrame.pack(expand=YES)

    global EnterName
    EnterName = Label(EnterFrame, text="Entre ton pseudo", font = ("Trash Toys 02", 30), bg = "grey", fg="white")
    EnterName.pack(expand=YES)

    global NomEntry
    NomEntry = Entry(EnterFrame, font = ("Trash Toys 02", 30), bg="grey", fg="black", justify= "center")
    NomEntry.pack(expand=YES)
    NomEntry.bind('<Return>')

    global Valider
    Valider = Button(VALIDERFrame, text = "Valider", font=("Trash Toys 02", 20), bg = "grey", fg = "black", cursor="hand2", command=DEMANDER_AGE)
    Valider.pack()
    
    return NomEntry
    



#DEMANDER AGE
def DEMANDER_AGE() :
    global Valider
    EnterName.pack_forget()
    NomEntry.pack_forget()
    Valider.pack_forget()

    global EnterAge    
    EnterAge = Label(EnterFrame, text="Entre ton âge", font = ("Trash Toys 02", 30), bg = "grey", fg="white")
    EnterAge.pack(expand=YES)

    global AgeEntry
    AgeEntry = Entry(EnterFrame, font = ("Trash Toys 02", 30), bg="grey", fg="black", justify= "center")
    AgeEntry.pack(expand=YES)
    AgeEntry.bind('<Return>')


    Valider = Button(VALIDERFrame, text = "Valider", font=("Trash Toys 02", 20), bg = "grey", fg = "black", cursor="hand2", command = INTRO) 
    Valider.pack()

    return AgeEntry


    
        

        
#CONTEXTE DU JEU
def INTRO ():

    global EnterFrame
    EnterFrame.pack_forget()
    global VALIDERFrame
    VALIDERFrame.pack_forget()

    VALIDERFrame.pack_forget()
    EnterFrame.pack_forget()
    global AgeEntry
    global NomEntry
    AgeEntry=AgeEntry.get()
    NomEntry=NomEntry.get()

    global INTROFRAME
    INTROFRAME = Frame(window, bg="black")
    INTROFRAME.pack(expand=YES)

    global INTROlabel
    INTROlabel = Label(INTROFRAME, text=f"Ok donc tu t'appelles {NomEntry} et t'as {AgeEntry} piges.", font = ("Trash Toys 02", 30), bg = "black", fg="white")
    INTROlabel.pack(expand=YES)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    INTROFRAME.pack(expand=YES)
    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command = CHOIXINTRO) 
    Suivant.pack()

    pygame.mixer.music.load("SOUNDTRACK SDC.mp3")
    pygame.mixer.music.play(-1)
    











#PREMIER DILEMME
def CHOIXINTRO():
    global Suivant
    Suivant.pack_forget()
    global INTROlabel
    INTROlabel.pack_forget()

    global CHOIXINTROlabel
    CHOIXINTROlabel = Label(INTROFRAME, text="Tu As DeS mEnOtTeS aUx PoIgNeTs. HiHi.\n Il Y a A tA dRoItE uN jOuRnAl Et A tA gAuChE uNe TaRtE mErInGuEe. MMMH.", font = ("Trash Toys 02", 30), bg = "black", fg="white")
    CHOIXINTROlabel.pack(expand=YES)

    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=CHOOSE1) 
    Suivant.pack()




def CHOOSE1():
    global CHOIXINTROlabel
    CHOIXINTROlabel.pack_forget()

    global Suivant
    Suivant.pack_forget()

    global Suivantframe
    Suivantframe.pack_forget()

    global CHOOSE1label
    CHOOSE1label = Label(INTROFRAME, text="LeQuEl VaS-tU cHoIsIr ? HOHOHOHOHO. \n Le JOURNAL... ou LA TAAAAARTE ? ", font = ("Arial", 40), bg = "black", fg="white")
    CHOOSE1label.pack(expand=YES)

    global CHOICEFRAME
    CHOICEFRAME = Frame(window, bg="black")
    CHOICEFRAME.pack(expand=YES)

    global TARTE
    TARTE = Button(CHOICEFRAME, text = "La tarte", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=CHOICETARTE) 
    TARTE.pack()
    global JOURNAL
    JOURNAL = Button(CHOICEFRAME, text = "Le journal", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=CHOICEJOURNAL) 
    JOURNAL.pack()



def CHOICETARTE():
    global CHOOSE1label
    CHOOSE1label.pack_forget()
    global CHOICEFRAME
    CHOICEFRAME.pack_forget()
    global JOURNAL
    JOURNAL.pack_forget()
    global TARTE
    TARTE.pack_forget()

    global CHOOSEJOURNAL
    CHOOSEJOURNAL = Label(INTROFRAME, text= "HAHAHAHAHAH Le ChOiX dE lA gOuRmAnDiSe !", font = ("Arial", 30), bg = "black", fg="white")
    CHOOSEJOURNAL.pack(expand=YES)

    global image2
    image2 = PhotoImage(file="YEUX SINGE.png")
    global label
    label = Label(image = image2)
    label.pack(expand=YES)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("CRR.mp3")
    pygame.mixer.music.play(-1)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=MONKEY) 
    Suivant.pack()



def MONKEY():
    global CHOOSEJOURNAL, Suivantframe, INTROFRAME, Suivant, label
    CHOOSEJOURNAL.pack_forget() 
    Suivantframe.pack_forget()  
    INTROFRAME.pack_forget()
    Suivant.pack_forget()
    label.pack_forget()

    global MONKIMAGE
    MONKIMAGE = PhotoImage(file="SINGE FOU.png")
    global labelMONKE
    labelMONKE = Label(image = MONKIMAGE, text="You LOSE. \nYou died from the madness\n caused by the cymbals.", compound='center', fg = "red", font = ("Trash Toys 02", 70))
    labelMONKE.pack(expand=YES)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("MAD MONKEYS.mp3")
    pygame.mixer.music.play(-1)








    


def CHOICEJOURNAL():
    global CHOOSE1label
    CHOOSE1label.pack_forget()
    global CHOICEFRAME
    CHOICEFRAME.pack_forget()
    global JOURNAL
    JOURNAL.pack_forget()
    global TARTE
    TARTE.pack_forget()
    


    global CHOOSEJOURNAL
    CHOOSEJOURNAL = Label(INTROFRAME, text='31 oct.2022\n LA SECTE DES CLOWNS\n Une semaine avant Halloween, de nombreux meurtres ont été commis. \n Ceux-ci étaient signés par "LA SECTE DES CLOWNS".\n\nRonald, victime de séquestration au sein de la Secte des Clowns, a décidé de témoigner :\n\nRonald : "Je me suis réveillé dans une cage au beau milieu de nulpart.\nA côté de moi, avait été déposé un journal et un pistolet à o.\nPar instinct, je me suis saisi du journal, ce choix était le premier mais pas le dern..."\n\nLe journal a été déchiré. ', font = ("Arial", 30), bg = "black", fg="white")
    CHOOSEJOURNAL.pack(expand=YES)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=THOMASTRAIN) 
    Suivant.pack()



def THOMASTRAIN() :
    global CHOOSEJOURNAL, Suivantframe, INTROFRAME, Suivant
    CHOOSEJOURNAL.pack_forget() 
    Suivantframe.pack_forget()  
    INTROFRAME.pack_forget()
    Suivant.pack_forget()
    
    
    
    global MONKIMAGE
    MONKIMAGE = PhotoImage(file="THOMAS-TRAIN.png")

    global buttonMONKE
    buttonMONKE = Button(image = MONKIMAGE, text="Suivant", compound='center', bg = "grey", fg = "white", font = ("Trash Toys 02", 70), command=CHOIXTELEPHONE)
    buttonMONKE.pack(expand=YES)



    pygame.mixer.music.pause()
    pygame.mixer.music.load("THOMAS INC.mp3")
    pygame.mixer.music.play()



def CHOIXTELEPHONE ():   
    global buttonMONKE
    buttonMONKE.pack_forget()


    global INTROFRAME
    INTROFRAME = Frame(window, bg="black")
    INTROFRAME.pack(expand=YES)
    global CHOICEFRAME
    CHOICEFRAME = Frame(window, bg="black")
    CHOICEFRAME.pack(expand=YES)


    global CHOIXTELEPHONELABEL
    CHOIXTELEPHONELABEL = Label(INTROFRAME, text="Le train vous dépose un téléphone.\n\n Il Y a 2 MeSsAgEs HEHEHE. \nL'uN vIeNt DeS pOmPiErS, l'AuTrE dE mOi. HIIIIHIHIHI. \n\n VaS-tU pLeUrEr DaNs LeS jUpOnS dEs PoMpIeRs ? \nOu CoNtInUeR l'AvEnTuRe AvEc MoI ? HAHAHAHAHAH. ", font = ("Trash Toys 02", 30), bg = "black", fg="white")
    CHOIXTELEPHONELABEL.pack(expand=YES)

    global POMPIERS
    POMPIERS = Button(CHOICEFRAME, text = "Ecouter les pompiers", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=POMPIERSMESSAGE)
    POMPIERS.pack()
    global LUI
    LUI = Button(CHOICEFRAME, text = "Ecouter son message", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=LUIMESSAGE) 
    LUI.pack()

    pygame.mixer.music.load("SOUNDTRACK SDC.mp3")
    pygame.mixer.music.play(-1)


def POMPIERSMESSAGE ():
    global INTROFRAME, CHOIXTELEPHONELABEL, POMPIERS, LUI, CHOICEFRAME
    CHOICEFRAME.pack_forget()
    CHOIXTELEPHONELABEL.pack_forget()
    POMPIERS.pack_forget()
    LUI.pack_forget()


    global CHOIXPOMPIERS
    CHOIXPOMPIERS = Label(INTROFRAME, text= "TsS tSs TsS... La FaCiLiTé... \nTu As FaIt Le ChOiX dE lA PARESSE... \n\nAAAAAAAAAAH", font = ("Arial", 30), bg = "black", fg="white")
    CHOIXPOMPIERS.pack(expand=YES)


    pygame.mixer.music.stop()
    pygame.mixer.music.load("GAS LEAK.mp3")
    pygame.mixer.music.play(-1)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command = GAZ) 
    Suivant.pack()


def GAZ():
    global INTROFRAME, Suivantframe, Suivant
    INTROFRAME.pack_forget()
    Suivantframe.pack_forget()
    Suivant.pack_forget()
   

    global GASMOKE
    GASMOKE = PhotoImage(file="GAS SMOKE.png")
    global labelGAS
    labelGAS = Label(image = GASMOKE, text="You LOSE. \nA deadly gas is asphyxiating you.", compound='center', fg = "red", font = ("Trash Toys 02", 70))
    labelGAS.pack(expand=YES)

    
    pygame.mixer.music.load("GAS LEAK.mp3")
    pygame.mixer.music.play(-1)



def LUIMESSAGE ():
    global INTROFRAME, CHOICEFRAME, CHOIXTELEPHONELABEL, POMPIERS, LUI
    CHOICEFRAME.pack_forget()
    CHOIXTELEPHONELABEL.pack_forget()
    POMPIERS.pack_forget()
    LUI.pack_forget()


    global CHOIXLUI
    CHOIXLUI = Label(INTROFRAME, text="HAHAHAH AuDaCiEuX ! J'aImE çA !\n PoUr Te RéCoMpEnSeR vOiLà UnE éNiGmE :", font = ("Arial", 30), bg = "black", fg="white")
    CHOIXLUI.pack(expand=YES)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=CHOIX2CHEMINS) 
    Suivant.pack()

    pygame.mixer.music.pause()
    pygame.mixer.music.load("CREEPY MESSAGE.mp3")
    pygame.mixer.music.play(-1) 


def CHOIX2CHEMINS():
    global INTROFRAME, Suivantframe, CHOICEFRAME, CHOIXLUI
    Suivantframe.pack_forget()
    CHOIXLUI.pack_forget()


    global CHOIXCHEMINS
    CHOIXCHEMINS = Label(INTROFRAME, text="2 objets vous sont jetés, \n tous les 2 semblent être reliés à quelque chose. \n\nIl y a une branche de figuier et une montre. \n\nLequel voulez-vous choisir ?", font = ("Arial", 40), bg = "black", fg="white")
    CHOIXCHEMINS.pack(expand=YES)

    global CHOICEFRAME
    CHOICEFRAME = Frame(window, bg="black")
    CHOICEFRAME.pack(expand=YES)

    global BRANCHE
    BRANCHE = Button(CHOICEFRAME, text = "La branche", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=CHOIXBRANCHE) 
    BRANCHE.pack()
    global MONTRE
    MONTRE = Button(CHOICEFRAME, text = "La montre", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=CHOIXMONTRE) 
    MONTRE.pack()

    pygame.mixer.music.stop()
    pygame.mixer.music.load("SOUNDTRACK SDC.mp3")
    pygame.mixer.music.play(-1) 


def CHOIXMONTRE():
    global BRANCHE, MONTRE, CHOIXCHEMINS, CHOICEFRAME
    CHOIXCHEMINS.pack_forget()
    BRANCHE.pack_forget()
    MONTRE.pack_forget()

    global CHOIXLUI
    CHOIXLUI = Label(INTROFRAME, text="CeLuI qU'oN nE cEsSe D'eSsAyEr De TuEr... LE TEMPS ! ZzzZZz\n\nLa montre est en fait relié à une bombe à retardement.\n Vous devez couper un fil blanc ou fil noir\nAlOrS ? qUeL fIl VaS-tU cOuPeR ? lE bLaNc ? Ou Le NoIr ? HEHEHEH", font = ("Arial", 30), bg = "black", fg="white")
    CHOIXLUI.pack(expand=YES)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

   
    BRANCHE = Button(CHOICEFRAME, text = "Le fil noir", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command=FILNOIR) 
    BRANCHE.pack()
    
    MONTRE = Button(CHOICEFRAME, text = "Le fil blanc", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2",command=FILBLANC) 
    MONTRE.pack()


def FILNOIR():
    global CHOIXLUI, Suivantframe, BRANCHE, MONTRE, CHOICEFRAME, INTROFRAME
    CHOIXLUI.pack_forget()
    Suivantframe.pack_forget()
    BRANCHE.pack_forget()
    MONTRE.pack_forget()
    CHOICEFRAME.pack_forget()



    global INTROGEORGES
    INTROGEORGES = Label(INTROFRAME, text="La bombe semble désactivée.\nLa lumière s'allume, vous êtes sur la scène d'un cirque et la cage se lève.\nLe cirque est totalement vide.\n\nEn sortant du cirque, vous vous retrouvez devant votre maison, mais en feu.\nVotre famille a eu le temps de sortir et vous courrez les retrouver\n\nThe END.",justify='left', font = ("Arial", 30), bg = "black", fg="white")
    INTROGEORGES.pack(expand=YES)

def FILBLANC():
    global CHOIXLUI, Suivantframe, BRANCHE, MONTRE, CHOICEFRAME, INTROFRAME
    CHOIXLUI.pack_forget()
    Suivantframe.pack_forget()
    BRANCHE.pack_forget()
    MONTRE.pack_forget()
    CHOICEFRAME.pack_forget()



    global INTROGEORGES
    INTROGEORGES = Label(INTROFRAME, text="Tu As DoNc ChOiSiS dE tE sEpArEr De Ta PuReTé...\nAiNsI sOiT-iL, vA !\nPrOfiTe De La ViE qUe Tu As ChOiSiS HAHAHAHAH\n\nLa bombe semble désamorcée, la lumière s'allume, vous êtes sur la scène d'un cirque et la cage se lève.\nEn sortant du cirque, vous vous retrouvez devant un château, où des servants vous accueillent.\nIls vous apprennent le décès de votre famille entière suite à un incendie.\n\nThe END.",justify='left', font = ("Arial", 30), bg = "black", fg="white")
    INTROGEORGES.pack(expand=YES)




def CHOIXBRANCHE ():
    global BRANCHE, MONTRE, CHOIXCHEMINS, CHOICEFRAME
    CHOICEFRAME.pack_forget()
    CHOIXCHEMINS.pack_forget()
    BRANCHE.pack_forget()
    MONTRE.pack_forget()

    global CHOIXLUI
    CHOIXLUI = Label(INTROFRAME, text="La BrAnChE dE fIgUiEr ! cOnNaIs-Tu SeUlEmEnT sA sYmBoLiQuE ?\n hEhEhE\n\nEn ToUt CaS, fElIcItAtIoNs ! Tu N'aS pAs EtE tEnTé PaR lA qUêTe VaInE dE l'AsSaSsInAt Du TeMpS !\n\nTu As PaSsE tOuTeS lEs EpReUvEs AvEc BrIo !!! HOHOHO", font = ("Arial", 30), bg = "black", fg="white")
    CHOIXLUI.pack(expand=YES)

    global Suivantframe
    Suivantframe = Frame(window, bg="white")
    Suivantframe.pack(expand=YES)

    global Suivant
    Suivant = Button(Suivantframe, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=CIRCUS) 
    Suivant.pack()


def CIRCUS():
    global CHOIXLUI, INTROFRAME, Suivantframe, Suivant
    CHOIXLUI.pack_forget()
    INTROFRAME.pack_forget()
    Suivant.pack_forget()
    Suivantframe.pack_forget()
    

    global CIRCUSIMAGE
    CIRCUSIMAGE = PhotoImage(file="CIRCUS.png")

    global buttonCIRCUS
    buttonCIRCUS = Button(image = CIRCUSIMAGE, text="Suivant", compound='center', bg = "grey", fg = "white", font = ("Trash Toys 02", 70), command=GEORGES)
    buttonCIRCUS.pack(expand=YES)

    
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Musique de cirque.mp3")
    pygame.mixer.music.play(-1) 


def GEORGES():
    global NomEntry, buttonCIRCUS
    buttonCIRCUS.pack_forget()

    

    global CLOWNEYFRAME
    CLOWNEYFRAME =Frame(window, bg="black")
    CLOWNEYFRAME.pack(side=LEFT)

    global CLOWNEYPIC
    CLOWNEYPIC = PhotoImage(file="GOD CLOWNEY.png")
    global CLOWNEYlabel
    CLOWNEYlabel = Label(CLOWNEYFRAME, image = CLOWNEYPIC)
    CLOWNEYlabel.pack(side=LEFT)

    global INTROFRAME
    INTROFRAME = Frame(window, bg="black")
    INTROFRAME.pack(side=LEFT)

    global INTROGEORGES
    INTROGEORGES = Label(INTROFRAME, text=f"Bonjour, je m'appelle Georges. Enchanté {NomEntry}\n\nC'est moi qui suis le grand gourou de la Secte des Clowns.\nDepuis 10 ans maintenant, nous œuvrons dans le but\nde reglorifier les Clowns qui sont de nos jours méprisés.\n",justify='left', font = ("Arial", 30), bg = "black", fg="white")
    INTROGEORGES.pack(side=LEFT)




    global Suivant
    Suivant = Button(INTROFRAME, text = "Suivant", font=("Trash Toys 02", 20), bg = "grey", fg = "white", cursor="hand2", command=GEORGES2) 
    Suivant.pack(side=BOTTOM)



    

    pygame.mixer.music.stop()
    pygame.mixer.music.load("SOUNDTRACK SDC.mp3")
    pygame.mixer.music.play(-1) 


def GEORGES2 ():
    global CLOWNEYFRAME, CLOWNEYlabel, INTROFRAME, INTROGEORGES, Suivant
    CLOWNEYFRAME.pack_forget()
    CLOWNEYlabel.pack_forget()
    INTROFRAME.pack_forget()
    INTROGEORGES.pack_forget()
    Suivant.pack_forget()

    global LASTCHOICEFRAME
    LASTCHOICEFRAME = Frame(window, bg = "black")
    LASTCHOICEFRAME.pack(expand=YES)

    CHOIXLUI = Label(LASTCHOICEFRAME, text="Tu as passé toutes mes épreuves.\n Tu es digne d'être mon successeur.\n Souhaites-tu prendre la relève ?\nSi tu refuses, je dissoudrai la Secte et disparaitrais avec.", font = ("Arial", 30), bg = "black", fg="white")
    CHOIXLUI.pack(expand=YES)


    global CHOICEFRAME
    CHOICEFRAME = Frame(window, bg="black")
    CHOICEFRAME.pack(expand=YES)

    global REFUSER
    REFUSER = Button(CHOICEFRAME, text = "Refuser", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command = BYE) 
    REFUSER.pack()
    global ACCEPTER
    ACCEPTER = Button(CHOICEFRAME, text = "Accepter", font=("Trash Toys 02", 30), bg = "grey", fg = "white", cursor="hand2", command= BESTEND) 
    ACCEPTER.pack()

def BYE():
    global LASTCHOICEFRAME, CHOICEFRAME, REFUSER, ACCEPTER, CHOIXLUI
    LASTCHOICEFRAME.pack_forget()
    REFUSER.pack_forget()
    ACCEPTER.pack_forget()
    CHOIXLUI.pack_forget()


    global ENDINGBYE
    ENDINGBYE = Label(CHOICEFRAME, text="3 ans plus tard.\n\nLe monde est en dépression. Les clowns n'existent plus.\n Les gens ne savent plus rire et prennent tout au premier degré.\n Le taux de suicide est à son paroxisme.\n\n\n The END.", font = ("Arial", 30), bg = "black", fg="white")
    ENDINGBYE.pack(expand=YES)



def BESTEND():
    global LASTCHOICEFRAME, CHOICEFRAME, REFUSER, ACCEPTER, CHOIXLUI
    LASTCHOICEFRAME.pack_forget()
    REFUSER.pack_forget()
    ACCEPTER.pack_forget()
    CHOIXLUI.pack_forget()
    CHOICEFRAME.pack_forget()


    global CLOWNEYFRAME
    CLOWNEYFRAME =Frame(window, bg="black")
    CLOWNEYFRAME.pack(side=LEFT)

    global CLOWNEYPIC
    CLOWNEYPIC = PhotoImage(file="CRUSTY.gif")
    global CLOWNEYlabel
    CLOWNEYlabel = Label(CLOWNEYFRAME, image = CLOWNEYPIC)
    CLOWNEYlabel.pack(side=LEFT)

    global INTROFRAME
    INTROFRAME = Frame(window, bg="black")
    INTROFRAME.pack(side=LEFT)

    global INTROGEORGES
    INTROGEORGES = Label(INTROFRAME, text=f" 3 ans plus tard.\n\n\n Et notre nouveau président\n avec plus de 60% des voix est...\n{NomEntry} !!! \n\n HAHAHAHAHHA\n\n The END.",justify='left', font = ("Arial", 30), bg = "black", fg="white")
    INTROGEORGES.pack(side=LEFT)





    
   


   





#création du bouton
framestart = Frame(window, bg="black", bd=3, relief=SUNKEN)
framestart.pack(expand=YES)

STARTBUTTON = Button(framestart, text = "START", font=("Trash Toys 02", 30), bg = "grey", fg = "black", cursor="hand2", command=DEMANDER_NOM)
STARTBUTTON.pack()



window.mainloop()


