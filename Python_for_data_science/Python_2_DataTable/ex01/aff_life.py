# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    aff_life.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/04/01 10:22:42 by pwolff            #+#    #+#             #
#    Updated: 2024/04/01 10:22:42 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from load_csv import load
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np

"""
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7856527-tirez-un-maximum-de-ce-cours
https://colab.research.google.com/drive/155rZhNOiLcv_jmtWiHzjrHR1vtye2TOJ

https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858285-tracez-des-graphiques-avec-matplotlib
https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html




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

def main(country = "France"):
    if len(sys.argv) > 1:
        country = sys.argv[1]
    
    # countriesData = load("life_expectancy_years.csv")
    countriesData = pd.read_csv("life_expectancy_years.csv")
    print(GREEN, "liste des pays : ")
    print(list(countriesData["country"]), "\n")

    print(f"\n{BLUE} ********** {country} ************ ")
    datas = countriesData[countriesData["country"].isin([country])]
    print(f"{datas}{WHITE}\n")
    # ts = pd.Series(datas)


    # ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    # ts = ts.cumsum()
    # ts.plot()
    # plt.show()

    # plt.plot(datas)
    # plt.show()

    # print(datas['France'])



    # ***********************************
    #      Methode 1 pandas to numpy

    print(datas.dtypes)

    datasNumpy = datas.values
    print("\nvalues\n", datasNumpy)

    datasNumpy = datasNumpy[0:1, 1:]
    print("\n[0:1, 1:]\n", datasNumpy)

    datasNumpy = datasNumpy[0]
    print("\n[0]\n", datasNumpy)

    # plt.plot(datasNumpy)
    # plt.show()

    # ***********************************


    # ***********************************
    #      Methode 2 recuperation du header de pandas


    header = list(countriesData)
    print("\nHeader :\n", header[1:])
    # ts = pd.Series(np.random.randn(1000))
    ts = pd.Series(datasNumpy, index=header[1:])


    print("\n*****************************\n",datas)
    print("\n*****************************\n",ts)
    
    # ts = pd.Series(datas)
    # ts = ts.cumsum()
    ts.plot()
    plt.show()
    




if __name__ == "__main__":
    main()
