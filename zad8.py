ime=str(input("unesite ime"))
def vanjska(ime):
    def unutarnja():
        print("Pozdrav " + ime)
    return unutarnja
funkcija=vanjska(ime)

print(lambda ime: ("dobrodosao" + ime))
funkcija()

def treca_funkcija(vanjska):
    vanjska(ime)
treca_funkcija(vanjska)

    
