# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/10 10:56:43 by pwolff            #+#    #+#             #
#    Updated: 2024/03/10 10:56:43 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("\n********** Test list empty **********")
family = []
print(slice_me(family, 1, -2))

print("\n********** Test No list  **********")
family = 1
print(slice_me(family, 1, -2))

print("\n********** Test list no valid for numpy  **********")
family = [[1, 2, 3], [4, 5]]
print(slice_me(family, 1, -2))

print("\n********** Test slicing no valid  **********")
family = [[1, 2, 3], [4, 5, 8]]
print(slice_me(family, 100000000000000000000000000000000000, -2))

print("\n********** Test slicing no valid  **********")
family = [[1, 2, 3], [4, 5, 8]]
print(slice_me(family, "hello", -2))
