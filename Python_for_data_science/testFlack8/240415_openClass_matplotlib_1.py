# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240415_openClass_matplotlib_1.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/15 08:00:01 by pwolff            #+#    #+#              #
#    Updated: 2024/04/15 09:09:08 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858285-tracez-des-graphiques-avec-matplotlib
https://colab.research.google.com/github/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/blob/main/notebooks/P3/P3C2%20-%20Tracez%20des%20graphiques%20avec%20Matplotlib.ipynb


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("************** PRETS ****************************\n")

# traitement réalisés précédemment
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets_final.csv')

print(prets)

print("\n******** 1. proportion de prêt par type de prêt. ***********\n")
type = prets.groupby('type').size()
type = type.reset_index()


# via la fonction value_counts :
# type = prets['type'].value_counts().reset_index()



type.columns = ['type', 'nombre']


print(type)
plt.pie(x=type['nombre'], labels=type['type'], autopct='%.2f%%')
plt.show()


print("\n******** 2. bénéfice mensuel réalisé en fonction du revenu du client - prêts immobiliers ***********\n")
# beneficesImmo = prets[prets['type'] == 'immobilier'].sort_values('revenu').reset_index()
beneficesImmo = prets[prets['type'] == 'immobilier']
print(beneficesImmo)
plt.scatter(beneficesImmo['revenu'], beneficesImmo['benefices'])
plt.show()


print("\n******** 3. La distribution des bénéfices réalisés ***********\n")
plt.hist(prets['benefices'])
plt.show()

print("\n******** 4. bénéfice mensuel total réalisé par agence ***********\n")
agences = prets.groupby('ville').sum('benefices').reset_index()
print(agences)
plt.bar(height=agences['benefices'], x=agences['ville'])
plt.show()
agences = agences.sort_values('benefices')
print(agences)
plt.bar(height=agences['benefices'], x=agences['ville'])
plt.show()
