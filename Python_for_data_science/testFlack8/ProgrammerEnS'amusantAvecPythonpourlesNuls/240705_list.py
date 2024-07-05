# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240705_list.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/05 09:42:40 by pwolff            #+#    #+#              #
#    Updated: 2024/07/05 10:28:25 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

list = [3 * x for x in range(10)]
print(list)

list3 = [3 * i for i in range(10) if (3 * i) % 2 == 0]
print(list3)




def table(x):
    list = []
    for i in range(10):
        list.append(i * x)
    return list

print(table(7))

list2 = [table(8)]
print(list2)

print(dir(list))
print(id(list))
print(id(list2))
