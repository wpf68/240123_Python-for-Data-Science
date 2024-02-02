# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 10:52:27 by pwolff            #+#    #+#              #
#    Updated: 2024/02/02 08:03:24 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here



"""
    Les list
    "Apprenez programmer en Python 4eme" page 115 - 121
    
    ********************************

    ft_list[1] = "World!"

    ********************************

    del ft_list[1]
    ft_list.append("World!")

    ********************************

    del ft_list[1]
    ft_list += ["World!"]

    ********************************

    ft_list.remove("tata!")
    ft_list += ["World!"]


"""

ft_list.remove("tata!")
ft_list += ["World!"]





"""
    Les tuples sont des sequences assez semblables aux listes, sauf qu'on ne peut
    modifier un tule apres qu'il a ete cree. Cela signifie qu'on definit le contenu
    d'un tule (les objets qu'il doit contenir) lors de sq creation, mains qu'on ne
    peut en ajouter ou en retier par la suite.

    "Apprenez programmer en Python 4eme" page 122

"""
del ft_tuple
ft_tuple = ("Hello", "France!")


"""
    les dictionnaires {"Cle" : "Valeur", "Cle2" : "Valeur2"}
    Pour ajouter une paire clé-valeur à un dictionnaire, ajoutez juste une 
    nouvelle clé dans le dictionnaire existant. Si la clé existe déjà, 
    vous l’écraserez en définissant une valeur.
"""

# ft_dict = {"Hello" : "titi!"}
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



"""
    $>python Hello.py | cat -e
    ['Hello', 'World!']$
    ('Hello', 'France!')$
    {'Hello', 'Paris!'}$
    {'Hello': '42Paris!'}$
    $>

"""