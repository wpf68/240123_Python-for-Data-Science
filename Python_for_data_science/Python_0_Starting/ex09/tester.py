# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    tester.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/17 08:16:55 by pwolff            #+#    #+#             #
#    Updated: 2024/02/17 08:16:55 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from ft_package.package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0