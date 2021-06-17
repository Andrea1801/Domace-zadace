imena = ["Ivan", "Ana", "Marko", "Toni", "Josip"]
prezimena = ["Ivancic", "Anic", "Maric", "Tomic", "Josipovic"]
godine = [20, 21, 23, 20, 25]

studenti= list(zip(imena, prezimena, godine))

for ime, prezime, godine in studenti:
    if godine > 21:
       print(ime, prezime)

