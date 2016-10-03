#-------------------------------------------------------------------------------
# Name:        Programmieren Lernen mit Tim Aufgabe 1
# Created:     04.03.2016

##Aufgabe: Gegeben sei eine Liste mit den Gewichten von 10 Corgies:
##(22, 23, 18, 31, 5, 9, 28, 28, 25, 12).
##Gebe fuer jeden Corgi der mehr als 27 Kilo wiegt aus:
##"xx kg - das ist selbst fuer einen Corgi zu dick!"
##Berechne das Gesamtgewicht aller Corgies. Verifiziere das durch Unit-Tests.
##Berechne das Durchschnittsgewicht aller Corgies. Verifiziere das durch Unit-Tests.
##Berechne die Summe und den Durchscnitt mit Hilfe von For/while Loops
##Teile alle Corgis in eine der folgenden Kategorien ein:
##Klein <10 Kilo
##Mittel >= 10 Kilo, < 20 Kilo
##Gross >= 20 Kilo
##Erstelle eine Liste in der die Kategorien stehen. Verifiziere das durch Unit-Tests.
##Bestimme das Gewicht des schwersten Corgis. Verifiziere das durch Unit-Tests.
#-------------------------------------------------------------------------------



## Fuer jeden Corgi ueber 27kg ausgeben, dass er zu dick ist
def PrintDickeCorgies(cutoff,liste):
    for Corgi in liste:
        if Corgi > cutoff:
            print(Corgi, "kg - das ist selbst fuer einen Corgi zu dick!")

## Urspruengliche Berechnung von Gesamtgewicht und Durchschnittsgewicht, ohne for/while loop
##def GesamtundDurchschnittsgewichtCorgies(liste):
##    Gesamtgewicht = sum(liste)
##    print("Alle Corgis zusammen wiegen", Gesamtgewicht, "Kilo.")
##    Durchschnittsgewicht = sum(liste)/len(liste)
##    print("Im Schnitt wiegen die Corgies", Durchschnittsgewicht, "Kilo")


## Gesamtgewicht und Durchschnittsgewicht aller Corgis berechnen
def GesamtgewichtLOOP(liste):
    GesamtgewichtLOOP = 0;
    for i in range (0, len(liste)):
        GesamtgewichtLOOP = GesamtgewichtLOOP + liste[i]
    return GesamtgewichtLOOP

def DurchschnittsgewichtLOOP(liste):
	if len(liste) == 0:
		return 0
	else:
		DurchschnittsgewichtCorgisLOOP = GesamtgewichtLOOP(liste) / len(liste)
		return DurchschnittsgewichtCorgisLOOP

## Corgis nach Gewicht in klein, mittel und gross, kategorisieren
def Corgikategorisierung(liste):
    KategorienListe = []
    for i in range(0, len(liste)):
        if liste[i] <=0:
			raise Exception("Ein echter Corgi wiegt mehr als 0 Kilo!")
        elif liste[i] <10:
            KategorienListe.append ("kleiner Corgi")
        elif liste[i] >= 10 and liste[i] <20:
            KategorienListe.append("mittlerer Corgi")
        else:
            KategorienListe.append("grosser Corgi")
    return KategorienListe

## Den dicksten Corgi bestimmen
def DicksterCorgi(liste):
	## Den dicksten Corgi bestimmen mit for Schleife
	for CorgiGewicht in liste:
	if CorgiGewicht >

    return max(liste)
	



def main(EingabeListe):
	PrintDickeCorgies(27,EingabeListe)
	## GesamtundDurchschnittsgewichtCorgies(EingabeListe)
	print("Alle Corgis zusammen wiegen", GesamtgewichtLOOP(EingabeListe), "Kilo.")
	print("Im Schnitt wiegen die Corgies", DurchschnittsgewichtLOOP(EingabeListe), "Kilo")
	print(Corgikategorisierung(EingabeListe))
	print("Der dickste Corgi wiegt", DicksterCorgi(EingabeListe), "Kilo.")

main([22, 23, 18, 31, 5, 9, 28, 28, 25, 12])


