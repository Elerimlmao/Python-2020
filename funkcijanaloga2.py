def zamenjava():
    x = int(input("Vnesi vrednost 1: "))
    y = int(input("Vnesi vrednost 2: "))
    temp = x
    x = y
    y = temp
    print('The value of x after swapping: {}'.format(x))
    print('The value of y after swapping: {}'.format(y))

zamenjava()
