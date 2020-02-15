# Projektname: Ausredenkallender
# Entwicklungsschritt: Klassenbibliothek 
# Ersteller: Tobias Weber
# Version 0.16 mit Klassen 16.02.2020

import myFunctions #Importiert Funktionen


Data_used = [] #Liste für schon benutzte Daten
Data_list = myFunctions.Data_import() #Liste mit Daten von Funktion holen
Day = myFunctions.Today() #Momentanen Tag ermitteln
counter = 1 


def Main_Programm(Data_list, Day, Data_used, counter):
       
    Data = myFunctions.Random(Data_list)

    if Day == myFunctions.Today():  #Wenn noch der selbe Tag ist
        if counter != "False":  #UND Der Counter noch nicht überschritten wurde
            if myFunctions.Redundanz_Überprüfung(Data, Data_used, Data_list) != "Alle Daten kamen schon vor": #UND Nicht schon alle Daten vorkamen
                if myFunctions.Redundanz_Überprüfung(Data, Data_used, Data_list) != False:                    #UND die momentanen Daten nicht schon vorkamen
                    print("Die Ausrede des heutigen Tages lautet: " + Data) #Daten ausgeben
                    Data_used.append(Data)                                  #Daten zur Liste benutzter Daten hinzufügen
                    counter = myFunctions.Aufrufe_counter(counter)          #counter erhöhen /// FUNKTION WIRKLICH NÖTIG? ///

                    print("Möchten Sie eine neue Ausrede generieren? Y/N")
                    Input = input()
                    if Input == "y" or Input == "Y":  # Soll eine weitere Ausrede generiert werden?
                        Main_Programm(Data_list, Day, Data_used, counter)   #Rekursion durch erneutes Aufrufen der Funktion
                else:
                    Main_Programm(Data_list, Day, Data_used, counter)   #Programm neu Aufrufen, um neue Datei auszuwählen
            else:
                print("Alle Daten kamen schon vor - bitte starten Sie das Programm neu")
        else:
            print("Die gesetzte Aufrufsanzahl wurde ereicht")
            #irgendwas machen
    else:
        Day =  myFunctions.Today()                          #Tag aktualisieren
        Data_used = []                                      #Liste benutzter Daten leeren
        counter = 1                                         #Counter zurücksetzen
        Main_Programm(Data_list, Day, Data_used, counter)   #Programm neu starten

Main_Programm(Data_list, Day, Data_used, counter)


"""
Day = int(time.strftime("%d", time.localtime())) #Momentanen Tag ermitteln


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
"""