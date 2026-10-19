riktig_brukernavn = 'michael'
riktig_passord = 'python123'
print('Skriv inn brukernavn og passord for å logge inn: ')

brukernavn = input('Brukernavn: ')
passord = input('passord: ')
if brukernavn == riktig_brukernavn and passord == riktig_passord:
    print(f'Velkommen, {brukernavn}!')
elif brukernavn == riktig_brukernavn:
    print('Feil passord.')
else:
    print('Ukjent bruker.')

svar = input('Ønsker du å prøve på nytt? (ja/nei) ')
