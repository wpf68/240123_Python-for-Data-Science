# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 10:52:27 by pwolff            #+#    #+#              #
#    Updated: 2024/01/27 11:27:26 by pwolff           ###   ########.fr        #
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
ft_tuple = ("hello", "France")



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