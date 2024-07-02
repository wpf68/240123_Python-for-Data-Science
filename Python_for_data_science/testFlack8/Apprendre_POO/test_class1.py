# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_class.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 13:07:18 by pwolff            #+#    #+#              #
#    Updated: 2024/05/28 13:25:21 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



class cercle():
    rayon = 3


print(cercle)
print (cercle.rayon)

c = cercle()
print(c.rayon)
c.rayon = 5
print("*********  Rayon = 5 *******")
print (cercle.rayon)
print(c.rayon)


print("*********  Diametre = 10 *******")
c.diametre = 10

# print (cercle.diametre) *** impossible
print(c.diametre)


print("*********  Perimetre = 20 *******")

cercle.perimetre = 20
print (cercle.perimetre)
print(c.perimetre)

cercle.perimetre = 200
print (cercle.perimetre)
print(c.perimetre)

c.perimetre = 400
print (cercle.perimetre)
print(c.perimetre)



print("*********  rayon = 20 *******")

c.rayon = 25
print(cercle.rayon)
print(c.rayon)


cercle.rayon = 250
print(cercle.rayon)
print(c.rayon)


print("*********  perimetre pour c2 *******")

c2 = cercle()
print (cercle.perimetre)
print(c.perimetre)
print(c2.perimetre)

print("*********  perimetre = 500  pour cercle *******")
cercle.perimetre = 500
print (cercle.perimetre)
print(c.perimetre)
print(c2.perimetre)

print("*********  perimetre = 600  pour c *******")
c.perimetre = 600
print (cercle.perimetre)
print(c.perimetre)
print(c2.perimetre)


print("*********  perimetre = 700  pour c2 *******")
c2.perimetre = 700
print(cercle.perimetre)
print(c.perimetre)
print(c2.perimetre)


