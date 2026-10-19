# Oppgave 4 — Billettluka

alder = 25 
er_student = True 
har_medlemskort = False 

alder < 12 or alder > 67


er_styudent and alder < 30 
#denne blir usann siden er_student er sann, men alder < 30 er usann. Derfor blir hele uttrykket usant.

not har_medlemskort 
# Denne her er usann siden har medlemskort er usann

er_student and har_medlemskort 
#denne blir usann på grunn at har_medlemskort er usann, og er_student er sann. Derfor blir hele uttrykket usant.

er_student or har_medlemskort 
# denne er sann siden er_student er sann, og har_medlemskort er usann så en av de er sann derfor blir hele uttrykket sann

not er_student or alder < 30
#denne er sann siden er_student er sann og not endrer alt false til true men skjer ikke i denne casen mens alder > 30 er usann, og derfor blir utrykket sann.

# Del 2 — Billettluka

alder = int(input("Hvor gammel er du? "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

if alder < 12 or alder > 67:
	print(f"Billetten er gratis.")
elif er_student and alder < 30:
	print(f"Billetten koster 50 kr.")
else:
	print(f"Billetten koster 120 kr.")

if not er_student:
	print("Tips: Studenter under 30 år får rabatt.")

# Forventede priser:
# 8 år, ikke student: gratis
# 70 år, ikke student: gratis
# 22 år, student: 50 kr
# 35 år, student: 120 kr
# 25 år, ikke student: 120 kr

# Utvidelse: Uten .lower() blir "Ja" ikke lik "ja", fordi sammenligning av
# tekst skiller mellom store og små bokstaver. .lower() gjør teksten liten.

# and krever at begge vilkårene er sanne. or krever at minst ett vilkår er sant.
# En 35-årig student betaler 120 kr fordi studentrabatten gjelder under 30.
# not snur en sann verdi til usann og omvendt. Uten not kan sjekken skrives
# som: if er_student == False:
# En student på 70 år får gratis billett. Gratisregelen står først og slår inn;
# her ville rekkefølgen også gitt gratis, siden studentrabatten ikke gjelder over 67.

