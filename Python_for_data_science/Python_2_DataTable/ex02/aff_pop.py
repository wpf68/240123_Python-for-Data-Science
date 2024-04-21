# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    aff_pop.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/04/21 10:35:19 by pwolff            #+#    #+#             #
#    Updated: 2024/04/21 10:35:19 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

# from load_csv import load
import matplotlib.pyplot as plt
import sys
import pandas as pd
# import numpy as np
from matplotlib.ticker import EngFormatter

"""
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7856527-tirez-un-maximum-de-ce-cours
https://colab.research.google.com/drive/155rZhNOiLcv_jmtWiHzjrHR1vtye2TOJ

https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858285-tracez-des-graphiques-avec-matplotlib
https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html


https://gvallverdu.gitbooks.io/python_sciences/content/
https://courspython.com/bases-python.html
https://phychim.ac-versailles.fr/IMG/pdf/tuto_python_matplotlib.pdf

https://www.data-transitionnumerique.com/numpy-python/

"""

"""
python3 -m venv env
source env/bin/activate


pip install pandas
pip install matplotlib
"""
RED = "\033[1;31m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"


def main(country="Belgium"):
    """Country Life expectancy Projections"""
    if len(sys.argv) > 1:
        country = sys.argv[1]

    try:
        countriesData = pd.read_csv("population_total.csv")
        print(countriesData)
    except Exception:
        print(f"\033[1;31m{Exception.__name__} \
              : File DataBase no present\033[1;37m")
        exit()

    datasFirstCountry = countriesData[countriesData["country"] == 'France'].iloc[:, 1:252].squeeze()
    datasFirstCountry = datasFirstCountry.str.replace('M', 'e6').str.replace('k', 'e3').astype(float)


    print(f"\n{BLUE} ********** {country} ************ ")
    testCountry = True
    while testCountry:
        # base de donnees de 1800 a 2050 sur une colonne
        datasSecoundCountry = countriesData[countriesData["country"].isin([country])]
        if datasSecoundCountry.shape[0] != 0:
            testCountry = False
        else:
            print(GREEN, "liste des pays : ")
            print(list(countriesData["country"]), "\n")
            country = input(f"{RED}Secound Country : {WHITE}")
            if country == "":
                print(f"{BLUE}BYE !!!!{WHITE}")
                exit()

    # base de donnees de 1800 a 2050 sur une colonne    
    datasSecoundCountry = datasSecoundCountry.iloc[:, 1:252].squeeze()
    print(f"{datasSecoundCountry}{WHITE}\n")
    datasSecoundCountry = datasSecoundCountry.str.replace('M', 'e6').str.replace('k', 'e3').astype(float)
    print(f"{datasSecoundCountry}{WHITE}\n")




    # print(f"{datas2.ndim}{WHITE}\n")
    print(RED, "****************************************", WHITE)

    plt.figure(figsize=(15, 10))

    plt.plot(
        datasFirstCountry.index.astype(int).to_list(),
        datasFirstCountry.values,
        label='France',
        color='green')
    
    plt.plot(
        datasSecoundCountry.index.astype(int).to_list(),
        datasSecoundCountry.values,
        label=country,
        color='blue')
    

    # datasFirstCountry.plot()
    # datasSecoundCountry.plot()
    # plt.yticks(['100M', '200M', '300M'])

    

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    eng_format = EngFormatter()
    plt.gca().yaxis.set_major_formatter(eng_format)
    # plt.tight_layout()
    plt.show()

    exit()



    # ***********************************
    #      M    # print(GREEN, "liste des pays : ")
    # print(list(countriesData["country"]), "\n")
    print(datas.dtypes)

    datasNumpy = datas.values
    print("\nvalues\n", datasNumpy)

    datasNumpy = datasNumpy[0:1, 1:]
    print("\n[0:1, 1:]\n", datasNumpy)

    datasNumpy = datasNumpy[0]
    # print("liste des pays : ")
    # print(list(countriesData["country"]), "\n")ot(datasNumpy)
    # plt.show()

    # ***********************************
    # ***********************************
    #      Methode 2 recuperation du header de pandas
    header = list(countriesData)
    print("\nHeader :\n", header[1:])
    # ts = pd.Series(np.random.randn(1000))
    ts = pd.Series(datasNumpy, index=header[1:])
    print("\n*********** datas ******************\n", datas)
    print("\n*********** ts  ******************\n", ts)
    plt.figure(figsize=(15, 10))
    # https://webdi.fr/couleur-hexa.php
    ts.plot(color='#005b9c', linewidth=2.5)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(country + ' Life expectancy Projections')
    # plt.xlim("1800", "2100")
    plt.show()


if __name__ == "__main__":
    main()
