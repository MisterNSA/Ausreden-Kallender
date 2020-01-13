# Projektname: Ausredenkallender 
# Ersteller: Tobias Weber
# Version 0.1 28.09.2019


'''
-Zufallsgenerator erstellen, der zufällig eine Ausrede auswählt (Am besten eigene Funktion "Zufallsgenerator", der Wert per return zurück gibt)
-Funktion(?), die erkennt, ob die Ausrede für diesen Tag atomar ist oder schon mehrfach vorgekommen ist / Einmaligkeit gewährleisten
-Integration des Kalenders seitens Betriebssystem um festzustellen, ob ein neuer Tag ist
'''
import random
import time

#def Ausredenkalender():
    #mit einer while-Schleife gewährleisten, dass das Programm so lange arbeitet, bis der nutzer es schließt
    #Button zum neu generieren






def Zufallsgenerator():


    Ausrede_1 = "Koronaler Massenauswurf"
    Ausrede_2 = "Zu niedrige Tacktfrequenz"
    Ausrede_3 = "Zu hohe Speicherauslastung"
    Ausrede_4 = "Problem wegen nicht eingestellter Interrupts an PCI"
    Ausrede_5 = "Fehlerhafte Sektoren im NAS-System"
    Ausrede_6 = "Die neuen Treiber haben Kompatibilitätsprobleme"
    Ausrede_7 = "Die Speicherresidenten Programme haben sich gegenseitig abgeschossen"
    Ausrede_8 = "Das verträgt sich nicht mit der Terminalemulation"
    Ausrede_9 = "Anti-Virus-Programm klassifiziert Windows Update als Virus"
    Ausrede_10 = "Platte am Server wurde falsch gepolt angeschlossen und dreht jetzt falsch herum"
    Ausrede_11 = "Momentan telefonieren zu viele Leute, weshalb das Netzwerk ausgelastet ist"
    Ausrede_12 = "Aufgrund zu hoher Stromrechnungen laufen die Geräte im Energiesparmodus und sind dadurch langsamer"
    Ausrede_13 = "Ständige Telefonanrufe an die Hotline verhindern, dass Schäden behoben werden können" 
    Ausrede_14 = "Auf Ihrem Rechner ist kein RTFM-Device installiert"
    Ausrede_15 = "Die Leistung wird für das aktuelle Systembackup benötigt"
    Ausrede_16 = "Auf ihrem Rechner war /dev/brain nach /dev/null gelinkt"
    Ausrede_17 = "Die Teritäre Hintergrundstrahlung ist zu hoch für die neuen (RAMs,ROMs,CPUs,etc.)"
    Ausrede_18 = "Auf allen Rechnern laufen Service-Pack-Updates"
    Ausrede_19 = "Borg-Prozess im Linux-Cluster assimiliert alle Systemprozesse"
    Ausrede_20 = "Beim Dual-Prozessor-Server streiten die CPUs um internen Cache-Speicher"
    Ausrede_21 = "Ihr Computer hat die Bits nicht zurückgegeben, die er vom Internet bekommen hat"
    Ausrede_22 = "Fehler 40 sorgt für Fehlerhafte Prozessausführung "
    Ausrede_23 = "Die CPU braucht eine Rekalibrierung"
    Ausrede_24 = "Schleife in der Schleife des redundanten Loopback"
    Ausrede_25 = "Wir haben nicht genug Lizenzen"
    Ausrede_26 = "Der Prozess ist nicht ISO 9000 konform"
    Ausrede_27 = "Unser ISP hat (Switching-, Routing-, SMDS-, etc.) Probleme"
    Ausrede_28 = "Die root-Nameserver sind nicht mehr synchronisiert"
    Ausrede_29 = "Exzessiver Hochspannungsschutz verhindert eine schnellere Übertragung der Daten"
    Ausrede_30 = "Der digitale Manipulator überschreitet seine Geschwindigkeitparameter"
    Ausrede_31 = "Jemand hat Zwergpakete gebroadcastet und der Router wusste nicht mit ihnen umzugehen"
    Ausrede_32 = "Quanten-Decoherenzen"
    Ausrede_33 = "Ich würde ihnen gerne helfen, aber die Chefetage hat mir einen Übergestellten Auftrag gegeben"
    Ausrede_34 = "Es findet gleich eine Besprechung bezüglich der Businessrelevanten-Actionpoints statt"
    Ausrede_35 = "Mal wieder ein Klassicher BNC (brain not connected) Fehler"
    Ausrede_36 = "Veraltete Hardware"
    Ausrede_37 = "Es kam zu einem OSI-Layer 8 Fehler"



    Ausreden_Liste = [
        Ausrede_1,
        Ausrede_2,
        Ausrede_3,
        Ausrede_4,
        Ausrede_5,
        Ausrede_6,
        Ausrede_7,
        Ausrede_8,
        Ausrede_9,
        Ausrede_10,
        Ausrede_11,
        Ausrede_12,
        Ausrede_13,
        Ausrede_14,
        Ausrede_15,
        Ausrede_16,
        Ausrede_17,
        Ausrede_18,
        Ausrede_19,
        Ausrede_20,
        Ausrede_21,
        Ausrede_22,
        Ausrede_23,
        Ausrede_24,
        Ausrede_25,
        Ausrede_26,
        Ausrede_27,
        Ausrede_28,
        Ausrede_29,
        Ausrede_30,
        Ausrede_31,
        Ausrede_32,
        Ausrede_33,
        Ausrede_34,
        Ausrede_35,
        Ausrede_36,
        Ausrede_37]

    Ausrede = random.choice(Ausreden_Liste)
    print ("\n Die Ausrede des Tages lautet - ", Ausrede)

Zufallsgenerator()  








''' VERSUCH FÜR MEHRFACHERKENNUNG UND VERHINDERUNG '''


def Datumserkennung():               #prüfen, ob noch der selbe Tag ist
    
    Ausreden_heute = [] 
    
    
    Day = 13 #nur zum testen
    Today = int (time.strftime("%d", time.localtime())).    #momentanen Tag erkennen

    if Day == Today:                                                    #wenn es noch der selbe Tag ist:
        print("Die Ausrede des heutigen Tages lautet: " + Ausrede)      #Ausrede ausgeben 
        Ausreden_heute.append(Ausrede)                                  #Ausrede zur Liste der heute schon vorgekommenen Ausreden hinzufügen

    else:
        Day = Today                                                     #wenn es ein anderer Tag ist:
        Ausreden_heute = []                                             #Ausredenliste der schon vorgekommenen Ausreden reseten



Datumserkennung()



    

    
    
    
    
    
    
''' VERSUCH 1
    try: # ***NOCH ZU ERLEDIGEN*** Wenn Versuch fehlschlägt weil alle Ausrede zum vermehrten Male vorkommt -> Except fehlermeldung
        if Tag = 1: # Wenn es der erste Tag ist dann:
            Tag_1.append(Ausrede) # Momentane Ausrede zur Liste der an Tag eins vorgekommenen hinzufügen
            if Tag_1.count(Ausrede)==1:   # Wenn die Ausrede in der Liste Tag eins zum ersten mal vorkommt
                print("Die Ausrede des heutigen Tages lautet: " + Ausrede)
            else: #Wenn Ausrede schon vorkam: 
                    # Neue Ausrede generieren und nochmal versuchen - Wie? - Keine Jumps vorhanden '''

''' VERSUCH 2
    while Tag = 1:
        Tag_1.append(Ausrede) # Momentane Ausrede zur Liste der an Tag eins vorgekommenen hinzufügen
            if Tag_1.count(Ausrede)==1:   # Wenn die Ausrede in der Liste Tag eins zum ersten mal vorkommt
                print("Die Ausrede des heutigen Tages lautet: " + Ausrede)
            else: #Wenn Ausrede schon vorkam: 
                    # Neue Ausrede generieren und nochmal versuchen - Wie? - Keine Jumps vorhanden '''
'''
