def parni_broj(prosljedjeni_parametar):
    broj=2
    while broj < prosljedjeni_parametar:
        yield broj
        broj+=2
for i in parni_broj(29):
    print(i)

def neparni_broj(prosljedjeni_parametar):
    broj=1

    while broj < prosljedjeni_parametar:
        yield broj
        broj+=2
for i in neparni_broj(37):
    print(i)
