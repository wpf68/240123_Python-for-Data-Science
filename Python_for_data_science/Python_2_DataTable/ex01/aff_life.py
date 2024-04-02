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

"""

"""
python3 -m venv env
source env/bin/activate


pip install pandas
pip install matplotlib


"""


def main(country = "France"):
    if len(sys.argv) > 1:
        country = sys.argv[1]
    print(country)
    countriesData = load("life_expectancy_years.csv")
    datas = countriesData[countriesData["country"].isin([country])]
    print(datas)
    # ts = pd.Series(datas)


    # ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    # ts = ts.cumsum()
    # ts.plot()
    # plt.show()

    # plt.plot(datas)
    # plt.show()

    print(datas['France'])




if __name__ == "__main__":
    main()
