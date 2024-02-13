from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


# from Loading import ft_tqdm
# for elem in ft_tqdm(range(333)):
#     sleep(0.005)


# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()


# def generateurMultiplicationPar2():
#     maliste = range(4)
#     for i in maliste:
#         yield i*2

# monGenerateur = generateurMultiplicationPar2()
# print(monGenerateur)
# print(type(monGenerateur))
# for i in monGenerateur:
#     print(i)

# print()
# lst = [x * x for x in range(3)]
# print(type(lst))
# for value in lst:
#     print (value)
# print(4 in lst)



# print()
# lst = (x * x for x in range(3))
# print(type(lst))

# for value in lst:
#     print (value)
# print(4 in lst)
# for value in lst:
#     print (value)
# print(4 in lst)

# print()

# monGenerateur = generateurMultiplicationPar2()
# print("Mon generateur 1 : ", next(monGenerateur))
# print("Mon generateur 2 : ", next(monGenerateur))
# print("Mon generateur 3 : ", next(monGenerateur))
# print("Mon generateur 4 : ", next(monGenerateur))
# # print("Mon generateur 5 : ", next(monGenerateur)) # error





print("original tqdm / sleep(0.007)")
for elem in tqdm(range(333)):
    sleep(0.005)
print()

print("ft_tqdm / sleep(0.007)")
for elem in ft_tqdm(range(333)):
    sleep(0.01)