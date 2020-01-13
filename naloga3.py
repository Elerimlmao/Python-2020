import math
a = (int(input("Prosim vnesite 1. koordinato 1: ")))
b = (int(input("Prosim vnesite 1. koordinato 2: ")))
c = (int(input("Prosim vnesite 2. koordinato 1: ")))
d = (int(input("Prosim vnesite 2. koordinato 2: ")))


p1 = [a, b]
p2 = [c, d]

distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)