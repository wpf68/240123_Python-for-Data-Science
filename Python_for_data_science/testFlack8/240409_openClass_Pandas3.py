# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240409_openClass_Pandas3.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/09 09:47:33 by pwolff            #+#    #+#              #
#    Updated: 2024/04/12 08:07:05 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857932-fusionnez-des-donnees-avec-pandas


import numpy as np
import pandas as pd

# traitement réalisés précédemment
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')

# calcul du taux d'endettement
prets['taux_endettement'] = round(prets['remboursement'] * 100 / prets['revenu'], 2)

# renommer taux en taux_interet
prets.rename(columns={'taux':'taux_interet'}, inplace=True)

# calculer le cout total du pret
prets['cout_total'] = prets['remboursement'] * prets['duree']

# calculer les bénéfices mensuels réalisés
prets['benefices'] = round((prets['cout_total'] * prets['taux_interet']/100)/(24), 2)

# création d'une variable risque
prets['risque'] = 'Non'
prets.loc[prets['taux_endettement'] > 35, 'risque'] = 'Oui'

# dataframe de profils clients
profil_clients = prets.groupby('identifiant')[['remboursement','taux_endettement','cout_total','benefices']].sum()
profil_clients.reset_index(inplace=True)
profil_clients.head()

print(prets)
print(profil_clients)



clients_1 = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/clients.csv')
print(clients_1)

clients_2 = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/clients_suite.csv')
print(clients_2)


print("\n**********************************************")
print("*************  CLIENTS  ***************************\n")

clients = pd.concat([clients_1, clients_2])
print(clients)

# clients = [clients_1, clients_2]
# clients = pd.concat(clients, ignore_index=True)
# print(clients)

# total = pd.merge(clients_1, clients_2, on="identifiant", how="outer")
# print(total)


print("\n**********************************************")
print("*************  DATA  ***************************\n")

data = pd.merge(clients, profil_clients, on="identifiant")
print(data)



print("\n**********************************************")
print("*************  AGE  ***************************\n")

clients_age = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/client_age.csv')
print(clients_age)

data = pd.merge(data, clients_age, on="identifiant", how="left")
print(data)