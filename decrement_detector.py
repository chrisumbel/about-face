#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import os
from binary import *
from detector import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', nargs='*')
    parser.add_argument('--endian', dest='endian', type=str, default='little', choices=['big', 'little'])
    parser.add_argument('--bits', dest='bits', type=int, default=8, choices=[8, 16, 32, 64])
    parser.add_argument('--ltgt', dest='ltgt', type=str, default='lt', choices=['lt', 'gt'])
    parser.add_argument('--strict', action='store_true')

    return parser.parse_args()

args = parse_args()

bits = args.bits
gt = args.ltgt == 'gt'
endian = endians[args.endian]
file_paths = args.pattern

def examine_word(current_word, old_word, i, j):
    return (
        (
            (
                args.strict and (
                    (gt and (current_word == old_word + 1)) or
                    (not gt and (current_word == old_word - 1))
                )
            ) or
            (
                not args.strict and (
                    (gt and (current_word > old_word)) or
                    (not gt and (current_word < old_word))
                )
            )
        )
    )

matches = detect(file_paths, bits, endian, examine_word)

contents_first = Path(file_paths[0]).read_bytes()
contents_last = contents_old = Path(file_paths[-1]).read_bytes()

for match in matches:    
    print(hex(match) + "\t" + hex(get_word(contents_first, match, bits, endian)) + "\t" + hex(get_word(contents_last, match, bits, endian)))
