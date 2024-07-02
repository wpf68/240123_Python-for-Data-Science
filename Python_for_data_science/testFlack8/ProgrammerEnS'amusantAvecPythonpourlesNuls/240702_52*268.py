# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240702_52*268.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/02 10:16:40 by pwolff            #+#    #+#              #
#    Updated: 2024/07/02 10:34:22 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

str = (input("Value :"))
str *= 3

try:
    value = int(str)
except ValueError:
    print ("input not int !!!", ValueError.__name__)
    exit()

print(str)
print(type(str))

