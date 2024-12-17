# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    .tester.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/17 10:03:47 by pwolff            #+#    #+#              #
#    Updated: 2024/12/17 10:04:16 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from S1E9 import Character, Stark
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

