# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    projection_life.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/04/24 08:18:05 by pwolff            #+#    #+#             #
#    Updated: 2024/04/24 08:18:05 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

import matplotlib.pyplot as plt
# import sys
import pandas as pd
# import numpy as np
# from matplotlib.ticker import EngFormatter

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


def main():
    """
    Create a program that calls the load function from the first exercise,
loads the files "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
and "life_expectancy_years.csv", and displays the projection of life
expectancy in relation to the gross national product of the year 1900 for
each country.
    """
    try:
        nameFile = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        inflationData = pd.read_csv(nameFile)
        lifeExpectancy = pd.read_csv("life_expectancy_years.csv")

    except Exception:
        print(f"\033[1;31m{Exception.__name__} \
              : File DataBase no present\033[1;37m")
        exit()
    inflationData = inflationData[['country', '1900']]
    inflationData = inflationData.rename(columns={'1900': 'inflation'})
    print(inflationData)

    lifeExpectancy = lifeExpectancy[['country', '1900']]
    lifeExpectancy = lifeExpectancy.rename(columns={'1900': 'lifeExpectancy'})
    print(lifeExpectancy)
    data = pd.merge(inflationData, lifeExpectancy)
    print(data)

    plt.figure(figsize=(9, 7))
    plt.scatter(data['inflation'], data['lifeExpectancy'])


#     plt.figure(figsize=(20, 12))
#     for country in data["country"]:
#         # print(country)
#         df = data.loc[data['country'] == country, :]
#         plt.scatter(df['inflation'], df['lifeExpectancy'], label=country)
# # http://www.python-simple.com/python-matplotlib/ajout-legende.php
#     plt.legend(ncol = 3)

    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    # plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(GREEN, main.__doc__, WHITE)
    main()
