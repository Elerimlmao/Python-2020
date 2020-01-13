n = (int(input("Prosim vnesite čas v sekundah: ")))

h = int(n / 60)

m = int((n % 60) /60)

s1 = (n % 60) % 60

print(n, "sekund je =", h, "ur, ", m, "minut, ", s1, "sekund.")