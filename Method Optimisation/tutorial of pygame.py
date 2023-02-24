import pygame

pygame.init() # type:ignore 

width  = 900
height = 500

screen = pygame.display.set_mode((width , height))
# Player 
x , y = width/2 , height/2
player_width , player_height = 10 , 20
player_speed_move = 1

#Main Loop
running  = True
  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #type:ignore
            running = False

    # get all the key that have been pressed in keyboard   
    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_LEFT] and x - player_speed_move > 0:#type:ignore
        x -= player_speed_move

    if Keys[pygame.K_RIGHT] and x + player_speed_move + player_width < width:#type:ignore
        x += player_speed_move
    
    if Keys[pygame.K_UP] and y - player_speed_move >0:#type:ignore
        y -= player_speed_move

    if Keys[pygame.K_DOWN] and y + player_speed_move + player_height < height:#type:ignore
        y += player_speed_move

    screen.fill((0,0,0))
    pygame.draw.rect(screen , (255,255,255) , (x ,y ,player_width ,player_height ))
    pygame.display.update()