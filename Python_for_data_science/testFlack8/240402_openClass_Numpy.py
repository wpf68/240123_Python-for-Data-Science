# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240402_openClass_Numpy.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/02 08:04:59 by pwolff            #+#    #+#              #
#    Updated: 2024/04/05 07:35:28 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #





"""
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7856832-creez-vos-premiers-arrays-avec-numpy

https://www.youtube.com/watch?v=mmT2--citbY


"""


import numpy as np
liste = [1800, 1500, 2200, 3000, 2172, 5000, 1400, 1200, 1100, 1300]
revenus = np.array(liste)
print(revenus)
haut_revenus = revenus[revenus >= 3000]
print(haut_revenus)
# somme = (revenus * 12)
# print(somme)
somme = revenus.sum() * 12
print(somme)
moyenne = somme / revenus.shape[0]
print(moyenne)
# revenus[revenus == 1400] = 1600
revenus[revenus == 1400] += 200
print(revenus)



"""
https://colab.research.google.com/github/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/blob/main/notebooks/P1/P1C4%20-%20Transformez%20vos%20donn%C3%A9es%20en%20tableaux.ipynb


"""

print("\n*******************************\n")

hugo = [1800, 21, 0]
richard = [1500, 54, 2]
emilie = [2200, 28, 3]
pierre = [3000, 37, 1]
paul = [2172, 37, 2]
deborah = [5000, 32, 0]
yohann = [1400, 23, 0]
anne = [1200, 25, 1]
thibault = [1100, 19, 0]
emmanuel = [1300, 31, 2]

tableau = [hugo, richard, emilie, pierre, paul, deborah,
           yohann, anne, thibault, emmanuel]

print("tableau :\n", tableau)
data = np.array(tableau)
print("data :\n", data)

valuePaul = data[4, :]
print("Paul = ", valuePaul)
print("taux = ", round(valuePaul[0] * 0.35, 2))

louise = [1900, 31, 1]

data = np.vstack((data, louise))
print("\n", data)

revenus = data[:,0]
print("Revenus : ", revenus)