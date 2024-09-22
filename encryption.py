# encryption using a linear feedback shift register
import bindec

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
    two_dimensional_list = []
    for char in string:
        current_character = charToBin(char)
        two_dimensional_list.append(current_character)

    result = [element for sublist in two_dimensional_list for element in sublist]
    return result

# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    result = ""
    if len(b_list) % 6 == 0:
        two_dimensional_list = [b_list[i:i + 6] for i in range(0, len(b_list), 6)]
    for i in range(len(two_dimensional_list)):
        current_binary = binToChar(two_dimensional_list[i])
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
    return ''

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    message_bin = strToBin(message)  # Convert the message to binary (6 bits per char)
    lfsr_state = generatePad(seed, k, len(message_bin))  # Generate LFSR pad of the same length

    encrypted_bin = [message_bin[i] ^ lfsr_state[i] for i in range(len(message_bin))]  # XOR with LFSR pad

    encrypted_message = binToStr(encrypted_bin)  # Convert the binary result back to string
    return encrypted_message