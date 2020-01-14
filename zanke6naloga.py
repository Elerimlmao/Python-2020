list1=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
a=int(input("Vnesi nekaj: "))

while a>0:
    print(list1[a-1])
    a=int(input("Vnesi nekaj: "))
    if (a==0 or a>26):
        break


if a==0 or a>26:
    print("Your marj gay lmfao.")