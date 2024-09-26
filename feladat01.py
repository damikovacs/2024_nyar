#1.,2. feladat#

'''
kerdes=input("Jó napod volt?")
if kerdes == "igen":
    print("Örülök neki!")
elif kerdes == "nem":
    print("Sajnálom nemtudok mit kezdeni vele :)")
else:
    print("Sajnos nem értem a válaszodat!")
'''

#3. feladat#

'''
szam = int(input("Kérek egy számot: "))
if szam%2==0:
    print("Ez a szám páros!")
elif szam%2==1:
    print("Ez a szám páratlan!")
'''
#4.feladat#

'''
szam = 2
valasz = int(input("Gondoltam egy számra 1 és 5 között"))
if valasz == szam:
    print("Kitaláltad!")
elif valasz > szam:
    print("A szám amire gondoltam kisebb")
elif valasz < szam:
    print("A szám amire gondoltam nagyobb")
'''

#5.feladat#

'''
szam = int(input("Kérek egy számot: "))
if szam > 0 and szam%2 == 0:
    print("Ez a szám pozitív páros!")
elif szam < 0 and szam%2 == 1:
    print("Ez a szám negatív páratlan!")
elif szam > 0 and szam%2 == 1:
    print("Ez a szám pozitív páratlan!")
elif szam < 0 and szam%2 == 0:
    print("Ez a szám negatív páros!")
'''

#6.feladat#

'''
henrik=input("Jön Henrik ma kosarazni?")
hanna=input("És Hanna jön ma kosarazni?")
if henrik == "igen" and hanna == "igen":
    print("Mindketten jönnek kosarazni")
elif henrik == "igen" and hanna == "nem":
    print("Csak Henrik jön kosarazni")
elif henrik == "nem" and hanna == "igen":
    print("Csak Hanna jön kosarazni")
elif henrik == "nem" and hanna == "nem":
    print("Egyikük sem jön kosarazni")
else:
    print("Csak igennel és nemmel válaszolhatsz!")
'''

#7.feladat#

'''
szam=int(input("Kérek egy számot: "))
if szam%3 == 0 and szam%4 == 0:
    print("A szám osztható 3-al is és 4-el is")
elif szam%3 == 0:
    print("A szám csak 3-al osztható")
elif szam%4 == 0:
    print("A szám csak 4-el osztható")
else:
    print("Egyikkel sem osztható")
'''

#8.feladat#