import re

regex1 = "[A-Z]"
regex2 = "\d"
regex3 = "\W"

unos = input("Unesite lozinku:")

duljina = len(unos)
if duljina < 8:
   print("Lozinka mora sadrzavati bar 8 znakova")

veliko = re.findall(regex1, unos)
if not veliko:
   print("Niste unijeli veliko slovo")

broj = re.findall(regex2, unos)
if not broj:
   print("Niste unijeli broj")
   
znak = re.findall(regex3, unos)
if not znak:
   print("Niste unijeli specijalni znak")

if veliko and broj and znak and duljina>=8:
   print("Ispravna lozinka.")
