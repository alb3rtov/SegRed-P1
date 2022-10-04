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

    return list_strings, len(packets)

''' Function converts plaintext to ciphertext using key '''
def ascii_shift(key, text, filename, num_packets):
    decoded_file_name = filename + "-decoded.txt" 
    
    for strings in text:
        result = ""
        for letter in strings:
            ascii = ( ord(letter) - key - 32 ) % 94 + 32
            result = result + chr(ascii)
        f = open(decoded_file_name, "a")
        f.write(result + '\n\n')
        f.close()
    
    print()
    if os.path.exists(decoded_file_name):
        print("Finished. Generated " + decoded_file_name + " file. " + num_packets + " packets have been read.")
    else:
        print("An error ocurred during generating decoded file.")
    print()

''' Main function '''
def main():
    if (len(sys.argv) == 3):
        if os.path.exists(sys.argv[1]) and sys.argv[2].isdigit():
            key = int(sys.argv[2])
            text, num_packets = read_packets(sys.argv[1]);
            ascii_shift(key, text, sys.argv[1].split('.')[0], str(num_packets))
        else:
            print(sys.argv[1] + " file not found or shift number incorrect")
    else:
        print()
        print("Usage: ascii_shifter_decoder.py <encoded_text_file> <shift number>");
        print()

if __name__ == "__main__":
    main()
