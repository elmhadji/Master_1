def calculate_center_of_class(list):
    sum = 0
    for element in list:
        sum += element
    return sum/len(list)
def min_list (list , type):     
    min_list = []
    match type:
        case 0: # Inter Class
            for index in range(len(list) - 1):
                sub_list_1 = list[index]
                sub_list_2 = list[index + 1]
                min_list.append(abs(sub_list_1[len(sub_list_1)]- sub_list_2[0]))

        case 1: # Intra Class
            for index in range(len(list) - 1):
                sub_list_1 = list[index]
                sub_list_2 = list[index + 1]
                min_list.append(abs(sub_list_1[0]- sub_list_2[len(sub_list_1)]))

        case 2: # Bay Center
            for index in range(len(list) - 1):
                center_sub_list_1 = calculate_center_of_class(list[index])
                center_sub_list_2 = calculate_center_of_class(list[index + 1])
                min_list.append(abs(center_sub_list_1- center_sub_list_2))

    return min_list.index(min(min_list))

def algorithm (list , type):
    while len(list[len(list)]) !=1:
        index_of_min_class = min_list(list , type)
        near_min_class = list[index_of_min_class + 1]
        new_list_of_classes = list[len(list)]
        
        new_list_of_classes.remove(new_list_of_classes[index_of_min_class])
        new_list_of_classes[index_of_min_class] = new_list_of_classes[index_of_min_class] + near_min_class
        list.append(new_list_of_classes)


test = [
    [2],
    [3],
    [4],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [12],
    [13],
    [14],
    [19],
    [22],
    [29],
    [33],
    [34],
    [36],
    [40],
]
# test2 = ["G","H","I",]
# print(test)
# print(test.remove(test[4]))
# print(test)
# print(test+test2)

print(algorithm(test , 0))