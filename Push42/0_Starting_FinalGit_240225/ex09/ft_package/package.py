# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    package.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/17 08:10:53 by pwolff            #+#    #+#             #
#    Updated: 2024/02/17 08:10:53 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

# pip install flak8
# alias norminette=flake8

# Chemin pour flack8 :
# export PATH=$PATH:/home/pwolff/.local/bin

def count_in_list(list, search):
    """
        The count_in_list(list, string) method returns the number
        of times the specified element appears in the list.',
    """
    return list.count(search)
