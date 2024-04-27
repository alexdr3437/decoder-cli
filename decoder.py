#!/usr/bin/env python

import sys

from tire_daq_decoder.decoder import *
import sys

def usage():
    print(f"Usage: {sys.argv[0]} <data|gps|logs> <hex string>")

current_func = decode_packet

def parse_input(line):
    global  current_func
    if len(line) == 1:
        if line[0] == 'gps':
            print("now decoding gps")
            current_func = decode_gps
        elif line[0] == 'logs':
            print("now decoding logs")
            current_func = decode_log
        elif line[0] == 'data':
            print("now decoding data")
            current_func = decode_packet
        elif line[0] == 'q' or line[0] == '':
            sys.exit(0)
        else:
            print(current_func(line[0]))
    elif len(line) == 0:
        sys.exit(0)
    elif len(line) != 2:
        print("Error: Invalid input")
        print("")
        usage()
        sys.exit(1)
    else:
        message_type, line =  line[0], line[1]
        try:
            if (message_type == 'gps'):
                print(decode_gps(line))
            elif (message_type == 'logs'):
                print(decode_log(line))
            else:
                print(decode_packet(line))
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        parse_input(sys.argv[1:3])
    
    for inp in sys.stdin:
        line = inp.strip().split()
        parse_input(line)

