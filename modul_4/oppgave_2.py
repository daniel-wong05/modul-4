aldersgrense = 18
alder = int(input("Hvor gammel er du? "))

if alder >= aldersgrense:
    print(f"Du er {alder} år, og gammel nok.")

else:
    print(f"Du er {alder} år, og ikke gammel nok.")

print("Takk for at du sjekket!")

# 1. når jeg fjernet innrykket fikk jeg feil melding
# fordi python trenger innrykk etter og ha brukt if statements
# så etter ett if statement må man bruke innryk for at python skal forstå

# 2."Takk for at du sjekket" ble skrevet ut 
# uansett alder fordi print()står ikke sammen med if og else

# 3. alder >= aldergrense sjekker om alderen er 18 eller over
# fordi at i den første linjen lagret jeg tallet 18 i aldersgrense variabelen
# svaret når vi bruker alder >= aldersgrense er enten riktig eller galt
# og if statements bruker det til og velge hvilken meldning som skrives ut

# 4. >= er riktig fordi 18 også er gammel nok, fordi det betyr større en eller lik
# men hvis jeg bare hadde brukt > må alderen være over 18 og ikke like fordi
# jeg ikke bruker =

