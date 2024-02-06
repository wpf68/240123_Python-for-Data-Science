# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 07:57:01 by pwolff            #+#    #+#              #
#    Updated: 2024/02/06 08:30:52 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    print(f"{object} {type(object)}")

    tab = {
        NoneType: "Nothing",
        float: "Cheese"

    }
