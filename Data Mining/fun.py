def get_median_class (list_of_classes):
    result = [sum (classe)/len(classe) for classe in list_of_classes ]
    return result

def get_subtruction_list (list_of_classes , type):
    min_list = []
    match type:
        case 0:#Inter Class
            for index , classe in enumerate(list_of_classes[:-1]):
                result = abs(classe[-1] - list_of_classes[index + 1][0])
                min_list.append(result)
        case 1:#Intra Class
            for index , classe in enumerate(list_of_classes[:-1]):
                result = abs(classe[0] - list_of_classes[index + 1][-1])
                min_list.append(result)
        case 2:#Bay Center
            median_classes = get_median_class(list_of_classes)
            for index , classe in enumerate(median_classes[:-1]):
                result = abs(classe - median_classes[index + 1])
                min_list.append(result)
        case _:
            pass

    return min_list

def CAH_algorithme (list_of_classes , type):
    new_classes = [list_of_classes.copy()]
    i=0
    while len(list_of_classes) != 1 :
        list_of_substuction = get_subtruction_list(list_of_classes , type)
        # print(list_of_substuction)
        #TODO: to upgrade the algorithm make it slecte all the same min value in one iteration
        index_of_min_class = list_of_substuction.index(min(list_of_substuction))
        #saving the neigbor class
        neigbor_class = list_of_classes[index_of_min_class + 1]
        #new class
        neigbor_class = list_of_classes[index_of_min_class] + neigbor_class
        # deleting the old class
        del list_of_classes[index_of_min_class + 1]
        list_of_classes[index_of_min_class] = neigbor_class
        new_classes.append(list_of_classes.copy())
    return new_classes


test = [
    [1],
    [1],
    [2],
    [3],
    [5],
    [5],
    [6],
    [9],
    [9],
    [14],
    [14],
    [17],
    [21],
    [27],
    [30],
    [40],
]
# print(len(test))
# test2 = ["G","H","I",]
# print(test)
# print(test.remove(test[4]))
# print(test)
# print(test+test2)
result = CAH_algorithme(test , 2)
for index , element in enumerate(result):
    print(index,element)


# for element in CAH_algorithme(test , 0):
#     print(element)

# print(len(CAH_algorithme(test , 0)))