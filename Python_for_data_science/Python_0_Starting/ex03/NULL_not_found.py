# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 07:57:01 by pwolff            #+#    #+#              #
#    Updated: 2024/02/18 10:06:48 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def NULL_not_found(object: any) -> int:

    tab = {
        None: "Nothing",
        float("NaN"): "Garlic",
        "0": "Zero",
        '': "Empty",
        False: "Fake",
    }

    result = tab.get(object, "Type not Found")

    if object == None:
        print(f"{result}: {object} {type(object)}")
    elif result == "Empty":
        print(f"{result}: {type(object)}")
    elif object == 0 and type(object) == int:
        print(f"Zero: {object} {type(object)}")
    elif object == False and type(object) == bool:
        print(f"{result}: {object} {type(object)}")
    elif type(object) == float and object != object:
        print(f"Cheese: {object} {type(object)}")
    else:
        print(result)
        return 1
    
    return 0
        




    # print(tab)
    


