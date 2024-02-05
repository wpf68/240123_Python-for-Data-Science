# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/05 07:57:32 by pwolff            #+#    #+#              #
#    Updated: 2024/02/05 08:33:09 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

todaySecound = time.time()
decimal = (str(todaySecound).split('.'))[1]


# print(todaySecound)
# print(time.ctime(0))
# print(time.gmtime())
# print(time.ctime(todaySecound))

print(f"Seconds since January 1, 1970: {int(todaySecound):,d}.{decimal} or {todaySecound:.1E} in scientific notation")
print(time.strftime("%b %d %Y"))