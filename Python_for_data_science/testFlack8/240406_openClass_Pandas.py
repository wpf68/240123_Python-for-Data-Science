# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240406_openClass_Pandas.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/06 08:25:52 by pwolff            #+#    #+#              #
#    Updated: 2024/04/06 08:53:48 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame


import numpy as np
import pandas as pd

prets = pd.read_csv("https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv")
print(prets.head())

# tauxInteret = prets["remboursement"] / prets["revenu"] * 100
# tauxInteret = tauxInteret.astype(int)
# tauxInteret = tauxInteret / 100



tauxInteret = round((prets["remboursement"] / prets["revenu"]), 2)
# tauxInteret = round(tauxInteret, 2)

prets["taux_interet"] = tauxInteret
print(prets.head())

