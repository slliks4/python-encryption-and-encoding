import sys
import encryption 

# DO NOT CHANGE ANY CODE IN THIS FILE

# DO NOT SUBMIT THIS FILE WITH YOUR ASSIGNMENT

# test 1: charToBin
print("\n1. Testing charToBin()")
print("Input:    'P'")
print("Expected: 0 0 1 1 1 1")
print("Actual:  ", *encryption.charToBin('P'))

# test 2: binToChar
print("\n2. Testing binToChar()")
print("Input:    [1,0,1,1,1,0]")
print("Expected: u")
print("Actual:  ", encryption.binToChar([1,0,1,1,1,0]))

# test 3: strToBin
print("\n3. Testing strToBin()")
print("Input:    Camera")
print("Expected: 0 0 0 0 1 0 0 1 1 0 1 0 1 0 0 1 1 0 0 1 1 1 1 0 1 0 1 0 1 1 0 1 1 0 1 0")
print("Actual:  ", *encryption.strToBin("Camera"))

# test 4: binToStr
print("\n4. Testing binToStr()")
print("Input:    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]")
print("Expected: pirate")
print("Actual:  ", encryption.binToStr([1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]))

# test 5: generatePad()
print("\n5. Testing generatePad(), with:")
print(">seed = [1,1,0,0,0,1,1,0,0,1,0]")
print(">k = 9")
print(">length = 20\n")
pad = encryption.generatePad([1,1,0,0,0,1,1,0,0,1,0], 9, 20)
print("Expected: 1 1 0 1 1 1 1 1 0 0 1 1 0 1 0 0 0 1 1 1")
print("Actual:  ", *pad)

# test 6: encrypt()
print("\n6. Testing encrypt()")
plain = "IdLoveToStayHereAndBeNormalButItsJustSoOverrated"
encrypted = encryption.encrypt(plain, [1,0,1,0,0,1,0,0,1,0], 8)
decrypted = encryption.encrypt(encrypted, [1,0,1,0,0,1,0,0,1,0], 8)

print("Input:    ", decrypted)
print("Expected:  F2n9bUBl5BPGNMm1sypLMADHzuvTjGk4YD8hG+96lMmA24qX")
print("Actual:   ", encrypted)
print("Decrypted:", decrypted, "\n\n")
