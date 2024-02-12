# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    sos.py                                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/12 07:41:08 by pwolff            #+#    #+#             #
#    Updated: 2024/02/12 07:41:08 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

"""
Program that takes a string as an argument and encodes it into Morse Code.

• The program supports space and alphanumeric characters
• An alphanumeric character is represented by dots . and dashes -
• Complete morse characters are separated by a single space
• A space character is represented by a slash /


Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin

"""

import sys


def createdCode(message):
    NESTED_MORSE = {
        ' ': '/',
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }

    result = ""
    try:
        for value in message:
            # result += value + " : " + NESTED_MORSE[value.upper()] + "\n"
            result += NESTED_MORSE[value.upper()] + " "
    except KeyError:
        print(f"AssertionError: the argument {value} is bad")
        sys.exit()
    return result[:len(result) - 1]


def main():

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the number of arguments are bad")
    except AssertionError as error:
        print(AssertionError.__name__ + ": " + str(error))
        sys.exit()

    message = sys.argv[1]
    result = createdCode(message)

    print(result)


if __name__ == "__main__":
    main()
