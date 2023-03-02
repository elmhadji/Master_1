import numpy as np

a = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
b = np.zeros([5,5])
b = [2,3,4,5,6]



a, b = 0, 5 # intervalle [a,b]
N = 100 # taille des données
X = np.linspace(a, b, N) # abscisses

X_train = X.reshape(-1,1)
#print(X_train)
def t(a):
    a=1
    return a

my_list = [[2], [3], [3], [8,9,10], [11], [12], [13]]

print(sum([2]))

# min_index = my_list.index(min(filter(lambda x: x != 0, my_list)))

# print(min_index)
# import random
# print (random.sample(my_list[1:-1] , len(my_list[1:-1])))
# saved = my_list[1+1]
# saved = my_list[1] + saved
# del my_list[1+1]
# my_list[1] = saved
# min_list = []
# for index ,element in enumerate(my_list[:-1]):
#     result = element[-1] - my_list[index +1][0]
#     min_list.append(abs(result))

# print(my_list)
# print(min_list)


# test.append([[2, 3], [4, 4], [5], [6], [7], [8], [9], [12], [13], [14], [19], [22], [29], [33], [34], [36], [40]])
# test .append([[2, 3, 4, 4], [5], [6], [7], [8], [9], [12], [13], [14], [19], [22], [29], [33], [34], [36], [40]])


# for e in test:
#     print(e)


