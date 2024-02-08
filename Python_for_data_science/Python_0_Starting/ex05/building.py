# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 08:20:39 by pwolff            #+#    #+#              #
#    Updated: 2024/02/08 09:28:32 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
# import string

def main():
    tab = sys.argv
    strPunctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    nbUpperCase = sum(1 for value in tab[1] if value.isupper())
    nbLowerCase = sum(1 for value in tab[1] if value.islower())
    nbPunctuation = sum(1 for value in tab[1] if value in strPunctuation)
    nbDigits = sum(1 for value in tab[1] if value.isdigit())
    nbSpaces = sum(1 for value in tab[1] if value.isspace() or value == '\n')

    # strPunctuation = string.punctuation
    
    # for value in tab[1]:
    #     if value.isupper():
    #         nbUpperCase += 1
    #     elif value.islower():
    #         nbLowerCase += 1
    #     elif value in strPunctuation:
    #         nbPunctuation += 1
    #     elif value.isdigit():
    #         nbDigits += 1
    #     elif value == " " or value =="\n":
    #         nbSpaces += 1

    print(f"The text contains {len(tab[1])} characters:")
    print(f"{nbUpperCase} upper letters")
    print(f"{nbLowerCase} lower letters")
    print(f"{nbPunctuation} punctuation marks")
    print(f"{nbSpaces} spaces")
    print(f"{nbDigits} digits")


if __name__ == "__main__":
    main()
