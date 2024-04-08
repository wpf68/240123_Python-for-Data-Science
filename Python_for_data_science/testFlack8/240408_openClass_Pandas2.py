# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240408_openClass_Pandas2.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/08 13:48:04 by pwolff            #+#    #+#              #
#    Updated: 2024/04/08 15:49:15 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas


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

print(prets)

# profilClient = prets.groupby(['identifiant', 'taux_endettement', 'cout_total', 'benefices'])['remboursement'].sum()
profilClient = prets.groupby(['identifiant']).agg({'remboursement': 'sum','taux_endettement': 'sum', 'cout_total': 'sum', 'benefices': 'sum'})
print(profilClient.reset_index())

risques = profilClient[profilClient['taux_endettement'] > 35]
print(risques)
nbrRisque = risques.shape[0]
print("nbrRisque = ", nbrRisque)

print("\n****************************************************")
print("****************************************************")
print("****************************************************\n")

# benefAgence = prets.groupby(['ville', 'type']).sum()
# benefAgence = prets.groupby(['ville', 'type']).agg({'benefices': 'sum'})
benefAgence = prets.groupby(['ville', 'type'])['benefices'].sum()
print(benefAgence)


print("\n****************************************************\n")

# benefMoyen = prets.pivot_table(index='ville', columns='type', values='benefices', aggfunc=np.mean)
# print(benefMoyen)

benefMoyen = prets.pivot_table(index='ville', columns='type', values='benefices', aggfunc='mean')
print(benefMoyen.reset_index())
print("\n****************************************************\n")

benefMoyen = benefMoyen.sort_values('immobilier', ascending=False).reset_index()
print(benefMoyen)
print("The Best : ", benefMoyen.loc[0, 'ville'])





