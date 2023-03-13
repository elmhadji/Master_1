import pygame
from random import randint


# Define the variables 

window_width , window_height = 900 , 650


city_number = int (input('enter the number of city : ') ) 

city_thickness = 10

cities_cordinates = [(randint(city_thickness , window_width - city_thickness) , \
    randint(city_thickness , window_height - city_thickness))for i in range (city_number)]


# initialize pygame 

pygame.init()   #type:ignore

#Set Up The Window

screen = pygame.display.set_mode((window_width , window_height))
pygame.display.set_caption('TSP using Pygame and the glutton algorithm')



# Define Function 

def draw_city():
    global city_number , screen

    #Clearing the screen 
    screen.fill((0,0,0))
    
    #Drawing the cities 
    for cordinate in cities_cordinates:
        pygame.draw.circle(screen , (255,0,0) , cordinate, city_thickness )

    # First circle is white
    pygame.draw.circle(screen , (255,255,255) , cities_cordinates[0], city_thickness )

    #update the screen 
    pygame.display.update()

def draw_best_road( best_road , road_color_in_rgb):
    global screen , cities_cordinates
    for i in range(len(best_road) - 1 ):
        pygame.draw.line(screen, road_color_in_rgb,cities_cordinates[best_road[i]] , cities_cordinates[best_road[i+1]], 5)

    #update the screen
    pygame.display.update()

def calculate_distance(city_one , city_two):
    from math import sqrt
    return sqrt((city_two[1] - city_one[1])**2 +(city_two[0] - city_one[0])**2) 



#Glutton Algorithme

def glutton_algorithme(city_number , cities_cordinate):
    best_road = None
    distance = 0
    visited = [0]
    remaining = [ i for i in range( 1 , city_number)]
    while remaining:
        current_city = visited[ -1 ]
        min_distance = None
        for next_city in remaining:
            new_distance = calculate_distance(cities_cordinate[current_city] ,cities_cordinate[next_city])
            if min_distance is None or new_distance < min_distance:
                min_distance = new_distance
                nearest_city = next_city
        visited.append(nearest_city) #type:ignore
        remaining.remove(nearest_city) #type:ignore
        distance += min_distance #type:ignore 
    distance +=calculate_distance(cities_cordinate[visited[ -1 ]] , cities_cordinate[ 0 ])
    visited.append(0)
    best_road = visited
    return best_road , distance

# movement type Algorithms :

# 1) exchange 

def best_road_update_exchange ( cities_cordinate , distance ,best_road , number_of_update):
    from  random import sample
    i = 0
    new_distance = distance
    while (i < number_of_update) and (new_distance >= distance):
        new_distance = 0
        # slicing only the middle part of best road (first and last are start point cannot be change)
        middle_of_best_road = best_road[1:-1]
        middle_of_best_road = sample(middle_of_best_road , len(middle_of_best_road))
        # concatinate the 3 list (first element , middle elemnts , last element)
        best_road = best_road[:1] + middle_of_best_road + best_road[-1:]
        # calculating the distance of new solution
        for index , city_cordinate in enumerate(cities_cordinate[:-1]):
            new_distance += calculate_distance(city_cordinate , cities_cordinate[index + 1])  
        i += 1
    return new_distance , best_road

# 2) shift 

def best_road_update_shift ( cities_cordinate , distance ,best_road , number_of_update):
    from  random import randint
    i = 0
    new_distance = distance
    while (i < number_of_update) and (new_distance >= distance):
        new_distance = 0
        # slicing only the middle part of best road (first and last are start point cannot be change)
        middle_of_best_road = best_road[1:-1]
        # save random city and delet it 
        city_index = middle_of_best_road.pop(randint( 0 , len(middle_of_best_road) - 1))
        # insert city in random position 
        middle_of_best_road.insert(randint( 0 , len(middle_of_best_road) - 1) , city_index)
        # concatinate the 3 list (first element , middle elemnts , last element)
        best_road = best_road[:1] + middle_of_best_road + best_road[-1:]
        # calculating the distance of new solution
        for index , city_cordinate in enumerate(cities_cordinate[:-1]):
            new_distance += calculate_distance(city_cordinate , cities_cordinate[index + 1])  
        i += 1
    return new_distance , best_road

# 3) inverse 

def best_road_update_inverse ( cities_cordinate , distance ,best_road , number_of_update):
    from  random import randint
    i = 0
    new_distance = distance
    while (i < number_of_update) and (new_distance >= distance):
        new_distance = 0
        # slicing only the middle part of best road (first and last are start point cannot be change)
        middle_of_best_road = best_road[1:-1]
        # selcting random index 
        start = randint(0 , len(middle_of_best_road) - 1)
        end = randint( start , len(middle_of_best_road) - 1)
        # inverse the list from selected index
        middle_of_best_road[start : end] = reversed(middle_of_best_road[start : end])
        # concatinate the 3 list (first element , middle elemnts , last element)
        best_road = best_road[:1] + middle_of_best_road + best_road[-1:]
        # calculating the distance of new solution
        for index , city_cordinate in enumerate(cities_cordinate[:-1]):
            new_distance += calculate_distance(city_cordinate , cities_cordinate[index + 1])  
        i += 1
    return new_distance , best_road

# The main prgrame

draw_city()

best , dst = glutton_algorithme(city_number , cities_cordinates)
print('best road ={} distance = {}'.format(best , dst))
draw_best_road(best , (255,255,255) )

dst_exchange ,best_road_exchange = best_road_update_exchange(cities_cordinates , dst ,best ,900 )

dst_shift ,best_road_shift = best_road_update_shift(cities_cordinates , dst ,best ,900 )

dst_inverse ,best_road_inverse = best_road_update_inverse(cities_cordinates , dst ,best ,900 )



print('best road using exchange method = {} new distance = {}'.format(best_road_exchange,dst_exchange))

print('best road using shift method = {} new distance = {}'.format(best_road_shift,dst_shift))

print('best road using inverse method = {} new distance = {}'.format(best_road_inverse,dst_inverse))



draw_city()

draw_best_road(best_road_exchange , (255,0,0))


running = True
index_of_switching_road = 1
key_down = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#type:ignore
            running = False

    keys = pygame.key.get_pressed()

    # when we press the key for first time 
    if not key_down and  keys[pygame.K_UP] :#type:ignore
        # print('pressed')
        key_down = True
        if index_of_switching_road == 0:
            draw_city()
            draw_best_road(best_road_exchange , (255,0,0))
            index_of_switching_road = 1
        elif index_of_switching_road == 1:
            draw_city()
            draw_best_road(best_road_shift , (255,0,255))
            index_of_switching_road = 2
        elif index_of_switching_road == 2:
            draw_city()
            draw_best_road(best_road_inverse , (0,255,255))
            index_of_switching_road = 3
        elif index_of_switching_road == 3:
            draw_city()
            draw_best_road(best , (255,255,255))
            index_of_switching_road = 0

    # we change the key_state when we release it 
    elif key_down and not keys[pygame.K_UP]:#type:ignore
        #print("realese")
        key_down = False

        
    
        