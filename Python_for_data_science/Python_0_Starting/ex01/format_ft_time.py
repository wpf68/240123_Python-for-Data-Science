# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/05 07:57:32 by pwolff            #+#    #+#              #
#    Updated: 2024/02/06 07:56:43 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

todaySecound = time.time()
decimal = (str(todaySecound).split('.'))[1]

print(f"Seconds since January 1, 1970: {int(todaySecound):,d}.{decimal[:4]} or {todaySecound:.1E} in scientific notation")
print(time.strftime("%b %d %Y"))