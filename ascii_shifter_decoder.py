#!/usr/bin/python3

from scapy.all import *

import os.path
import sys

''' Read all packet from capture file '''
def read_packets(path_file):

    packets = rdpcap(path_file)
    list_strings = []

    for packet in packets:
        if TCP in packet and packet[TCP].sport == 12345:
            if Raw in packet:
                string = ""
                raw_data = packet[Raw].load
                for c in raw_data:
                    if c > 31:
                        string = string + chr(c)
                list_strings.append(string)

    return list_strings

''' Function converts plaintext to ciphertext using key '''
def ascii_shift(key, text):
    
    for strings in text:
        result = ""
        for letter in strings:
            ascii = ( ord(letter) - key - 32 ) % 94 + 32
            result = result + chr(ascii)
        print(result)

''' Main function '''
def main():
    if (len(sys.argv) == 3):
        if os.path.exists(sys.argv[1]) and sys.argv[2].isdigit():
            key = int(sys.argv[2])
            text = read_packets(sys.argv[1]);
            ascii_shift(key, text)
        else:
            print(sys.argv[1] + " file not found or shift number incorrect")
    else:
        print()
        print("Usage: ascii_shifter_decoder.py <encoded_text_file> <shift number>");
        print()

if __name__ == "__main__":
    main()
