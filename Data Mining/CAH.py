def get_min_list (list_of_substruction):
    min_element = min(list_of_substruction)
    index_min_element = list_of_substruction.index(min_element)
    list_of_min_index = [list_of_substruction.index(min_element)]
    for index in range(index_min_element + 1 , len(list_of_substruction)):
        if list_of_substruction[index] == min_element and index - 1 != list_of_min_index[-1]:
            list_of_min_index.append(index)    
    return list_of_min_index

def get_median_class (list_of_classes):
    result = [sum (classe)/len(classe) for classe in list_of_classes ]
    return result

def get_subtruction_list (list_of_classes , type):
    min_list = []
    if type == 0:#Inter Class
        for index , classe in enumerate(list_of_classes[:-1]):
            result = abs(classe[-1] - list_of_classes[index + 1][0])
            min_list.append(result)
    elif type == 1:#Intra Class
        for index , classe in enumerate(list_of_classes[:-1]):
            result = abs(classe[0] - list_of_classes[index + 1][-1])
            min_list.append(result)
    elif type == 2:#Bay Center
        median_classes = get_median_class(list_of_classes)
        for index , classe in enumerate(median_classes[:-1]):
            result = abs(classe - median_classes[index + 1])
            min_list.append(result)
    return min_list

def CAH_algorithme (list_of_classes , type):
    new_classes = [list_of_classes.copy()]
    while len(list_of_classes) != 1 :
        list_of_substuction = get_subtruction_list(list_of_classes , type)
        list_of_min_index = get_min_list(list_of_substuction)
        for index ,index_of_min_class in enumerate(list_of_min_index):
            #index_of_min_class = list_of_substuction.index(min(list_of_substuction))
            #saving the neigbor class
            neigbor_class = list_of_classes[index_of_min_class + 1 - index]
            #new class
            neigbor_class = list_of_classes[index_of_min_class - index] + neigbor_class
            # deleting the old class
            del list_of_classes[index_of_min_class + 1 -index ]
            list_of_classes[index_of_min_class - index] = neigbor_class           
        new_classes.append(list_of_classes.copy())
    return new_classes

def string_to_list_of_sublist(string):
    
    return [[int(element)] for element in string.split(',')]
    
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

# result = CAH_algorithme(test , 0)
# for index , element in enumerate(result):
#     print(index,element)