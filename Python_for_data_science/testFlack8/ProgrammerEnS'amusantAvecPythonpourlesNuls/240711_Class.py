# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240711_Class.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/11 09:22:15 by pwolff            #+#    #+#              #
#    Updated: 2024/07/11 09:47:51 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class test():
    """
        test class dir()
    """
    def __init__(self, name = "Pascal") -> None:
        self.att = "Hello World"
        self.name = name
    def Result(self) -> tuple:
        result = (self.att, self.name)
        return result



inst = test()

print(test())
print(inst)

print(dir(inst))
print(inst.att)
result = (inst.Result())
print(result)

inst2 = test("Daniel")
print(inst2.Result())

