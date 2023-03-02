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

my_list = [2, 3, 8, 3, 9, 2, 0]
# min_index = my_list.index(min(filter(lambda x: x != 0, my_list)))

# print(min_index)
import random
print (random.sample(my_list[1:-1] , len(my_list[1:-1])))