# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare:
Datum:
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""

# -*- coding: latin-1 -*-

# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand
import json
import os
# ------------------------------ Listor --------------------------------------- #

path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(path,"förefternamn.json")) as f:
    förefternamn = json.load(f)

kvinnligt_förnamn = förefternamn["namn_kvinna"]
manligt_förnamn = förefternamn["namn_man"]
efternamn = förefternamn["efternamn"]

passagerare = []

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn, efternamn, kön, ålder):
        self.namn = namn
        self.efternamn = efternamn
        self.kön = kön
        self.ålder = ålder

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn} {self.efternamn}. {self.kön} är {self.ålder} år gammal."
    
    # Setters
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn
    
    def setEfternamn(self, nyttEfternamn):
        self.efternamn = nyttEfternamn

    def setKön(self, nyttKön):
        self.kön = nyttKön

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    # Getters
    def getNamn(self):
        return self.namn
    
    def getEfternamn(self):
        return self.efternamn
    
    def getKön(self):
        return self.kön

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plockaUpp(antal_passagerare):
    for i in range(antal_passagerare):
        if rand.random() >= 0.5:
            förnamn_i_funktion = manligt_förnamn[rand.randint(0, len(manligt_förnamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            ålder = rand.randint(0, 110)
            en_man = Person(förnamn_i_funktion, efternamn_i_funktion, "Han", ålder)
            passagerare.append(en_man)
        else:
            förnamn_i_funktion = kvinnligt_förnamn[rand.randint(0, len(kvinnligt_förnamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            ålder = rand.randint(0, 110)
            en_kvinna = Person(förnamn_i_funktion, efternamn_i_funktion, "Hon", ålder)
            passagerare.append(en_kvinna)

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
    return sum([person.ålder for person in passagerare])/len(passagerare)
    
# Skriver ut personen som är äldst på bussen.
def äldst():
    äldsta_personer = []
    äldsta_person = max([person.ålder for person in passagerare])
    for person in passagerare:
        if person.ålder == äldsta_person:
            äldsta_personer.append(person)
    
    for i, person in enumerate(äldsta_personer):
        print(f"{i+1}. {person}")
# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():

    sorteringsVal = ""

    while sorteringsVal != "q":

        print(
            """
                                            --- SORTERINGSMENY ---
                        Välkommen till sorteringsmenyn. Välj ett av alternativen nedan:
                1. Sortera efter förnamn                            2. Sortera efter efternamn
                3. Sortera efter ålder                              4. Sortera efter kön
                5. Omvänd passagerare                               q. Återgå till huvudmenyn
            ---------------------------------------------------------------------------------------
            """)
        
        sorteringsVal = input("-> ")

        if sorteringsVal == "1":
            passagerare.sort(key=lambda x: x.namn)
            print("Bussen är nu sorterad efter förnamn")
        elif sorteringsVal == "2":
            passagerare.sort(key=lambda x: x.efternamn)
            print("Bussen är nu sorterad efter efternamn")
        elif sorteringsVal == "3":
            passagerare.sort(key=lambda x: x.ålder)
            print("Bussen är nu sorterad efter åldern")
        elif sorteringsVal == "4":
            passagerare.sort(key=lambda x: x.kön)
            print("Bussen är nu sorterad efter kön")
        elif sorteringsVal == "5":
            passagerare.reverse()
            print("Passagerare har nu blivit omvända")

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare(åldersSpann):
    return

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(petad):
    petad_i_funktion = passagerare[petad-1]

    if petad_i_funktion.ålder <= 4:
        print("Gogo gaga")
    elif petad_i_funktion.ålder <= 12:
        if petad_i_funktion.kön == "Han":
            print("Bort från mig din pedofil!")
        else:
            print("HJÄLP!!! Jag blir antastad av busschauffören!!!")
    elif petad_i_funktion.ålder <= 18:
        if petad_i_funktion.kön == "Han":
            print("Yelaen Tarekhek") # Damn your entire history
        else:
            print("Din knullbulle, vad håller du på med!")
    elif petad_i_funktion.ålder <= 26:
        if petad_i_funktion.kön == "Han":
            print("Kille reaktion")
        else:
            print("Jag ringer polisen!!!")
    elif petad_i_funktion.ålder <= :
        if petad_i_funktion.kön == "Han":
            print("Kille reaktion")
        else:
            print("Tjej reaktion")
    elif petad_i_funktion.ålder <= ÅLDER:
        if petad_i_funktion.kön == "Han":
            print("Kille reaktion")
        else:
            print("Tjej reaktion")
    elif petad_i_funktion.ålder <= 80:
        if petad_i_funktion.kön == "Han":
            print("Ojj, hej ditt lilla kex, du kanske vill hjälpa mig hem?")
        else:
            print("Vad håller du på med?")
    elif petad_i_funktion.ålder <= 110:
        if petad_i_funktion.kön == "Han":
            print("Nämen vad i hela friden tror du att du håller på med unga man?")
        else:
            print(f"Snälla låta en gammal dam vara, jag är faktiskt {petad_i_funktion.ålder} år.")
        
    

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
            if len(passagerare) == 25:
                print("Bussen är för närvarande full.")
            elif antal + len(passagerare) > 24:
                for i in range(antal):
                    plockaUpp(1)
                    if len(passagerare) == 25:
                        print(f"Det fanns {antal} passagerare på busshålsplatsen men endast {i} kunde stiga på.")
                        break
                    else:
                        continue
            else:
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
            if len(passagerare)>= 1:
                skrivUt()
            else:
                print("Inga passagerare befinner sig på bussen.")
        elif menyVal == "4":
            print(f" Den sammanlagda åldern hos de {len(passagerare)} passagerare är {sammanlagdÅlder()}.")
        elif menyVal == "5":
            print(f" Medelåldern hos de {len(passagerare)} passagerare är {medelÅlder()}.")
        elif menyVal == "6":
            if len(passagerare)>= 1:
                äldst()
            else:
                print("Inga passagerare befinner sig på bussen.")
        elif menyVal == "7":
            busSort()
        elif menyVal == "8":
            pass
        elif menyVal == "9":
            if len(passagerare)>= 1:
                skrivUt()
                petad_passagerare = int(input("Välj en passagerare att peta på. -> "))
                peta(petad_passagerare)
            else:
                print("Inga passagerare befinner sig på bussen.")

print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()