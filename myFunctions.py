#########################################
# Funktions-Library                     #
# Version 0.1                           #
# Ersteller: Tobias Weber               #
#########################################

import random
import time

#---------- E ----------#

# Textatei öffnen und Textblock für Textblock in Liste einlesen
""" Um Ausreden einzulesen, bitte eine Ausreden.txt Datei im selben Verzeichnis erstellen. 
Ausreden hineinschreiben und nach jeder Ausrede mit Enter bestätigen bzw. eine neue Zeile anfangen.
(Bei .rtf gibt es anscheinend Probleme mit der Codierung, deshalb bitte nur .txt verwenden.)
"""
def Data_import():
    Data_list = []

    Data_source = open('Ausreden.txt', 'r')
    for i in Data_source:  # Für jeden Datensatz
        Data_list.append(i)  # Datensatz in Liste speichern
    Data_source.close()
    return(Data_list)
    


Data_import()

# Gibt den momentanen Tag als Integer zurück
def Today():
    return int(time.strftime("%d", time.localtime()))



"""/// NIcht benötigt? ///
# Wartet auf eine Nutzereingabe und gibt diese zurück
def User_input():
    Input = input()
    return(Input)



# Abfragen, ob eine neue Ausrede generiert werden soll 
def Contine_or_not():
    print("Möchten Sie eine neue Ausrede generieren? Y/N")
    return(User_input())
"""
#--------- A ----------#

# Gibt über die Konsole aus, dass alle Daten aufgebraucht sind 
def all_used():
    print("Das waren alle Daten, bitte starten Sie das Programm neu")

#---------- V ----------#

def Random(Data_list):  # Es muss kein Wert mitgegeben werden. Diese Fuktion wählt nur eine der Daten

    Data = random.choice(Data_list)  # Zufällige Daten auswählen
    return(Data)



# Überprüft, ob es noch der selbe Tag ist  - Ja = True - Nein = False
def Datumskontrolle(Day):
    if Day == int(time.strftime("%d", time.localtime())):
        return True
    else:
        return False



#
def Data_were_used():
    Data_used.append(Data) # Momentane Daten werden zur Liste der benutzten Daten hinzugefügt



# Prüft, ob Daten schon vorkamen
''' 
Drei mögliche Rückgabewerte:
True - Daten kamen noch nicht vor
False - Daten kamen schon vor, aber es gibt Daten, die noch nicht vorkamen
"Alle Daten kamen schon vor" - Selbsterklärend
'''
def Redundanz_Überprüfung(Data, Data_used, Data_list):
    if Data in Data_used:  # Prüfen, ob daten schon vorkam
        if len(Data_list) == len(Data_used):  # Prüfen, ob schon alle Daten vorkamen
            return("Alle Daten kamen schon vor")
        else:
            return False # Momentane Daten kam vor, aber es gibt Daten, die noch nicht vorkamen
    else:
        return True



#Counter, wie oft funktion aufgerufen wurde - gibt ab überschreitung des Maximums "False" aus / Als String da False equals 0 und es so eine endlosrekursion gebe
def Aufrufe_counter(counter):
        if counter < 99: #Hier Zahl für MAX Aufrufe eingeben
            counter += 1
            return counter
        else: 
            return "False"
        