poeng = int(input("Hvor mange poeng fikk du?"))

if poeng >= 90:
    print("A")

elif poeng >= 80:
    print("B")   

elif poeng >= 60:
    print("C")

elif poeng >= 50:
    print("D")    

elif poeng >= 40:
    print("E")     

else:
    print("F")   

# 1. Når jeg snudde teksten i motsatt rekkefølge fikk jeg E når jeg skrev 95
# fordi python stopper ved den første betingelsen som er sann

# 2. da jeg byttet elif med if fikk jeg bokstavene i rekkefølge fra top til bunn
# det er fordi python sjekker ut if-statements hver for seg fordi jeg skrev 95 som
# har høyere verdi en alle poenggrense jeg har skrevet ned. 

# 3. else kjører hvis ingen av de andre sjekkene passer, dersom jeg skriver 40 poengs for eksempel
# skriver programmet F, dersom jeg skriver inn en høyere verdi finner programmet en annen bokstav/poeng karakter