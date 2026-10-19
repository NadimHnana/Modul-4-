navn = input("Hva heter du? ")
print("Hei,", navn)
# samme hilden med f-strengen
print(f"Hei, {navn}!")

#spørre om alderen og sjekke datatypen
alder = input("Hvor gammel er du? ")
print(type(alder))

# i steg 5 så prøvde jeg å legge sammen en streng og et tall, noe som ikke er tillatt.
#  Derfor fikk jeg en feilmelding som sa "TypeError: can only concatenate str (not "int") to str". 
# Dette skjedde fordi input() alltid returnerer en streng, og jeg prøvde å legge til et tall til denne strengen uten å konvertere den først.

# her gjør jeg det om til et heltall 
alder = int(alder)
print(type(alder))
print(f"Neste år blir du {alder + 1} år!")

# utviddelse av høyde i meter 
hoyde = input("Hvor høy er du i meter? ")
hoyde = float(hoyde)
print(f"Du er {hoyde} meter høy.") # legger til en f-streng sånn at det blir lettere å lese og sette inn variabler i teksten

# Hva svarte type() på alderen før du brukte int()? Hvorfor tror du input() gir deg akkurat denne datatypen?
# den svartre meg med: TypeError: can only concatenate str (not "int") to str. jeg tror den svarer sånn på grunn av at input() 
# alltid returnerer en streng (string) uansett hva brukeren skriver inn. Derfor må vi konvertere strengen til en int for å kunne 
# gjøre matematiske operasjoner med den.

# Hva klaget Python på i steg 5? Beskriv feilmeldingen med egne ord.
# Python klaget på at du prøvde å legge sammen en streng og et tall, noe som ikke er tillatt. 
# Feilmeldingen var "TypeError: can only concatenate str (not "int") to str".

# Sammenlign print("Hei,", navn) og f-strengen. Hvilken synes du er lettest å lese? Hva skjer med mellomrommene i de to variantene?
# Jeg synes f-strengen er lettest å lese fordi den gjør det tydeligere hva som skal settes inn i teksten. I print("Hei,", navn) 
# må man huske å legge til et komma for å få et mellomrom, mens i f-strengen håndteres mellomrommet automatisk når man skriver teksten.

# Hva tror du skjer hvis brukeren skriver tretti i stedet for 30? Prøv.
# Hvis brukeren skriver "tretti" i stedet for "30", vil programmet kaste en ValueError når det prøver å konvertere strengen "tretti" til en int. 
# Dette skjer fordi "tretti" ikke er et gyldig tall som kan konverteres til en int.