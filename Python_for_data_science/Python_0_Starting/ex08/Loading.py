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

"""

def ft_tqdm(listeRange):
    char = '█'
    i = len(listeRange) - 1
    for value in listeRange:
        pourcentage = (100 / i * value)
        # string = f"{'█' * int(pourcentage)}"
        string = "|"
        string += '█' * int(pourcentage)

        
        string += ' ' * int(100 - pourcentage)
        string += "|"
        # pourcentage = int(pourcentage)

        # print(f"\r{pourcentage:6.2f} % {string}", end=" : ", flush=True)
        print(f"\r{pourcentage:>3.0f}%{string}", end=" : ", flush=True)

        yield


def main():
    pass

if __name__ == "__main__":
    main()

