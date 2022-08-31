
#JEU LA SECTE DES CLOWNS ESCAPE GAME


print("Vous vous réveillez dans une cage. Vous ne voyez absolument pas ce qu'il y a en dehors de la cage.")

def demander_nom():    
     nom_int = input("Comment vous appelez-vous ? ")  
     return nom_int


def demander_age():
     age_int = 0 
     while age_int == 0 : 
          age_str = input("Quel âge avez-vous ? ") 
          try: 
               age_int = int(age_str) + 0                     #forcer à rentrer un chiffre
          except:
               print("ERREUR : Entrez un chiffre !")

     if age_int == 18 :
          print("A peine majeur, t'es sûr de vouloir continuer ? ")
          MAJEUR = input('Choisissez "oui" ou "non" ')
          while MAJEUR != "oui" and MAJEUR != "non" :
               MAJEUR = input('ERREUR : Choisissez "oui" ou "non" ')
          if MAJEUR == "non" :
               print("Ok, force à toi le reuf.")
               exit()
          else :
               print("Aight, on est ensemble")
     elif age_int >= 18 :
          print("Ok tu peux continuer")
     else :
          print("Ca dégage, pas de mineurs ici.")
          exit()
     return age_int 




nom = demander_nom()
age = demander_age()

     
print("Ok donc tu t'appeles " + nom + " et tu as " + str(age) + " piges")
print("Tu As DeS mEnOtTeS aUx PoIgNeTs. HiHi.")
print("Il Y a A tA dRoItE uN jOuRnAl Et A tA gAuChE uNe TaRtE mErInGuEe. MMMH.")
print("LeQuEl VaS-tU cHoIsIr ? HOHOHOHOHO. Le JOURNAL... ou LA TAAAAARTE ? ")  
GOURMANDISE = input('Choisissez "la tarte" ou "le journal" ')

while GOURMANDISE != "la tarte" and GOURMANDISE != "le journal" : #forcer à rentrer un des 2 choix proposer et rien d'autres
          GOURMANDISE = input('ERREUR : Choisissez "la tarte" ou "le journal." ')


if GOURMANDISE == "la tarte" :
          print("HAHAHAHAHAH Le ChOiX dE lA gOuRmAnDiSe !")
          print("Un jouet singe s'approche de vous en faisant raisonner des cymbales.")
          print("Le bruit s'amplifie à vous percer les tympans. ")
          print("Vous devenez fou, vous mourrez")
          print("YOU LOSE.")
else :
          print("")
          print("31 oct.2022")
          print("LA SECTE DES CLOWNS")
          print("")
          print('Une semaine avant Halloween, de nombreux meurtres ont été commis.  ')
          print('Ceux-ci étaient signés par "LA SECTE DES CLOWNS"')
          print("Ronald, victime de séquestration au sein de la Secte des Clowns, a décidé de témoigner.")
          print('Ronald : "Je me suis réveillé dans une cage au beau milieu de nulpart.')
          print("A côté de moi, avait été déposé un journal et un pistolet à o.")
          print('Par instinct, je me suis saisi du journal, ce choix était le premier mais pas le dern..."')
          print("Le journal a été déchiré.")
          print("")
          print("Peu de temps après, un bruit de train, suivi du train lui-même, vous dépose un téléphone à côté de vous.")
          print("Il Y a 2 MeSsAgEs HEHEHE. L'uN vIeNt DeS pOmPiErS, l'AuTrE dE mOi. HIIIIHIHIHI.")
          print("VaS-tU pLeUrEr DaNs LeS jUpOnS dEs PoMpIeRs ? Ou CoNtInUeR l'AvEnTuRe AvEc MoI ? HAHAHAHAHAH. ")
          PARESSE = input('Choisissez "lui" ou "les pompiers" ')

          while PARESSE != "les pompiers" and PARESSE != "lui" :
                    PARESSE = input('ERREUR : Choisissez "lui" ou "les pompiers" ')

          if PARESSE == "les pompiers" :
                    print("TsS tSs TsS... La FaCiLiTé... Tu As FaIt Le ChOiX dE lA PARESSE... AAAAAAH")
                    print("Un gaz envahit la pièce, vous êtes asphyxié et vous mourrez.")
                    print("YOU LOSE.")

          else :
                    print("HAHAHAH AuDaCiEuX ! J'aImE çA ! PoUr Te RéCoMpEnSeR vOiLà UnE éNiGmEs :")
                    print("On PaSsE nOtRe ViE à EsSaYeR dE lE tUeR, mAiS eN vAiN cAr Il FiNiT tOuJoUrS pAr NoUs AvOiR.")
                    print("2 objets vous sont jetés, tous les 2 semblent être reliés à quelque chose.") 
                    print("Il y a une branche de figuier et une montre. Lequel voulez-vous choisir ?")
                    TWIST = input('Choisissez "la montre" ou "la branche" ')

                    while TWIST != "la montre" and TWIST != "la branche" :
                         TWIST = input('ERREUR : Choisissez "la montre" ou "la branche" ')

                    if TWIST == "la montre" :
                         print("CeLuI qU'oN nE cEsSe D'eSsAyEr De TuEr... LE TEMPS ! ZzzZZz")
                         print("Tu As ChOiSiS lA mOnTrE ! A cHaCuN sOn PaSsE tEmPs...")
                         print("La montre est en fait relié à une bombe à retardement. Vous devez couper un fil blanc ou fil noir")
                         print("AlOrS ? qUeL fIl VaS-tU cOuPeR ? lE bLaNc ? Ou Le NoIr ? HEHEHEH")
                         COULEUR = input('Choisissez "le blanc" ou "le noir" ')

                         while COULEUR != "le blanc" and COULEUR != "le noir" : 
                              COULEUR = input('ERREUR : Choisissez "le blanc" ou "le noir" ')

                         if COULEUR == "le blanc" :
                              print("Tu As DoNc ChOiSiS dE tE sEpArEr De Ta PuReTé...")
                              print("AiNsI sOiT-iL, vA !")
                              print("La bombe semble désamorcée, la lumière s'allume, vous êtes sur la scène d'un cirque et la cage se lève.") 
                              print("Vous êtes applaudi par une foule de ClOwNs et des billets vous tombent dessus.")                                   
                              print("PrOfiTe De La ViE qUe Tu As ChOiSiS HAHAHAHAH")
                              print("...")
                              print("En sortant du cirque, vous vous retrouvez devant un château, où des servants vous accueillent. ")
                              print("Ils vous apprennent le décès de votre famille entière suite à un incendie. ")
                              print("The End.")
                         else :
                              print("BrAvO, jE nE pEnSaIs PaS qUe Tu ArRiVeRaIs JuSqU'iCi. ")
                              print("La bombe semble désactivée. La lumière s'allume, vous êtes sur la scène d'un cirque et la cage se lève.")
                              print("Le cirque est totalement vide.")
                              print("En sortant du cirque, vous vous retrouvez devant votre maison, mais en feu. ")
                              print("Votre famille a eu le temps de sortir et vous courrez les retrouver")
                              print("The End.")
                    else :
                         print("La BrAnChE dE fIgUiEr ! cOnNaIs-Tu SeUlEmEnT sA sYmBoLiQuE ?")
                         print("En ToUt CaS, fElIcItAtIoNs ! Tu N'aS pAs EtE tEnTé PaR lA qUêTe VaInE dE l'AsSaSsInAt Du TeMpS !")
                         print("Tu As PaSsE tOuTeS lEs EpReUvEs AvEc BrIo !!! HOHOHO")
                         print("")
                         print("La branche était reliée à un interrupteur, la lumière s'allume, vous êtes sur la scène d'un cirque et la cage se lève.")
                         print("Les gradins sont remplis de Clowns")                             
                         print("Un clown s'approche de vous calmement : ")
                         print("")
                         print("Je m'appelle Georges. Enchanté " + nom)
                         print("C'est moi qui dirige la Secte Des Clowns, mais il semblerait que j'ai trouvé mon successeur.")
                         print("Tu peux accepter de me succéder, ou bien refuser et ainsi je dissoudrai cette Secte")
                         LAST = input('Choisissez "accepter" ou "refuser" ')

                         while LAST != "accepter" and LAST != "refuser" :
                              LAST = input('ERREUR : Choisissez "accepter" ou "refuser" ')

                         if LAST == "accepter" :
                              print("Les clowns vous applaudissent tous.")
                              print("Merci à toi " + nom )
                              print("Tu as maintenant 1000 clowns à ton service, puisses-tu faire bon usage de ta nouvelle influence.")
                              print("")
                              print("3 years later.")
                              print("")
                              print("JOURNAL TELEVISE")
                              print(nom + " est notre nouveau Président ! Gloire à " + nom + ".")
                              MESURE = input(nom + ", bonjour, quelle sera votre première mesure ? ")
                              print("Excellent ! Vive la nouvelle Rirepublique. ")
                              print("")
                              print("The End.")
                         else :
                              print("Les clowns se mettent tous à pleurer, y compris Georges. ")
                              print("La liberté, c'est ton droit le plus fondamental et nous le respecterons.")
                              print("")
                              print("3 years later.")
                              print("")
                              print("JOURNAL TELEVISE")
                              age3 = age + 3
                              print("Bonsoir, aujourd'hui nous accueillons " + nom + ", " + str(age3) + " ans, qui va nous parler de son tout nouveau film.")
                              OPINION = input("Tout d'abord, que pensez-vous de votre propre film ? ")
                              print("Merci pour ces premiers retours en exclusivité !")
                              print("")
                              print("The End.")

                         


