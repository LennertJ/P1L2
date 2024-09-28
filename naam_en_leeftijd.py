def naam_en_leeftijd():
    naam = input("Wat is jouw naam?")
    leeftijd = input("Wat is jouw leeftijd?")
    print("Jouw naam is", naam, "jouw leeftijd is", leeftijd,".")

naam_en_leeftijd()

def vraag_input(onderwerp):
    return input("Geef me een " + onderwerp + ": ")
