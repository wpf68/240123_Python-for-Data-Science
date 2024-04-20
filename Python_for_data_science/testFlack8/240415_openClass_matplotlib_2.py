# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240415_openClass_matplotlib_2.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/15 09:55:23 by pwolff            #+#    #+#              #
#    Updated: 2024/04/20 17:43:15 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858361-personnalisez-vos-graphiques-avec-matplotlib

https://colab.research.google.com/github/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/blob/main/notebooks/P3/P3C3%20-%20Personnalisez%20vos%20graphiques%20avec%20Matplotlib.ipynb


"""

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# CA = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/CA.csv')

# print(CA, CA.dtypes)

# CA['date'] = pd.to_datetime(CA['date'])
# # CA['immobilier'] = pd.to_numeric(CA['immobilier'])
# print(CA, CA.dtypes)


# # plt.figure(figsize=(10, 7))
# # # immo = CA[['date', 'immobilier']]
# # # print(immo, type(immo), immo.dtypes)
# # plt.plot(CA['date'], CA['immobilier'])

# print(CA['date'])
# # plt.show()

# # plt.figure(figsize=(10, 7))
# # plt.plot(CA['date'], CA['immobilier'], label='immobilier', linewidth=3)
# # plt.figure(figsize=(10, 7))
# # plt.plot(CA['date'], CA['immobilier'], label='immobilier', linewidth=3)
# # plt.plot(CA['date'], CA['automobile'], label='automobile', linewidth=3)
# # plt.plot(CA['date'], CA['consommation'], label='consommation', linewidth=3)
# # plt.legend(loc='upper right')
# # plt.ylabel('Benefice net (€)', fontsize=13)
# # plt.yticks(fontsize=11)
# # plt.title("Bénéfices mensuels nets sur l'année 2021, par type de prêt", fontsize=14)
# # plt.grid(color='gray', linestyle='-', linewidth=0.5)
# # plt.show()



# # prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets_final.csv')
# # print(prets)
# # plt.scatter(prets['identifiant'], prets['benefices'])
# # plt.show()



# # fig, ax = plt.subplots()
# plt.plot([1, 3, 4, 6], [2, 3, 5, 1])
# # ax.plot([1, 3, 4, 6], [2, 3, 5, 1])

# plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CA = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/CA.csv')
CA['date'] = pd.to_datetime(CA['date'])
print(CA.head())


print(CA['date'])
print(CA['immobilier'])

# date = CA['date'].to_list()
# immobilier = CA['immobilier'].to_list()
# automobile = CA['automobile'].to_list()
# consommation = CA['consommation'].to_list()

date = CA['date']
immobilier = CA['immobilier']
automobile = CA['automobile']
consommation = CA['consommation']


plt.figure(figsize=(10, 7))
plt.plot(date, immobilier, label='immobilier', linewidth=3)
plt.plot(date, automobile, label='automobile', linewidth=3)
plt.plot(date, consommation, label='consommation', linewidth=3)
plt.legend(loc='upper right')
plt.ylabel('Benefice net (€)', fontsize=13)
plt.yticks(fontsize=11)
plt.title("***  PC **** Bénéfices mensuels nets sur l'année 2021, par type de prêt", fontsize=14)
# plt.title("Bénéfices mensuels nets sur l'année 2021, par type de prêt", fontsize=14)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.show()

# plt.figure(figsize=(10, 7))
# plt.plot(CA['date'], CA['immobilier'], label='immobilier', linewidth=3)
# plt.plot(CA['date'], CA['automobile'], label='automobile', linewidth=3)
# plt.plot(CA['date'], CA['consommation'], label='consommation', linewidth=3)
# plt.legend(loc='upper right')
# plt.ylabel('Benefice net (€)', fontsize=13)
# plt.yticks(fontsize=11)
# plt.title("Bénéfices mensuels nets sur l'année 2021, par type de prêt", fontsize=14)
# plt.grid(color='gray', linestyle='-', linewidth=0.5)
# plt.show()

