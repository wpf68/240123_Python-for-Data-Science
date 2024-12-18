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

from S1E9 import Character, Stark


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    print("\n--- Test error ---\n")     # test error
    # hodor = Character("hodor")          # test error
    # print(hodor.__dict__)               # test error

    try:
        hodor = Character("hodor")
        print(hodor.__dict__)
    except Exception as e:
        print(f"\nCaught erronious class stuff: {e}")


if __name__ == "__main__":
    main()
