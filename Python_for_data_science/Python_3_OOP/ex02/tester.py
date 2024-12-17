# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/17 10:03:47 by pwolff            #+#    #+#             #
#    Updated: 2024/12/17 13:00:33 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

# https://www.reddit.com/r/learnpython/comments/dhu6wm/
# why_is_diamond_death_actually_a_problem_in_python/?tl=fr&rdt=40910

# https://fr.wikipedia.org/wiki/Lin%C3%A9arisation_C3

# https://deusyss.developpez.com/tutoriels/Python/heritage_metaclasse/

from DiamondTrap import King


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()


# Comment Python gère-t-il les problèmes d’héritage multiple et de diamant?
# Python est un autre langage POO qui prend en charge l’héritage multiple,
# mais il utilise une approche différente pour résoudre le problème du diamant.
# Python utilise le concept d’ordre de résolution de méthode (MRO),
# qui est un ordre linéaire des classes impliquées dans la hiérarchie
# d’héritage. Le MRO détermine quelle méthode de classe sera appelée en premier
# en cas de conflit. Python calcule le MRO à l’aide d’un algorithme appelé C3,
# qui garantit que les sous-classes sont visitées avant leurs superclasses et
# que l’ordre est cohérent avec l’ordre des classes de base. Par exemple, si
# vous définissez Pet comme une sous-classe de Dog and Cat, et Dog et Cat
# comme des sous-classes d’Animal, alors le MRO de Pet sera
# [Animal, chien, chat, animal]. Cela signifie que l’animal héritera de la
# nourriture() de Dog, puisque c’est la première classe du MRO qui la définit.
