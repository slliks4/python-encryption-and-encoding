# binary to decimal conversion
# @author mhatcher 2020

# DO NOT CHANGE ANY CODE IN THIS FILE

# DO NOT SUBMIT THIS FILE WITH YOUR ASSIGNMENT

# converts decimal to a binary list of at least n digits
def decToBin(x, n = 6):
    binary = []
    while (x > 0):
        binary.append(0 if x % 2 == 0 else 1)
        x = int(x / 2)
    while (len(binary) < n):
        binary.append(0)
    binary.reverse()
    return binary

# converts binary (in list format) to decimal
def binToDec(binary):
    dec = 0
    power = 1
    length = len(binary)
    for i in range(1, length + 1):
        dec += binary[length - i] * power
        power = power * 2
    return dec

