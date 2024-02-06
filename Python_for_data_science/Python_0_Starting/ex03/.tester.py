# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    .tester.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 07:58:50 by pwolff            #+#    #+#              #
#    Updated: 2024/02/06 08:00:19 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))