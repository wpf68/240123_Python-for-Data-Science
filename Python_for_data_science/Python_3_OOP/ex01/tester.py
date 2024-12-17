# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/17 10:03:47 by pwolff            #+#    #+#             #
#    Updated: 2024/12/17 13:00:33 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

# https://github.com/zstenger93/python_piscine
# https://github.com/znichola/piscine-python/tree/main/python_for_data_science

from S1E7 import Baratheon, Lannister


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}" +
          f", Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
