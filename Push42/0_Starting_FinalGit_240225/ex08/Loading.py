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
est la solution la plus adaptée. Inversement, si la consommation de mémoire
est moins prioritaire que les performances d’exécution, il est plus approprié
d’utiliser une source de données statique telle qu’une liste.

Creer un decompte :
https://www.delftstack.com/fr/howto/python/python-countdown-timer/

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin

"""


def formatTime(secound):
    m, s = divmod(secound, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(listeRange: range) -> None:
    i = len(listeRange) - 1
    for value in listeRange:
        pourcentage = int(100 / i * value)
        string = "|" + '█' * int(pourcentage)
        string += ' ' * int(100 - pourcentage)
        if len(str(value + 1)) < len(str(i + 1)):
            nbZero = int(len(str(i + 1)) - len(str(value + 1)))
            strValue = str(value + 1) + "." + "0" * nbZero
        else:
            strValue = " " + str(value + 1)
        string += "|" + f" {strValue}/{i + 1}"

        print(f"\r{pourcentage:>3.0f}%{string}", end="", flush=True)

        yield


def main():
    pass


if __name__ == "__main__":
    main()
