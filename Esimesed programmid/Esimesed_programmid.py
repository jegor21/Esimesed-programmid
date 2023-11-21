#Ülesanne 1
print("Ülesanne 1")
nimi = input("Sisesta oma nimi: ")
print("Tere tulemast, " + nimi + "!")
print(" ")
#Ülesanne 2
print("Ülesanne 2")



print(" ")
#Ülesanne 2.1
print("Ülesanne 2.1")



print(" ")

#Ülesanne 2.2
print("Ülesanne 2.2")



print(" ")

#Ülesanne 3
print("Ülesanne 3")

print(" ")

#Ülesanne 4
print("Ülesanne 4")



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