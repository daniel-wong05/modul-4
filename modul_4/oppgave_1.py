navn = input("Hva Heter du")
alder = input ("Hvor gammel er du?")
alder = int(alder)

print("Hei,", navn)
print(f"Hei, {navn}!")
print(type(alder))
print(alder + 1)

#    Refleksjon
# 1. type() svarte med str. altså string, som betyr at alderen var tekst.
#    Jeg tror det er fordi input() lagrer det brukeren skriver som tekst,
#    selv om man skriver et tall.
#
# 2. Python ga feilmelding fordi jeg prøve og legge sammen tekst og tall.
#    Python kan ikke legge sammen tekst og tall.
#
# 3. Jeg måtte bruke int() for og gjøre om alderen til et tall.
#
# 4. Jeg syns kansje at f-strengen er lettest og lese fordi teksten og
#    variablet står samlet i en string.
#    I den første varianten av oppgaven setter print() automatisk
#    mellomrom mellom teskten og variablen. men i f-strengen kan jeg selv
#    skrive mellomrommet det jeg vil hva det.
#
# 5. Jeg tror at hvis jeg skriver tretti og ikke selve tallet 30 får jeg
#    feilmelding fordi python ikke klarer og gjøre tekst om til tall med int()