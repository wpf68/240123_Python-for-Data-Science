# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 07:57:01 by pwolff            #+#    #+#              #
#    Updated: 2024/02/16 10:41:16 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def NULL_not_found(object: any) -> int:
    # print(f" ** {object} {type(object)}")

    tab = {
        None: "Nothing",
        math.nan: "Cheese",
        "0": "Zero",
        '': "Empty",
        False: "Fake",
    }

    result = tab.get(object, "Type not Found")
    # print(f" ** Result = {result}")
    # typeObject = type(object)

    if object == None:
        print(f"{result}: {object} {type(object)}")
    elif result == "Empty":
        print(f"{result}: {type(object)}")
    elif object == 0 and type(object) == int:
        print(f"Zero: {object} {type(object)}")
    elif object == False and type(object) == bool:
        print(f"{result}: {object} {type(object)}")
    elif type(object) == float and math.isnan(object): # Test float sinon conflit avec isnam pour autres valeurs
        print(f"Cheese: {object} {type(object)}")
    else:
        print(result)
        return 1
    
    return 0
        




    # print(tab)
    


