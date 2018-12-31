# python3
# This a a script for counting in a number system based on the alphabet.
# It loops through the numbers from start_value to stop_value and converts each number into a string
# The conversion is following a 26 based number system, in which 1 =a and 26  = z
# Examples: 1 = a; 26 = z; 27 = aa;
# cbd
# 3*26² + 2*26^1 + 4 *26^0 = 2084
# aaa
# 1 * 26² + 1* 26^1 + 1 * 26^0 = 703

import string

start_value = 1
stop_value = 9999999
max_string_length = 8

# Returns the highest dimension for a number, when converted into the base 26 number system
def get_text_dimension(number):
    if number <= 26:
        return 0

    for dimension in range (1, max_string_length, 1):
        if get_min_value_for_text_dimension(dimension) == number:
            return dimension

        if get_min_value_for_text_dimension(dimension) > number:
            # the min_value for dimension excreeds the number to be converted
            # return the next biggest dimension
            return dimension -1

# gets the value for the first string of this dimension, for example AAAA
# lowest possible min_value is 1 (converts to A)
# the min_value of dimension 2 is aaa -> 1 * 26² + 1* 26^1 + 1 * 26^0 = 703
def get_min_value_for_text_dimension(textOrder):
    baseValue = 0
    for n in range(textOrder, -1, -1):
        baseValue += 1 * pow(26, n)

    return baseValue


# numeric letter has value 1 for a and 26 for z - offset to ascii, where a = 0
# Example: cbd -> the value for the "c" is = 3*26²
def get_numeric_value_for_letter(numericLetter, order):
    return numericLetter * pow(26, order)


# main loop converting each number in range of start_value and stop_value
for counter in range(start_value, stop_value):

    # start with a blank text before conversion
    convertedString = ''
    highestTextDimension = get_text_dimension(counter)
    numeric_value_already_converted = 0

    # iterate through all text dimensions, starting from the highest
    for currentTextDimension in range(highestTextDimension, -1, -1):

       # if the current text dimension is 0 (number is in between 1-26), the number converts to a single letter
        if currentTextDimension == 0:
            numericLetter = counter - numeric_value_already_converted

        # we need to convert the letter for the current dimension
        # and save the remainder of the counter for further conversion
        else:
            # the value of an a in the current dimension
            minValueOfCurrentLetter = get_numeric_value_for_letter(1, currentTextDimension)

            # reserve space for at least an "a" on each inferior dimension
            actual_value_of_current_letter = counter - numeric_value_already_converted \
                                             - get_min_value_for_text_dimension(currentTextDimension - 1)

            # How many times does the min_value of the current dimension fit into the actual value?
            # the numeric letter is in between 1 and 26 , with 1 = a
            numericLetter = int(actual_value_of_current_letter / minValueOfCurrentLetter)

            # get the value of the current letter and add it to the count of already converted numbers
            valueOfCurrentLetter = get_numeric_value_for_letter(numericLetter, currentTextDimension)
            numeric_value_already_converted += valueOfCurrentLetter

        try:
            # substract 1 to correct offset that "a" is 0 in ascii
            ascii_letter = string.ascii_lowercase[numericLetter - 1]
        except:
            print("failed to convert numeric letter", numericLetter, ascii_letter, counter)
            continue

        # add current letter to string
        convertedString = convertedString + ascii_letter

    print(counter, convertedString)