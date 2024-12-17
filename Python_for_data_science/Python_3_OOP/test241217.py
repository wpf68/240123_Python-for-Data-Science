# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test241217.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/17 08:46:56 by pwolff            #+#    #+#              #
#    Updated: 2024/12/17 09:00:45 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def parler(self):
        return "rien"
        pass
    # @abstractmethod
    def origine(self):
        return "Animal"

class Chien(Animal):
    def parler(self):
        return "Wouf Wouf"

class Chat(Animal):
    def parler(self):
        return "Miaou"

# Tentative d'instanciation de la classe abstraite
# animal = Animal()  # Cela lèvera une erreur

# Utilisation des sous-classes
mon_chien = Chien()
mon_chat = Chat()

print(mon_chien.parler()) # Affichera "Wouf Wouf"
print(mon_chien.origine()) # Affichera "Wouf Wouf"
print(mon_chat.parler()) # Affichera "Miaou"
print(mon_chat.origine()) # Affichera "Miaou"