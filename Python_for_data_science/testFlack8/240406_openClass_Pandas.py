# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240406_openClass_Pandas.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/06 08:25:52 by pwolff            #+#    #+#              #
#    Updated: 2024/04/07 11:19:50 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame
# https://egallic.fr/Enseignement/Python/pandas.html
# https://cdiese.fr/pandas-series/




import numpy as np
import pandas as pd

prets = pd.read_csv("https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv")
print(prets.head())

# tauxInteret = prets["remboursement"] / prets["revenu"] * 100
# tauxInteret = tauxInteret.astype(int)
# tauxInteret = tauxInteret / 100



tauxInteret = round((prets["remboursement"] * 100 / prets["revenu"]), 2)
# tauxInteret = round(tauxInteret, 2)
print (tauxInteret)

prets["taux_endettement"] = tauxInteret
prets.rename(columns={'taux': 'taux_interet'}, inplace=True)
# prets = prets.rename(columns={'taux': 'taux_interet'})

print(prets.head())

# cout_total = round(((((prets["remboursement"] * prets["taux_interet"]) / 12) / (1 - (1 + (prets["taux_interet"] / 12)) ** (- prets["duree"]))) * prets["duree"]), 2)
cout_total = round((prets["remboursement"] * prets["duree"]), 2)
print(cout_total)
benefices = round(((cout_total * prets["taux_interet"] / 100) / 24), 2)
print (benefices)

prets["cout_total"] = cout_total
prets["benefices_Mensuel"] = benefices
print(prets.head())

# prets = prets.sort_values('benefices_Mensuel', ascending=False)
# print(prets.head())
prets = prets.sort_values('benefices_Mensuel', ascending=False).head()
print(prets)

prets = prets.rename(index={8: '01', 23: "02"})
print(prets)

# prets['ville'][181] = "Nice01"    error
prets.loc['02', 'ville'] = "Nice02"

print(prets)

print("\n****************************************************")
print("****************************************************")
print("****************************************************\n")


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

print(prets.head(), "\n", prets.shape)

clients_risque = prets[prets['taux_endettement'] > 35]
print (clients_risque, "\nNbr de clients a risques : ", clients_risque.shape[0])

clients_risque = prets[(prets['taux_endettement'] > 35) & (prets['ville'] == 'PARIS')]
print (clients_risque, "\nNbr de clients a risques sur Paris : ", clients_risque.shape[0])

risque = pd.Series("Non", index = [np.arange(prets.shape[0])])
print(risque)