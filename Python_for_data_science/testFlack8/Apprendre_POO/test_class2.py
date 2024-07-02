# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_class2.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 13:30:25 by pwolff            #+#    #+#              #
#    Updated: 2024/05/28 13:34:35 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class cercle():
    def perimetre(machin):
        return 2 * 3.14 * machin.rayon
    

c = cercle()

c.rayon = 2
print(c.perimetre())