# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/05 07:57:32 by pwolff            #+#    #+#              #
#    Updated: 2024/02/16 11:12:12 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

todaySecound = time.time()
# decimal = (str(todaySecound).split('.'))[1]

# print(f"Seconds since January 1, 1970: {int(todaySecound):,d}.{decimal[:4]} or {todaySecound:.2e} in scientific notation")
print(f"Seconds since January 1, 1970: {todaySecound:,.4f} or {todaySecound:.2e} in scientific notation")
print(time.strftime("%b %d %Y"))