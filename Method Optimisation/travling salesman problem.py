import pygame
from random import randint

# initialize pygame 

pygame.init()   #type:ignore

#Set Up The Window

window_width , window_height = 900 , 650
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

def draw_best_road( best_road):
    global screen , cities_cordinates
    for i in range(len(best_road) - 1 ):
        pygame.draw.line(screen, (255,255,255),cities_cordinates[best_road[i]] , cities_cordinates[best_road[i+1]], 5)

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


def best_road_update ( cities_cordinate , distance ,best_road , number_of_update):
    from  random import sample
    i = 0
    new_distance = distance
    while (i < number_of_update) and (new_distance >= distance):
        new_distance = 0
        #slicing only the middle part of best road 
        middle_of_best_road = best_road[1:-1]
        middle_of_best_road = sample(middle_of_best_road , len(middle_of_best_road))
        #concatinate the 3 list (first element , middle elemnts , last element)
        best_road = best_road[:1] + middle_of_best_road + best_road[-1:]
        best_road = best_road
        for index , city_cordinate in enumerate(cities_cordinate[:-1]):
            new_distance += calculate_distance(city_cordinate , cities_cordinate[index + 1])  
        i += 1
        #print(new_distance)
    return new_distance , best_road





# Define the variables 

city_number = 8

city_thickness = 10

cities_cordinates = [(randint(city_thickness , window_width - city_thickness) , \
    randint(city_thickness , window_height - city_thickness))for i in range (city_number)]



# The main prgrame

draw_city()

best , dst = glutton_algorithme(city_number , cities_cordinates)
print('best road =',best,'distance = ',dst)
draw_best_road(best) 

dst ,best = best_road_update(cities_cordinates , dst ,best ,900 )

print('new best road =',best,'new distance = ',dst)


# def TSP (city_number , cities_cordinates):
#     from numpy import zeros
#     road_taken = zeros([city_number , city_number])
#     total_distance = 0
#     for i in range(city_number):
#         city_cord = cities_cordinates[i]
#         distence_to_next_city = []
#         if i != city_number-1 : # TODO; change the condition 
#             for j in range(i+1 , city_number):
#                 next_city_cord = cities_cordinates[j]
#                 distence_to_next_city.append(calculate_distance(city_cord , next_city_cord))
#             # get the min distance between city and there index
#             print('i = ',i,'distance to next city:',distence_to_next_city )

#             index , distance = calculate_min_distance(distence_to_next_city)
            
#             total_distance += distance
#             print('index = ',index,'min distance to next city:',distance )

#             pygame.draw.line(screen, (255,255,255),cities_cordinates[i] , cities_cordinates[index+i+1], 5)
#     print('total distance = ',total_distance)





# Drawing the Lines between cities
# for index,cordinate in enumerate(cities_cordinates):
#     i = index
#     if index != city_number-1:
#         i = index + 1
#     pygame.draw.line(screen , (255,255,0) , cordinate ,cities_cordinates[i] , 5)
#     print('index:',index,'cordinate:',cordinate)
# pygame.draw.line(screen, (255,255,255),cities_cordinates[city_number-1] , cities_cordinates[0], 5)


pygame.display.update()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#type:ignore
            running = False
        
    
        