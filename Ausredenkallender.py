# Projektname: Ausredenkallender 
# Ersteller: Tobias Weber
# Version 0.9. 17.01.2020

import random
import time

#def Ausredengenerator():


"""-----E-----"""


""" Um Ausreden einzulesen, bitte eine Ausreden.txt Datei im selben Verzeichnis erstellen. 
    Ausreden hineinschreiben und nach jeder Ausrede mit Enter bestätigen bzw. eine neue Zeile anfangen.
    (Bei .rtf gibt es anscheinend Probleme mit der Codierung, deshalb bitte nur .txt verwenden.)
"""


def Data_import():
    # Textatei öffnen und Textblock für Textblock in Liste einlesen
    Data_source = open('Ausreden.txt', 'r')
    return(Data_source)
    Data_source.close()


def Today():
    return int(time.strftime("%d", time.localtime()))


def User_input():
    Input = input()
    return(Input)


"""-----A-----"""


def Data_output(Data):
    print("Die Ausrede des heutigen Tages lautet: " + Data)


def all_used():
    print("Das waren alle Ausreden, bitte starten Sie das Programm neu")


def Contine_or_not():
    print("Möchten Sie eine neue Ausrede generieren? Y/N")
    return(User_input())


"""-----V-----"""


Data_list = []  # Liste um Ausreden zu speichern

for i in Data_import():  # Für jeden Datensatz
    Data_list.append(i)  # Datensatz in Liste speichern
    #Datei wieder schließen


def Random(Data_list):  # Es muss kein Wert mitgegeben werden. Diese Fuktion generiert nur eine Ausrede

    Data = random.choice(Data_list)  # Zufällige Ausrede auswählen
    return(Data)


def Output_Data(Day, Data_used, Data_list):

    Data = Random(Data_list)

    if Day == Today():  # wenn es noch der selbe Tag ist:
        if Data in Data_used:  # Prüfen, ob Ausrede schon vorkam
            if len(Data_list) == len(Data_used):  # Prüfen, ob schon alle Ausreden vorkamen
                all_used()
                pass
            else:
                # Falls Ausrede schon vorkam, neu starten
                Output_Data(Day, Data_used, Data_list)
        else:
            Data_output(Data)
            #print("Die Ausrede des heutigen Tages lautet: " + Datensatz)      #Ausrede ausgeben
            # Ausrede zur Liste der heute schon vorgekommenen Ausreden hinzufügen
            Data_used.append(Data)
            Contine_or_not()
            if Input == "y" or "Y":  # Soll eine weitere Ausrede generiert werden?
                # neu starten
                Output_Data(Day, Data_used, Data_list), Data_used
            else:
                pass
    else:
        Day = Today()  # wenn es ein anderer Tag ist:
        Data_used = []  # Ausredenliste der schon vorgekommenen Ausreden reseten
        Output_Data(Day, Data_used, Data_list)  # neu starten



Data_used = []  # Erster durchlauf vor Schleife
Day = Today()
Data = Random(Data_list)  # Zufällige Ausrede auswählen

Data_output(Data)
# Ausreden, die schon vorkamen in Liste der vorgekommenen Ausreden
Data_used.append(Data)
Input = Contine_or_not()
if Input == "y" or Input == "Y":  # Soll eine weitere Ausrede generiert werden?
    # Funktion aufrufen - Diese dient als Schleife
    Output_Data(Day, Data_used, Data_list)
else:
    pass  # Program beenden

#Ausredengenerator()
