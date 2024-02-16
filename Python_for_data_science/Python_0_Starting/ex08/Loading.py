# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Loading.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/12 08:42:11 by pwolff            #+#    #+#             #
#    Updated: 2024/02/12 08:42:11 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""
les generateur / yield :
https://www.pythoniste.fr/python/quest-ce-quun-generateur-en-python/

Si les contraintes de mémoire l’emportent sur la vitesse, alors un générateur
est la solution la plus adaptée. Inversement, si la consommation de mémoire est
moins prioritaire que les performances d’exécution, il est plus approprié 
d’utiliser une source de données statique telle qu’une liste.

Creer un decompte :
https://www.delftstack.com/fr/howto/python/python-countdown-timer/


"""

import time


def formatTime(secound):
    m, s = divmod(secound, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(listeRange):
    timeInitial = time.time()
    # char = '█'
    i = len(listeRange) - 1
    for value in listeRange:
        pourcentage = (100 / i * value)
        timeActual = time.time() - timeInitial
        speedLoop = value / timeActual
        timeRest = ((i + 1) - value) / speedLoop

        # string = f"{'█' * int(pourcentage)}"
        string = "|"
        string += '█' * int(pourcentage)

        
        string += ' ' * int(100 - pourcentage)
        # s = (time.time() - tempsInitial)
        # a = time.strftime("%H:%M:%S", s)
        string += "|" + f" {value + 1}/{i + 1} [{time.strftime("%H:%M:%S", (time.ctime(time.time() - tempsInitial)))}]"
        # string += "|" + f" {value + 1}/{i + 1} " + formatTime(timeActual) + "<" + formatTime(timeRest)

        # string += "|" + f" {value + 1}/{i + 1} [{a}]"
        
        # pourcentage = int(pourcentage)

        # print(f"\r{pourcentage:6.2f} % {string}", end=" : ", flush=True)
        print(f"\r{pourcentage:>3.0f}%{string}", end="", flush=True)

        yield


def main():
    pass

if __name__ == "__main__":
    main()

