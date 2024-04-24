# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    S1E9.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/04/24 10:00:28 by pwolff            #+#    #+#             #
#    Updated: 2024/04/24 10:00:28 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""
    https://docs.python.org/fr/3/library/abc.html
    https://www.tresfacile.net/le-module-abc-python/
    https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf



"""


from abc import ABC, abstractmethod


class Véhicule(ABC):
    @property
    @abstractmethod
    def nom(self):
        pass

class Voiture(Véhicule):
    nom = "Peugeot"

v = Voiture()
print("v.nom = ", v.nom)




# class Character(ABC):
#     """Your docstring for Class"""
#     @abstractmethod
#     #your code here
#     def doSomething(self, name):
#         print("test")
        

# class Stark(Character):
#     """Your docstring for Class"""
#     #your code here
#     def __init__(self) -> None:
#         super().__init__()
    
#     def is_alive() -> bool:
#         return True


