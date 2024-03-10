# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/09 10:57:15 by pwolff            #+#    #+#             #
#    Updated: 2024/03/09 10:57:15 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from give_bmi import give_bmi, apply_limit

print("\033[1;33m")
print("\n *** Utiliser bash !!! ***\n")
print("\033[1;37m")


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print("\033[1;32m", bmi, type(bmi))
print("\033[1;32m", apply_limit(bmi, 26), "\033[1;37m")

print("\n********* Lists not same size ****************\n")

height = [2.71, 1.15]
weight = [165.3, 38.4, 35]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


print("\n********* Value imvalid ****************\n")

height = [2.71, 2]
weight = [165.3, -12]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


print("\n********* not int or float ****************\n")

height = [2.71, 2]
weight = [165.3, "hj"]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


print("\n********* division by zero ****************\n")

height = [2.71, 2, 0]
weight = [165.3, 35, 56]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
