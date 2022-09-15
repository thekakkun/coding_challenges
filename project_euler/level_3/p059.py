import os
import time
from itertools import product

start_time = time.time()


def p059(encrypted_message):
    """XOR decryption

    Problem 59

    Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
    """

    password = find_pass(encrypted_message)
    ascii_message = []

    for i, code in enumerate(encrypted_message):
        ascii_message.append(code ^ [ord(x)
                                     for x in password][i % len(password)])

    return sum(ascii_message)


def find_pass(encrypted_message):
    CONTROL_CHARACTERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                          15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 127]

    LETTERS = list(range(ord('A'), ord('Z'))) + list(range(ord('a'), ord('z')))
    PASSWORD_LENGTH = 3

    letter_count_history = {}

    for password in product(range(ord('a'), ord('z') + 1), repeat=PASSWORD_LENGTH):
        message = []

        for i, code in enumerate(encrypted_message):
            character = code ^ password[i % PASSWORD_LENGTH]

            if character in CONTROL_CHARACTERS:
                break
            else:
                message.append(character)

        else:
            letter_count_history[''.join([chr(x) for x in password])] = len(
                [x for x in message if x in LETTERS])

    max_character_count = max(letter_count_history.values())

    likely_password = list(letter_count_history.keys())[list(
        letter_count_history.values()).index(max_character_count)]

    return likely_password


with open(os.path.join('level_3', 'p059_cipher.txt'), 'r') as f:
    encrypted_message = [int(x) for x in f.readlines()[0].split(',')]
    print(p059(encrypted_message))
print('Completed in', time.time() - start_time, 'seconds')
