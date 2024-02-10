# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    filterstring.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/10 09:02:04 by pwolff            #+#    #+#             #
#    Updated: 2024/02/10 09:02:04 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


# TESTS :
print(filter.__doc__)

aquarium = [11, False, 18, 21, "", 12, 34, 0, [], {}]
print(aquarium)
filtre = filter(None, aquarium)
print(list(filtre))
aquarium = [11, 0, 18, 21, 90, 12, 34, 0]
print(aquarium)

print(list(filter(lambda value: value > 18, aquarium)))
