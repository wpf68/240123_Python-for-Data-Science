# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 06:48:57 by pwolff            #+#    #+#              #
#    Updated: 2024/02/06 07:54:08 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def all_thing_is_obj(object: any) -> int:
    result = type(object)

    if result == list:
        print(f"List : {type(object)}")
    elif result == tuple:
        print(f"Tuple : {type(object)}")
    elif result == set:
        print(f"Set : {type(object)}")
    elif result == dict:
        print(f"Dict : {type(object)}")
    elif result == str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
        
    return 42

"""
    Pas réussi avec match / case

    Possible de mettre les "List - Tuple ..." dans un dict pour
    reduire le nombre de elif.

    ------------------------------------------------------------
    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")


    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")
    else:
        print(f"{type_name}")

    return 42
    ----------------------------------------------------------
"""
