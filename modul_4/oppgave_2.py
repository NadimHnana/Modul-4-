# Oppgave 2 - Gammel nok 
aldersgrense = 18
alder = int(input("Hvor gammel er du? "))

# Forventning: 17 år er ikke gammel nok.
# Forventning: 18 år er gammel nok.
# Forventning: 19 år er gammel nok.

if alder >= aldersgrense:
	print(f"Du er {alder} år, og gammel nok.")
else:
	print(f"Du er {alder} år, og ikke gammel nok.")

print("Takk for at du sjekket!")
