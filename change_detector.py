#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import os
from binary import *
from detector import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sequence', dest='sequence', type=str)
    parser.add_argument('--endian', dest='endian', type=str, default='little', choices=['big', 'little'])
    parser.add_argument('--bits', dest='bits', type=int, default=8, choices=[8, 16, 32, 64])
    parser.add_argument('pattern', nargs='*')

    return parser.parse_args()

args = parse_args()

bits = args.bits
file_paths = args.pattern
endian = endians[args.endian]
expects = list(args.sequence)

def examine_word(current_word, old_word, i, j):
    return  (   
                (expects[i] == 'l' and current_word < old_word) or 
                (expects[i] == 'g' and current_word > old_word) or
                (expects[i] == 'd' and current_word != old_word) or
                (expects[i] == 's' and current_word == old_word)
            ) 

matches = detect(file_paths, bits, endian, examine_word)

for match in matches:    
    print(hex(match) + ":", end = '')

    for i, file_path in enumerate(file_paths[1:]):
        contents = Path(file_path).read_bytes()

        print("\t" + hex(get_word(contents, match, bits, endian)) , end = '')

    print()

