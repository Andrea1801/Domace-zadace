tekst = "U računarstvu i informatici, regularni izraz (još i pravilni izraz, ispravni izraz[1] – često i engleske skraćenice regexp ili regex, u množini regexps, regexes ili regexen) je niz znakova koji opisuje druge nizove znakova (engl. string), u skladu s određenim sintaksnim pravilima. Prvenstvena svrha regularnog izraza je opisivaǌe uzorka za pretraživaǌe nizova znakova. Regularne izraze koriste mnogi uređivači teksta i pomoćni programi za pretragu i manipulaciju teksta ovisno o nekim uzorcima. Mnogi programski jezici podržavaju regularne izraze za manipulaciju stringovima. Na primjer, Perl i Tcl u svojoj sintaksi sadrže potrebne elemente za korišteǌe regularnih izraza. Skup pomoćnih programa (uključujući uređivač ed i filter grep) koji se standardno distribuira sa Unix distribucijama je znatno učinio na promociji i popularizaciji koncepta regularnih izraza."

tekst = tekst.lower()

slova = {}

for slovo in tekst:
    slova[slovo] = slova.get(slovo, 0) + 1

print(slova);

for eng in ["x", "y", "w"]:
    if (eng in slova):
    	print("Pojavljue se englesko slovo", eng)

for broj in range(10):
    if str(broj) in slova:
        print("Pojavljuje se broj", broj)

parovi = slova.items();
print(parovi)

for slovo, ponavljanja in parovi:
	print("Slovo:", slovo, "Ponavljanja:", ponavljanja)


