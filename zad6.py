def rekurzivna_funkcija(s):
    if len(s) ==0:
        return s
    else:
        return rekurzivna_funkcija (s[1:])+s[0]

rez=rekurzivna_funkcija("programiranje")
print(rez)

