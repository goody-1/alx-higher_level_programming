#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_string = roman_string.upper()
    rom_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    numeric_rep = [1, 5, 10, 50, 100, 500, 1000]

    zipped_numerals = list(zip(rom_numerals, numeric_rep))
    sum = 0

    for i in range(len(roman_string)):
        for j in range(len(zipped_numerals)):
            # check if char is in zipped_numerals and
            if (roman_string[i] == zipped_numerals[j][0]):
                # if its not the last char and index of the char in the
                # rom_numerals list is less than index of next char subtract
                # associated value from sum
                if (i < len(roman_string) - 1) and (rom_numerals.index(
                        roman_string[i]) < rom_numerals.index(
                            roman_string[i + 1])):
                    sum -= zipped_numerals[j][1]
                else:
                    sum += zipped_numerals[j][1]

    return sum
