# Projektname: Ausredenkallender 
# Ersteller: Tobias Weber
# Version 0.9. 17.01.2020

import random
import time



Ausreden_Liste = []
""" Um Ausreden einzulesen, bitte eine Ausreden.txt Datei im selben Verzeichnis erstellen. 
    Ausreden hineinschreiben und nach jeder Ausrede mit Enter bestätigen bzw. eine neue Zeile anfangen.
    (Bei .rtf gibt es anscheinend Probleme mit der Codierung, deshalb bitte nur .txt verwenden.)
"""

datei = open('Ausreden.txt','r') #Textatei öffnen und Textblock für Textblock in Liste einlesen
for i in datei:
    Ausreden_Liste.append(i)

datei.close()

    

def Zufallsgenerator(Ausreden_Liste): #Es muss kein Wert mitgegeben werden. Diese Fuktion generiert nur eine Ausrede

    Ausrede = random.choice(Ausreden_Liste) #Zufällige Ausrede auswählen
    return(Ausrede)
      


def Ausrede_ausgeben(Day, Ausreden_heute, Ausreden_Liste):

    Ausrede = Zufallsgenerator(Ausreden_Liste)
    Today = int (time.strftime("%d", time.localtime()))  #Momentanen Tag ermitteln

    if Day == Today:                                               #wenn es noch der selbe Tag ist:
        if Ausrede in Ausreden_heute:                              #Prüfen, ob Ausrede schon vorkam
            if len(Ausreden_Liste) == len(Ausreden_heute):         #Prüfen, ob schon alle Ausreden vorkamen
                print("Das waren alle Ausreden, bitte starten Sie das Programm neu")
                pass
            else:
                Ausrede_ausgeben(Day, Ausreden_heute, Ausreden_Liste) # Falls Ausrede schon vorkam, neu starten
        else:    
            print("Die Ausrede des heutigen Tages lautet: " + Ausrede)      #Ausrede ausgeben 
            Ausreden_heute.append(Ausrede)                                  #Ausrede zur Liste der heute schon vorgekommenen Ausreden hinzufügen
            print("Möchten Sie eine neue Ausrede generieren? Y/N")
            Input = input()              
            if Input == "y" or "Y":      #Soll eine weitere Ausrede generiert werden?
                Ausrede_ausgeben(Day, Ausreden_heute, Ausreden_Liste), Ausreden_heute #neu starten
            else:
                pass
    else:
        Day = Today                                                     #wenn es ein anderer Tag ist:
        Ausreden_heute = []                                             #Ausredenliste der schon vorgekommenen Ausreden reseten
        Ausrede_ausgeben(Day, Ausreden_heute, Ausreden_Liste)                                           #neu starten

            
            
Ausreden_heute = []                                 #Erster durchlauf vor Schleife
Day = int (time.strftime("%d", time.localtime()))   #Tag ermitteln
Ausrede = Zufallsgenerator(Ausreden_Liste)          #Zufällige Ausrede auswählen

print("Die Ausrede des heutigen Tages lautet: " + Ausrede)         
Ausreden_heute.append(Ausrede)                      #Ausreden, die schon vorkamen in Liste der vorgekommenen Ausreden
print("Möchten Sie eine neue Ausrede generieren? Y/N")
Input = input()
if Input == "y" or Input == "Y":      #Soll eine weitere Ausrede generiert werden?
    Ausrede_ausgeben(Day, Ausreden_heute, Ausreden_Liste)   #Funktion aufrufen - Diese dient als Schleife
else:
    pass            #Program beenden
