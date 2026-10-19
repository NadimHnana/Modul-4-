# Oppgave 3 — Karakterkalkulator
# forventningene ved å taste inn poeng: 95 gir A, 72 gir C, 40 git E og 12 git F 
poeng = int(input("Skriv inn antall poeng (0-100): "))
if poeng < 0 or poeng > 100:
    print("Feil: Poeng må være mellom 0 og 100.")
elif poeng >= 90:
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

# hvis det skulle ha vært at E-sjekkes først i kjeden med elif og 95 er det som er gyldig,
# blir da resultatet E: 95 
# Med riktig rekkefølge og separate if-setninger skriver 95 ut A, B, C, D og E, fordi flere betingelser er sanne.
# Ugyldige poeng må sjekkes før karaktergrensene.
#
# Refleksjon:
# Steg 4: 95 fikk E fordi E-sjekken ble nådd før sjekken for A.
# Steg 5: Separate if-setninger vurderes alle, mens en if/elif-kjede
# stopper etter den første betingelsen som er sann.
# B trenger bare poeng >= 80 fordi elif-kjeden allerede har utelukket
# poeng på 90 eller mer.
# else kjører når ingen av betingelsene i if/elif-kjeden er sanne.
