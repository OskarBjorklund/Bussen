# ------------------------------- Information --------------------------------- #

"""
Titel: Bussen
Författare: Oskar Björklund, Teeshk Nader, Siavash Razmjooei, Matteus Liss
Datum: 9/11 2021 till 1/19 2022
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
    förefternamn = json.load(f) #Laddar .json filen

kvinnligt_förnamn = förefternamn["namn_kvinna"] #Använder sig av nyckeln "namn_kvinna" för att komma åt dictionary i .json filen
manligt_förnamn = förefternamn["namn_man"] #Använder sig av nyckeln "namn_man" för att komma åt dictionary i .json filen
efternamn = förefternamn["efternamn"] #Använder sig av nyckeln "efternamn" för att komma åt dictionary i .json filen


passagerare = [] #Listan där alla objekt lagras

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():

    """ 
    Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn som tar hänsyn till kön, et efternamn, en ålder och ett kön, samt metoder för att returnera
    alternativt modifiera respektive attribut. 
    """

    #Objektens attributer
    def __init__(self, namn, efternamn, kön, ålder):
        self.namn = namn
        self.efternamn = efternamn
        self.kön = kön
        self.ålder = ålder
        

    #Strängrepresentation av objektet.
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
# ------------------------- Funktionsdefinitioner ---------------------------- #


def clear_screen():
    os.system("cls || clear") #Används för rensa skärmen

def plockaUpp(antal_passagerare):
    '''
    Lägger till en ny person i bussen.
    Slumpat antal passagerare stiger på bussen. Könet på personen slumpas 50/50, utifrån könet får personen
    ett kvinnligt eller manligt namn, namnen hämtas från en slumpmässig plats i en lista, (manligt_förnamn eller kvinnligt_förnamn).
    På samma sätt slumpas ett efternamn som hämtas från en lista. Därefter slumpas en ålder. Förnamn, efternamn och ålder
    lagras i en varibel som sedan används för att skapa ett objekt men dessa egenskaper. Objektet lagras sedan
    i listan (passagerare)
    '''

    for i in range(antal_passagerare):
        if rand.random() >= 0.5: #Manligt kön
            förnamn_i_funktion = manligt_förnamn[rand.randint(0, len(manligt_förnamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            ålder = rand.randint(0, 110)
            en_man = Person(förnamn_i_funktion, efternamn_i_funktion, "Han", ålder)
            passagerare.append(en_man)
        else: #Kvinnligt kön
            förnamn_i_funktion = kvinnligt_förnamn[rand.randint(0, len(kvinnligt_förnamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            ålder = rand.randint(0, 110)
            en_kvinna = Person(förnamn_i_funktion, efternamn_i_funktion, "Hon", ålder)
            passagerare.append(en_kvinna)

def gåAv(antal_passagerare):
    '''
    Avlägsnar en person från bussen.
    Beroende på slumpat antal_passagerare som går av bussen körs for-loopen så många gånger.
    I for-loopen tas en slumpmässig passagerare bort från listan (passagerare).
    '''

    for i in range(antal_passagerare):
            passagerare.pop(rand.randint(0, len(passagerare)-1))
    
def skrivUt():
    '''
    Skriver ut alla passagerare på bussen.
    enumerate, inbyggd funktion i Python. enumerate ger index i listan samt det som befinner sig på platsen.
    '''

    for i, person in enumerate(passagerare):
        print(f"{i+1}. {person}") #Skriver ut siffror framför passagerare, alltså, 1,2,3... 


def sammanlagdÅlder():
    '''
    Returnerar summan av alla passagerares åldrar. Alltså
    adderas alla objekts ålder attribute i listan passagerare.
    '''

    return sum([person.ålder for person in passagerare])   


def medelÅlder():
    '''
    Returnerar medelåldern på passagerarna i bussen.
    Alltså adderas alla objekts ålder attribute i listan passagerare.
    Sedan divideras den sammanlagda åldern med längden på listan.
    Värdet avrundas.
    '''

    return round(sum([person.ålder for person in passagerare])/len(passagerare))
    
def äldst():
    '''
    Skriver ut personen/personerna som är äldst på bussen.
    Funktionen skapar först en tom lista, den högsta åldern tas fram ifrån listan (passagerare)
    Sedan kör en for-loop genom listan (passagerare), om ett objekt har attribute ålder likadant värde så appendas
    det objektet till listan som funktionen skapade i början.

    Sedan upprepas samma procedur som på funktionen skrivUt():
    '''
    äldsta_personer = []
    äldsta_person = max([person.ålder for person in passagerare]) #Objektet med högst värde på sin attribute ålder.

    for person in passagerare:
        if person.ålder == äldsta_person:
            äldsta_personer.append(person)
    
    for i, person in enumerate(äldsta_personer):
        print(f"{i+1}. {person}")

def busSort():
    '''
    Sorterar bussen, antingen efter namn, efternamn i bokstavsordning, kön eller efter ålder.
    Kan också ovända listan (passagerare).
    
    Menyn är uppbyggd på samma sätt som main() menyn.

    Beroende på ditt val så sorteras listan på olika sätt genom attributerna.
    '''

    sorteringsVal = ""

    clear_screen()

    while sorteringsVal != "q": #Bryter loopen med "q"

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
            passagerare.sort(key=lambda x: x.namn) #Sorterar efter namn
            clear_screen()
            print("Bussen är nu sorterad efter förnamn") 
        elif sorteringsVal == "2":
            passagerare.sort(key=lambda x: x.efternamn) #Sorterar efter efternamn
            clear_screen()
            print("Bussen är nu sorterad efter efternamn")
        elif sorteringsVal == "3":
            passagerare.sort(key=lambda x: x.ålder) #Sorterar efter ålder
            clear_screen()
            print("Bussen är nu sorterad efter åldern")
        elif sorteringsVal == "4":
            passagerare.sort(key=lambda x: x.kön) #Sorterar efter kön
            clear_screen()
            print("Bussen är nu sorterad efter kön")
        elif sorteringsVal == "5":
            passagerare.reverse() #Vänder listan
            clear_screen()
            print("Passagerare har nu blivit omvända")
        elif sorteringsVal != "q": #Återgår till huvudmenyn
            clear_screen()
            print("Felaktig inmatning.")
    clear_screen()

def hittaPassagerare(åldersSpann1, åldersSpann2):
    '''
    Skriver ut en lista på alla passagerare inom ett visst åldersspann.
    Först skapar funktionen en tom lista där personer med åldern inom intervallet som angets i funktionens parameter 
    läggs till i listan.

    Därefter upprepas samma procedur igen som skriver ut listan
    '''

    ålderSpann_personer = []
    for person in passagerare:
        if person.ålder >= åldersSpann1 and person.ålder <= åldersSpann2:
            ålderSpann_personer.append(person)
    
    print("")

    if len(ålderSpann_personer) == 0: #Om det inte finns några passagerare inom intervallet
        print(f"Det finns inga passagerare mellan {åldersSpann1} år och {åldersSpann2} år.")
    else:
        for i, person in enumerate(ålderSpann_personer):
            print(f"{i+1}. {person}")

def peta(petad):
    '''
    Petar på en passagerare. Skriver ut en text som beskriver passagerarens 
    reaktion när denne blir petad på. Passagerarens reaktion beror helt på attributerna ålder och kön.
    '''
    
    petad_i_funktion = passagerare[petad]

    if petad_i_funktion.ålder <= 4:
        print("Gogo gaga")

    elif petad_i_funktion.ålder <= 12:
        if petad_i_funktion.kön == "Han":
            print("Bort från mig din pedofil!")
        else:
            print("HJÄLP!!! Jag blir antastad av busschauffören!!!")

    elif petad_i_funktion.ålder <= 18:
        if petad_i_funktion.kön == "Han":
            print("Yelaen Tarekhek!!")  # Damn your entire history
        else:
            print("Din knullbulle, vad håller du på med!?")

    elif petad_i_funktion.ålder <= 26:
        if petad_i_funktion.kön == "Han":
            print("Vad tror du att du håller på med?")
        else:
            print("Jag ringer polisen!!!")

    elif petad_i_funktion.ålder <= 30:
        if petad_i_funktion.kön == "Han":
            print("Papi vad gör du?")
        else:
            print("Bort med tassarna ditt äckel")

    elif petad_i_funktion.ålder <= 55:
        if petad_i_funktion.kön == "Han":
            print("Sluta peta på mig din idiot!")
        else:
            print("Vad gör du din gubbstrut?")

    elif petad_i_funktion.ålder <= 80:
        if petad_i_funktion.kön == "Han":
            print("Ojj, hej ditt lilla kex, du kanske vill hjälpa mig hem?") 
        else:
            print("Vad håller du på med?")

    elif petad_i_funktion.ålder <= 90:
        if petad_i_funktion.kön == "Han":
            print("Jag kanske har Alzheimers men jag har åtminstone inte Alzheimers")
        else:
            print("Har du problem med gammla män!")

    elif petad_i_funktion.ålder <= 110:
        if petad_i_funktion.kön == "Han":
            print("Nämen du din jävel, nu ska du lyssna, fasiken vad du ska lyssna. Så gör man inte här i denna foster land. Nu ska du fannnn få käft i dig jävla ouppfostrad... Fy fan, tappade andan.")
        else:
            print(f"Snälla låta en gammal dam vara, jag är faktiskt {petad_i_funktion.ålder} år.")

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    '''
    Huvudmenyn, här väljer du bland alla olika alternativ.
    '''
    menyVal = ""

    clear_screen()

    while menyVal != "q": #Loopen bryts om användaren väljer "q"

        print(
        """
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
        """)
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

            antal = rand.randint(0, 10) #Slumpmässigt antal passagerare stiger på
            lediga_platser = 25 - len(passagerare) #Lediga platser på bussen, maximalt antal tillåtna platser = 25

            if lediga_platser > 0: 
                if lediga_platser >= antal: #Om antalet lediga platser är större än antalet som stiger på så får alla plats
                    antal_påstigna = antal
                    clear_screen()
                    print(f"{antal_påstigna} ny(a) passagerare steg ombord bussen.")
                else:
                    antal_påstigna = lediga_platser #Annars får endast vissa personer plats
                    clear_screen()
                    print(f"Det fanns {antal} passagerare på busshålsplatsen men endast {antal_påstigna} kunde stiga på.")
                plockaUpp(antal_påstigna) #Funktionen plockaUpp anropas sedan med antalet som får plats som argument
            else: #Om bussen är full får inga gå gå
                clear_screen()
                print("Bussen är för närvarande full.")

        elif menyVal == "2":
            if len(passagerare) > 10: #Slumpar fram hur många passagerare som går av
                antal = rand.randint(0, 10)
                gåAv(antal) #Funktionen gåAv anropas med slumat antal som argument
                clear_screen()
                print(f"{antal} passagerare steg av bussen.")
            elif len(passagerare) >= 1:
                antal = rand.randint(0, len(passagerare)) #Ser till att inte det går av fler passagerare än vad som befinner sig i bussen
                gåAv(antal)
                clear_screen()
                print(f"{antal} passagerare steg av bussen.")
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

        elif menyVal == "3":
            if len(passagerare)>= 1:
                clear_screen() 
                skrivUt() #Anropar funktionen skrivUt
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

        elif menyVal == "4":
            if len(passagerare)>= 1:
                clear_screen() 
                print(f" Den sammanlagda åldern hos de {len(passagerare)} passagerare är {sammanlagdÅlder()}.") 
                #Skriver ut den sammlagda åldern genom att anropa funktionen sammlagdÅlder
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen, alltså blir den sammanlagda åldern noll.")

        elif menyVal == "5":
            if len(passagerare)>= 1:
                clear_screen()
                print(f" Medelåldern hos de {len(passagerare)} passagerare är {medelÅlder()}.")
                #Skriver ut den sammlagda åldern genom att anropa funktionen medelÅlder
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen, alltså blir den medelåldern noll.")

        elif menyVal == "6":
            if len(passagerare)>= 1:
                clear_screen()
                äldst() #Anropas funktionen äldst
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

        elif menyVal == "7":
            if len(passagerare)>= 1:
                clear_screen()
                busSort() #Anropar funktionen busSort
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

        elif menyVal == "8":
            if len(passagerare)>= 1:
                clear_screen()

                while True:
                    åldersSpann1 = input("Ange lägsta åldern på passagerare du vill hitta -> ")
                    if åldersSpann1.isdigit(): #Kollar om inmatningen är rättlig, om den är rättlig går programmet vidare
                        break
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")

                while True:
                    åldersSpann2 = input("Ange högsta åldern på passagerare du vill hitta -> ")
                    if åldersSpann2.isdigit(): #Kollar om inmatningen är rättlig, om den är rättlig går programmet vidare
                        break    
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")

                clear_screen()
                hittaPassagerare(int(åldersSpann1), int(åldersSpann2)) #Anropar funktionen hittaPassagerare med två argument

                input(
                    """

                    Tryck på valfri knapp för att fortsätta...
                    """)

                clear_screen()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

        elif menyVal == "9":
            if len(passagerare)>= 1:
                clear_screen()

                while True:

                    clear_screen()

                    skrivUt() #Anropar funktionen  skrivUt så att man kan se vilka passagerare man kan välja mellan

                    petad_passagerare = input(
                    """

                    Välj en passagerare att peta på. -> 

                    """)

                    if petad_passagerare.isdigit(): #Kollar om sin inmatning är rättlig
                        if int(petad_passagerare) > 0: #Ser till att man inte väljer ett värde under noll
                            if int(petad_passagerare) <= len(passagerare): #Ser till att man håller sig inom listans längd
                                clear_screen()
                                peta(int(petad_passagerare)-1) #Anropar funktionen peta med ett korrekligt argument

                                input(
                                """

                                Tryck på valfri knapp för att fortsätta...
                                """)

                                clear_screen()

                                break #Bryter loopen så att man kommer tillbaka till huvudmenyn
                            else:
                                clear_screen()
                                print("Felaktig inmatning.")
                                input(
                                """

                                Tryck på valfri knapp för att fortsätta...
                                """)
                        else: 
                            clear_screen()
                            print("Felaktig inmatning.")
                            input(
                            """

                            Tryck på valfri knapp för att fortsätta...
                            """)
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")
                        input(
                        """

                            Tryck på valfri knapp för att fortsätta...
                        """)
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                
        elif menyVal != "q":
            clear_screen()
            print("Felaktig inmatning.")

main() #Anropar main funktionen så att programmet kan starta