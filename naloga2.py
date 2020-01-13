a=int(input("Vnesite število 1: "))
b=int(input("Vnesite število 2: "))
c=int(input("Vnesite število 3: "))

if a<b and a<c:
    print (a, "je najmanjše število.")

if b<c and b<a:
    print(b, "je najmanjše število.")

if c<b and c<a:
    print(c, "je najmanjše število.")

if a > b and a > c:
    print(a, "je največje število.")

if b > c and b > a:
    print(b, "je največje število.")

if c > b and c > a:
    print(c, "je največje število.")
