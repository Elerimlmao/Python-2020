n = input("Vnesite število za računanje vsote:")
n = int (n)
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("Vsota prvih ", n, "števil je: ", sum )
