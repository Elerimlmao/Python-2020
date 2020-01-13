#Program ki pretvori število dni v leto, teden in dan (uporabnik vnese
# število dni) npr. št.dni: 1329 - 3 leta, 33 tednov, 3 dni

n=int(input("Vnesite število dni: "))


leta = int(n / 365)

tedni = int((n % 365) /7)

dnevi = (n % 365) % 7

print("leta = ",leta, ", teden = ",tedni,", dan = ",dnevi)



