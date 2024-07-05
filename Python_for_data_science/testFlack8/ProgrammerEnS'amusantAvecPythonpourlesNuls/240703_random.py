# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240703_random.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/03 07:18:38 by pwolff            #+#    #+#              #
#    Updated: 2024/07/03 07:58:36 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# import random
from random import randint

for i in range(1, 11):
    print(i, " : ", randint(1, 10))

# print(help(random.randint))
print(help(randint))


import this

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()