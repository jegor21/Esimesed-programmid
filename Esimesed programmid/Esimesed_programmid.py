import math
#Ülesanne 1
print("Ülesanne 1")
nimi = input("Sisesta oma nimi: ")
print("Tere tulemast, " + nimi + "!")
print(" ")



#Ülesanne 2
print("Ülesanne 2")
result_sulgudes = 3 + 8 / (4 - 2) * 4 #Sulgudes
print("Sulgudes: ", result_sulgudes)
result_ilma = 3 + 8 / 4 - 2 * 4 #Ilma
print("Ilma: ", result_ilma)
result_muud = (3 + 8) / 4 - 2 * 4 #Muud variant
print("Muud variant: ", result_muud)
print(" ")



#Ülesanne 2.1
print("Ülesanne 2.1")
ringi_raadius = 3
ruudu_kulje_pikkus =round( 2 * ringi_raadius,2) # Ruudu külje pikkus
ruudu_pindala = ruudu_kulje_pikkus ** 2 # Ruudu pindala
ruudu_umbermoet = round(4 * ruudu_kulje_pikkus,2) # Ruudu ümbermõõt
ringi_pindala = round(math.pi * ringi_raadius ** 2,2)
ringi_umbermoet = round(2 * math.pi * ringi_raadius,2) # Ringi ümbermõõt
print(f"Ruudu pindala: {ruudu_pindala}")
print(f"Ruudu ümbermõõt: {ruudu_umbermoet}")
print(f"Ringi pindala: {ringi_pindala}")
print(f"Ringi ümbermõõt: {ringi_umbermoet}")
print(" ")

#Ülesanne 2.2
print("Ülesanne 2.2")
maa_raadius_km = 6378  # Maa raadius
mündi_läbimõõt_cm = 2.5  # 2-eurose mündi läbimõõt sentimeetrites
pi_ligikaudne = 3.14159  # Ligikaudne väärtus pi jaoks

ümbermõõt_cm = 2 * pi_ligikaudne * maa_raadius_km * 1000  # Ümbermõõt sentimeetrites
mündi_arv = ümbermõõt_cm / mündi_läbimõõt_cm

print(f"Ümbermõõt on {ümbermõõt_cm:.2f} sentimeetrit.")
print(f"2-euroseid münte umbes {int(mündi_arv)} münti.")
print(" ")

#Ülesanne 3
print("Ülesanne 3")
kill = "kill"
koll = "koll"
killadi = "killadi"

result = f"{kill}-{koll} {kill}-{koll} {killadi}-{koll} {kill}-{koll} {kill}-{koll} {killadi}-{koll} {kill}-{koll} {kill}-{koll} {kill}-{koll}"
print(result)


print(" ")

#Ülesanne 4
print("Ülesanne 4")
laul1="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?
"""
print(laul1)

laul2="""
Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(laul2)

print(" ")

#Ülesanne 5
print("Ülesanne 5")
print("Nüüd leiame ristküliku ümbermõõdu!")
arv1=int(input("Kirjutage ühe külje pikkus: "))
arv2=int(input("Kirjutage ühe külje pikkus: "))
P=arv1*2+arv2*2
print("Tulemus on "+str(P))
print(" ")

#Ülesanne 6
print("Ülesanne 6")
print("Kütusekulu arvutamine")
kütus=int(input("Kui palju kütust täideti(liitrites)? "))
läbitudkm=int(input("Mitu kilomeetrid läbitud? "))
keskmine=round(kütus/läbitudkm*100,1)
print("Tulemus on "+str(keskmine))
print(" ")

#Ülesanne 7
print("Ülesanne 7")
print("Rulluisutaja keskmine kiirus on 29,9km/h")
M=int(input("Kui kaugele jõuab M minutiga? "))
R=round(29.9*M/1000,1)
print("Tulemus on "+str(R)+" km")
print(" ")

#Ülesanne 8
print("Ülesanne 8")
print("Ajateisendus")
aeg = int(input("Sisesta aeg minutites: "))
tunnid = aeg // 60
minutid = aeg % 60
print(f"Vastus: {tunnid}:{minutid}")