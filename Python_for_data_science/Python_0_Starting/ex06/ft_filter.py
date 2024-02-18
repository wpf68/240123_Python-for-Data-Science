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


def ft_filter(ft_lambda, listIterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # if ft_lambda:
    #     print("lambda")
    #     return(value for value in listIterable if ft_lambda(value))
    # print("No lambda !!!")
    # return(value for value in listIterable if value == True)
    return (value for value in listIterable if ft_lambda(value))
