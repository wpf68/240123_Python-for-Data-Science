# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240515_test_list.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/15 07:30:42 by pwolff            #+#    #+#              #
#    Updated: 2024/05/15 07:45:40 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


"""
https://www.commentcoder.com/python-liste-strings/
"""


test = ["hello", "bonjour"]
print(test)
test.reverse()
print(test)
test.insert(1, "Titi")
print(test)


test2 = "helo"
print(test2)
test2 = list(test2)
print(test2)
test2.insert(2,"l")
print(test2)
test2 = "".join(test2)
print(test2)
