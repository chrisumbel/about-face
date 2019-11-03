from pathlib import Path
from binary import *

def detect(file_paths, bits, endian, fun):
    bytes_per_word = bits // 8
    contents_old = contents_old = Path(file_paths[0]).read_bytes()
    size = len(contents_old)
    state = [True] * size

    for i, file_path in enumerate(file_paths[1:]):
        contents = Path(file_path).read_bytes()

        for j in range(0, size, bytes_per_word):
            state[j] = state[j] and fun(get_word(contents, j, bits, endian), get_word(contents_old, j, bits, endian), i, j)

        contents_old = contents

    return [i for i, x in enumerate(state) if x and i % bytes_per_word == 0]

