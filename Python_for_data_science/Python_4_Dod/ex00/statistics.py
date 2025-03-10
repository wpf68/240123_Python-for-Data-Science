# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistics.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 08:28:22 by pwolff            #+#    #+#              #
#    Updated: 2025/03/10 09:39:13 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

        


def ft_statistics(*args, **kwargs) -> None:
    """You must take in *args a quantity of unknown number and make the Mean,
        Median, Quartile (25% and 75%), Standard Deviation and Variance
        according to the **kwargs ask.
    You have to manage the errors."""

    if quartile(args) != -1:
        mean(args)
        median(args)
        print("quartile :",quartile(args))

def main():
    pass


if __name__ == "__main__":
    main()

