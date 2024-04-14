# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240412_openClass_PandasQuiz.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/12 08:14:00 by pwolff            #+#    #+#              #
#    Updated: 2024/04/14 10:38:19 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/exercises/4576


import numpy as np
import pandas as pd

notes = pd.read_csv('notes.csv')

print("\n**************************************")
print("********** Question 5 ***************")
print("\n**************************************\n")


print(notes)
notesMath = notes[notes['matiere'] == 'Mathématiques']
print(notesMath)
moyenne = notesMath['note'].mean()
print("\nMoyenne : ", round(moyenne, 2))



print("\n**************************************")
print("********** Question 6 ***************")
print("\n**************************************\n")

moyenne = notes[['nom', 'note']].groupby('nom').mean()
print(moyenne)
nombreInf10 = moyenne[moyenne['note'] < 10].shape[0]
print("\nQui n ont pas la moyenne :", nombreInf10)


print("\n**************************************")
print("********** Question 7 ***************")
print("\n**************************************\n")

print(notes.loc[((notes['matiere'] == 'Mathématiques') | (notes['matiere'] == 'Physique/Chimie')) & (notes['note'] >= 15), 'nom'])


print("\n**************************************")
print("********** Question 8 ***************")
print("\n**************************************\n")

notes_sup = pd.read_csv('notes_sup.csv')
print(notes_sup)
notesTotal = pd.merge(notes, notes_sup, how="outer")
print(notesTotal)

notesTotal = pd.concat([notes, notes_sup])
print(notesTotal)


print("\n**************************************")
print("********** Question 9 ***************")
print("\n**************************************\n")

print(notesTotal)
print(notesTotal.pivot_table(index='nom', columns='matiere', values='note'))
# print(notes.groupby(['nom', 'matiere']).unique())
print(notesTotal.melt(id_vars=['nom', 'matiere'], value_vars='note'))


print("\n**************************************")
print("********** Question 10 ***************")
print("\n**************************************\n")


commande = pd.read_csv('commande.csv')
produits = pd.read_csv('produits.csv')
print(commande)
print(produits)

totalProduit = pd.merge(produits, commande, on='id', how='inner')
# totalProduit = commande.merge(produits)
print(totalProduit)
totalProduit['CA'] = totalProduit['prix'] * totalProduit['nombre']

print(totalProduit)

somme = totalProduit[['id','nombre', 'CA']].groupby('id').sum()
# somme = totalProduit.groupby('id').sum()
print(somme)





# totalProduit = totalProduit.pivot_table(index='id')


print(somme.sort_values('CA').head(1))
print(somme.sort_values('nombre').tail(1))

print((somme.sort_values('CA').head(1)))
print((somme.sort_values('nombre').tail(1)))


CApetir = ((somme.sort_values('CA').reset_index())[:1]['id'])
CApetir = int(CApetir.iloc[0])

print("CA le plus petit :", CApetir)
print("Le plus vendu : ",int((somme.sort_values('nombre')).reset_index()[-1:]['id'].iloc[0]))

