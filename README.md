# Ascii shifter decoder
First you have to generate PCAP file using Wireshark.

## Requirements
In order to run the script it is necessary to install the scapy module to handle `pcap` package capture files.
```
$ pip install scapy
```
## Launch
Use this command to run the script:
```
$ ./ascii_shifter_decoder.py <capture.pcap> <shift number>
```
