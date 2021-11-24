# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare:
Datum:
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand
import json
import os
# ------------------------------ Listor --------------------------------------- #

path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(path,"förefternamn.json")) as f:
    förefternamn = json.load(f)

förnamn = förefternamn["namn"]
efternamn = förefternamn["efternamn"]

passagerare = []

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn, efternamn, ålder):
        self.namn = namn
        self.efternamn = efternamn
        self.ålder = ålder

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn} {self.efternamn}. Hen är {self.ålder} år gammal."
    
    # Setters
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn
    
    def setEfternamn(self, nyttEfternamn):
        self.namn = nyttEfternamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    # Getters
    def getNamn(self):
        return self.namn
    
    def getEfternamn(self):
        return self.efternamn

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plockaUpp(antal_passagerare):
    for i in range(antal_passagerare):
        förnamn_i_funktion = förnamn[rand.randint(0, 100)]
        efternamn_i_funktion = efternamn[rand.randint(0, 100)]
        ålder = rand.randint(0, 110)
        en_person = Person(förnamn_i_funktion, efternamn_i_funktion, ålder)
        passagerare.append(en_person)

# Avlägsnar en person från bussen.
def gåAv(antal_passagerare):
    for i in range(antal_passagerare):
        passagerare.pop(rand.randint(0, len(passagerare)-1))
    

# Listar alla passagerare på bussen.
def skrivUt():
    for i, person in enumerate(passagerare):
        print(f"{i+1}. {person}")

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder():
    return sum([person.ålder for person in passagerare])      
   

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder():
    return

# Skriver ut personen som är äldst på bussen.
def äldst():
    return

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    return

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare(åldersSpann):
    return

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            antal = rand.randint(0, 10)
            plockaUpp(antal)
            print(f"{antal} ny(a) passagerare steg ombord bussen.")
        elif menyVal == "2":
            if len(passagerare) > 10:
                antal = rand.randint(0, 10)
                gåAv(antal)
                print(f"{antal} passagerare steg av bussen.")
            elif len(passagerare) >= 1:
                antal = rand.randint(0, len(passagerare))
                gåAv(antal)
                print(f"{antal} passagerare steg av bussen.")
            else:
                print("Inga passagerare befinner sig på bussen.")
        elif menyVal == "3":
            if len(passagerare) >= 1:
                skrivUt()
            else:
                print("Inga passagerare befinner sig på bussen.")
        elif menyVal == "4":
            print(f" Den sammanlagda åldern hos de {len(passagerare)} passagerare är {sammanlagdÅlder()}.")
        elif menyVal == "5":
            pass
        elif menyVal == "6":
            pass
        elif menyVal == "7":
            pass
        elif menyVal == "8":
            pass

print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()