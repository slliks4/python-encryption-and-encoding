# encryption using a linear feedback shift register
import bindec

# base64_chart = {
#     'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
#     'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
#     'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
#     'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
#     'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
#     'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
#     'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
#     'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
#     'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
#     'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
#     'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
#     's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
#     'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
#     '0': '110100', '1': '110101', '2': '110110', '3': '110111',
#     '4': '111000', '5': '111001', '6': '111010', '7': '111011',
#     '8': '111100', '9': '111101', '+': '111110', '/': '111111'
# }

# Base64 Chart
base64_chart = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]

# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c):
    global base64_chart
    if c in base64_chart:
        index = base64_chart.index(c)
        binary_representation = format(index, '06b')  # 6-bit binary representation
        return [int(bit) for bit in binary_representation]
    else:
        return []

# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b):
    binary_string = ''.join(map(str, b))
    decimal_value = int(binary_string, 2)

    global base64_chart  # Use the global keyword

    if 0 <= decimal_value < len(base64_chart):
        return base64_chart[decimal_value]
    else:
        return ''

# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(s):
    string = s.replace(' ','')
    result = []
    for char in string:
        current_character = charToBin(char)
        result.append(current_character)

    return result

# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    result = ""
    for i in range(len(b_list)):
        current_binary = binToChar(b_list[i])
        result += current_binary

    return result

# generates a sequence of pseudo-random numbers using Linear Feedback Shift Register (LFSR)
def generatePad(seed, k, length):
    pad = seed.copy()  # Initialize the seed with the given value
    seed_length = len(seed)

    for i in range(seed_length, length):
        feedback = pad[i - seed_length] ^ pad[i - k]  # XOR the feedback bits
        pad.append(feedback)

    return pad[:length]

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    encrypted_message = ""
    lfsr_state = generatePad(seed, k, len(message))

    for i in range(len(message)):
        char_bin = charToBin(message[i])
        encrypted_bin = [char_bin[j] ^ lfsr_state[i + j] for j in range(len(char_bin))] # XOR with LFSR output
        encrypted_char = binToChar(encrypted_bin)
        encrypted_message += encrypted_char

    return encrypted_message

plain = "IdLoveToStayHereAndBeNormalButItsJustSoOverrated"
seed = [1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
k = 8
encrypted = encrypt(plain, seed, k)
print("Expected:", "F2n9bUBl5BPGNMm1sypLMADHzuvTjGk4YD8hG+96lMmA24qX")
print("Encrypted:", encrypted)
