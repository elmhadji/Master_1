import numpy as np


#Function define

def calculate_distance ( start , end):
    return np.sqrt((end[1] - start[1])**2 +(end[0] - start[0])**2)

def create_obstacle(table , number_of_obstacle):
    from random import randint
    index = 0
    
    while index < number_of_obstacle:
        x = randint(0 , 3)
        y = randint(0 , 5)
        if table[x][y] != "":
            table[x][y] = ""
            index += 1
    return table



    
def greedy_algorithm(table , start_point , destination):
    #distance = calculate_distance(start_point , destination)
    road = []
    road_cordonate = []
    road.append(table[ start_point[0] ][ start_point[1]])
    road_cordonate.append(start_point)
    while start_point != destination:

        distances = [

            calculate_distance(start=(start_point[0] - 1 , start_point[1] - 1) ,end = destination) \
                if (start_point[0] - 1 >= 0 and start_point[1] - 1 >= 0) and \
                    (table[start_point[0] - 1][start_point[1] - 1] != "")  else -1 ,

            calculate_distance(start=(start_point[0] - 1 , start_point[1]) ,end = destination) \
                if (start_point[0] - 1 >= 0 ) and \
                    (table[start_point[0] - 1][start_point[1]] != "") else -1 ,
            
            calculate_distance(start=(start_point[0] - 1 , start_point[1] + 1) ,end = destination) \
                if (start_point[0] - 1 >= 0 and start_point[1] + 1 <6) and \
                    (table[start_point[0] - 1][start_point[1] + 1] != "") else -1 ,

            calculate_distance(start=(start_point[0] , start_point[1] - 1) ,end = destination) \
                if (start_point[1] - 1 >= 0) and \
                    (table[start_point[0]][start_point[1] - 1] != "") else -1 ,    

            calculate_distance(start=(start_point[0] , start_point[1] + 1) ,end = destination) \
                if (start_point[1] + 1 < 6) and \
                    (table[start_point[0]][start_point[1] + 1] != "") else -1 ,

            calculate_distance(start=(start_point[0] + 1 , start_point[1] - 1) ,end = destination) \
                if (start_point[0] + 1 < 4 and start_point[1] - 1 >= 0) and \
                    (table[start_point[0] + 1][start_point[1] - 1] != "") else -1 ,

            calculate_distance(start=(start_point[0] + 1 , start_point[1]) ,end = destination) \
                if (start_point[0] + 1 < 4) and \
                    (table[start_point[0] + 1][start_point[1]] != "") else -1 ,

            calculate_distance(start=(start_point[0] + 1 , start_point[1] + 1) ,end = destination) \
                if (start_point[0] + 1 < 4 and start_point[1] + 1 < 6) and \
                    (table[start_point[0] + 1][start_point[1] + 1] != "") else -1 ,
            
        ]

        min_index = distances.index(min(filter(lambda x: x != -1, distances)))

        match min_index:
            case 0:
                start_point = (start_point[0] - 1 , start_point[1] - 1)
            case 1:
                start_point = (start_point[0] - 1 , start_point[1])
            case 2:
                start_point = (start_point[0] - 1 , start_point[1] + 1)
            case 3:
                start_point = (start_point[0] , start_point[1] - 1)
            case 4:
                start_point = (start_point[0] , start_point[1] + 1)
            case 5:
                start_point = (start_point[0] + 1 , start_point[1] - 1)
            case 6:
                start_point = (start_point[0] + 1 , start_point[1])
            case 7:
                start_point = (start_point[0] + 1 , start_point[1] + 1)
            case _:
                break

        road.append(table[ start_point[0] ][ start_point[1]])
        road_cordonate.append(start_point)


    return road , road_cordonate


# Variables

table  = [
    ["A" , "B" , "C" , "D" , "E" , "F"],
    ["G" , "H" , "I" , "J" , "K" , "L"],
    ["M" , "N" , "O" , "P" , "Q" , "R"],
    ["S" , "T" , "U" , "V" , "W" , "X"],
]
table = np.array(table)

table = create_obstacle(table , 10)

from random import randint

destination_x = randint(0 , 3)
destination_y = randint(0 , 5)

while table[destination_x][destination_y] == "":
    destination_x = randint(0 , 3)
    destination_y = randint(0 , 5)

destination = ( destination_x , destination_y )

start_x = randint(0 , 3)
start_y = randint(0 , 5)

while (table[start_x][start_y] == "") or \
        (destination_x == start_x and destination_y == start_y):
    start_x = randint(0 , 3)
    start_y = randint(0 , 5)

start_point = ( start_x , start_y )

# start_point = ( 2 , 0 )
# destination = ( 3 , 5 )



print('start point =',start_point ,'destination = ',destination)
print( 'start point =',table[start_point[0]][start_point[1]])
print('destination = ',table[destination[0]][destination[1]])

road , road_coordinate = greedy_algorithm(table , start_point , destination)
print('best_road = ',road)
print('best_road codination = ',road_coordinate)
# print('\n',table)

#print(road_cordinate[0][0] , road_coordinate[0][1])




import matplotlib.pyplot as plt

for i in range (4):
    for j in range(6):
        if table[i][j] !="":
            plt.scatter(j, i , color = 'blue')
            plt.text(j, i , table[i][j] )
        else:
            plt.scatter(j, i , color = 'red')
            plt.text(j, i , table[i][j] )


road_cordinate_y , road_cordinate_x = zip(*road_coordinate)
#print('cordx',road_cordinate_x , 'cordy',road_cordinate_y)
plt.plot(road_cordinate_x, road_cordinate_y , '-o')


plt.show()