# Oppgave 5 — Finn feilen 2.0

riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = input("Hvor gammel er du? ")

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")

# riktig verson av alder
alder int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
else: 
    print("Du er ikke 18")

# dette er feilmeldingen jeg fikk: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# Hva var feilene? Beskriv dem kort med egne ord.
# 1. Hva var feilene?
# Programmet hadde fire feil.
# Første feil var at if-setningen brukte = i stedet for ==. Tegnet = brukes til å
# legge en verdi i en variabel, mens == sammenligner to verdier. Dette ga SyntaxError.
# Andre feil var at kolonet manglet etter if-linjen. Kolonet forteller Python at
# en kodeblokk starter. Dette ga også SyntaxError.
# Tredje feil var at print-linjen under else manglet innrykk. Python bruker innrykk
# for å vite hvilke linjer som hører til else. Dette ga IndentationError.
# Fjerde feil var en logisk feil: input() gir alltid en streng, så "18" ble
# sammenlignet med heltallet 18 og ble aldri likt. Jeg fikset det med int().


# Den siste feilen ga ingen feilmelding. Hvordan oppdaget du den? Hvorfor tror du Python ikke klager?
# siden input() alltid returnerer en streng, og alder ble sammenlignet med et heltall, 
# så ble aldri if-setningen sann. Python klager ikke fordi det er lovlig å sammenligne 
# en streng med et heltall, men de vil aldri være like.

# Hva er forskjellen på en syntaksfeil og en logisk feil? Hvilken av dem tror du er farligst i et ekte program?
# det er farligst med logisk feil siden det er de man som oftest ikke helt legger merke til, 
# og de kan føre til at programmet gjør noe annet enn det man hadde tenkt. tenker jeg da.

# Hvilke verdier er lurt å teste med for å finne logiske feil i et program som dette?
# jeg tror det er lurt å teste med verdier som er på grensen av hva som er tilstrekkelig i oppgaven, 
# for eksempel 17, 18 og 19.