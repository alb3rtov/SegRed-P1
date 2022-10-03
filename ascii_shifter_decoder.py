#!/usr/bin/python3

import os.path

''' Read file of encrypted text '''
def read_file(path_file):
    file = open(path_file, mode='r')
    text = file.read()
    file.close()
    bytes_object = bytes.fromhex(text)
    string = bytes_object.decode()
    return string

''' Function converts plaintext to ciphertext using key '''
def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result

path_file = input("Enter encrypted text file path: ")

if (os.path.exists(path_file)):
    shift = input("Enter shift: ")
    key = int(shift)

    text = read_file(path_file)
    result = ascii_shift(key, text)
    print("Result: ", result)
    print()
else:
    print(path_file + " file not found.")
