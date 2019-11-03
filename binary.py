from enum import Enum

endians = Enum('Endian', 'big little')

def get_word(contents, pos, bits, endian):
    val = 0
    bytes_in_word = int(bits / 8)

    for i in range(0, bytes_in_word):
        if(len(contents) > pos + i):
            byte = contents[pos + i]

            if endian == endians.big:
                byte <<= ((bytes_in_word - 1 - i) * 8)
            else:
                val <<= (i * 8)

            val |= byte
        else:
            return 0

    return val
