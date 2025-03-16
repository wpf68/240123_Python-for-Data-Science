# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistics.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 08:28:22 by pwolff            #+#    #+#              #
#    Updated: 2025/03/16 09:34:21 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# from math import sqrt

def mean(args):
    """Calculation of the average"""
    # sum = 0
    # for val in args:
    #     sum += val
    if len(args) == 0:
        # print("ERROR")
        return -1
    print("mean :", sum(args) / len(args))

def median(args):
    """Calculation of the median value"""
    if int(len(args) % 2) == 0:
        # print("ERROR")
        return -1
    tri = sorted(args)
    pos= int((len(tri) + 1)/2) - 1
    print("median :",tri[pos])

def quartile(args):
    """Quartile calculation"""
    if int(len(args) % 2) == 0:
        # print("ERROR")
        return -1
    tri = sorted(args)
    pos = int((len(tri) + 1)/2) - 1
    if (int(pos + 1) % 2) == 0:
        # print("ERROR")
        return -1
    pos1 = int(((pos + 2) / 2) - 1)
    listQuartile = [float(tri[pos1]), float(tri[pos + pos1])]
    return listQuartile

        
def stdDeviation(args):
    m = mean(args)
    result = sqrt(sum([(x - m) ** 2 for x in args]) / len(args))
    print('std :', result)


def ft_statistics(*args, **kwargs) -> None:
    """You must take in *args a quantity of unknown number and make the Mean,
        Median, Quartile (25% and 75%), Standard Deviation and Variance
        according to the **kwargs ask.
    You have to manage the errors."""

    result = []
    for key, value in kwargs.items():
        # print ("dictionaire : ", key, " : ", value)
        result.append(value)
        
    # print(result)
        


    if quartile(args) != -1:
        if 'mean' in result:
            mean(args)
        if 'median' in result:
            median(args)
        if 'quartile' in result:
            print("quartile :",quartile(args))


    if 'std' in result and len(args) != 0:
        stdDeviation(args)
        print("std")

def main():
    pass


if __name__ == "__main__":
    main()

