# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_filter.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/10 09:01:13 by pwolff            #+#    #+#             #
#    Updated: 2024/02/10 09:01:13 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

"""
class ft_filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  

    Comment filter une liste sans utiliser filter ?

    https://www.commentcoder.com/python-fonction-filter/

    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    nombres_pairs = [nombre for nombre in nombres if nombre % 2 == 0]

    print(nombres_pairs)

"""

def ft_filter(ft_lambda, listIterable):
    if ft_lambda:
        return(value for value in listIterable if ft_lambda(value))
    return(value for value in listIterable if value == True)