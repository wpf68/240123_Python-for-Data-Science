# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    testPanda.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/26 14:38:51 by pwolff            #+#    #+#              #
#    Updated: 2024/03/26 14:54:52 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


"""
https://ledatascientist.com/manipulez-vos-donnees-avec-pandas/


python3 -m venv env
source env/bin/activate
python3 start.py

or :
pip install numpy
pip install Pillow
pip install matplotlib
pip install pandas

    lire la doc :
    python3
    import load_image
    help(load_image)

    from load_image import ft_load
    help(ft_load)

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin
"""

import pandas as pd

data = { 'population': [2187526,863310,516092,479553,340017],
         'area': [105.4, 240.6,47.87,118.3, 71.92]
}

cities = pd.DataFrame(data,index=['Paris','Marseille','Lyon','Toulouse','Nice'])

print(data)
print(cities)

print("\n**************\n")

print(cities.head(3))

print("\n**************\n")

print(cities["population"])

print("\n**************\n")

print(cities[2:])

print("\n******* [] *******\n")

print(cities[0:1])

print("\n******* iloc[] *******\n")

print(cities.iloc[0])

print("\n******* iloc[] *******\n")

print(cities.iloc[[0, 1]])

print("\n******* filtre *******\n")

print(cities[cities["population"] > 500000])