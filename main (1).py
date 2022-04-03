import game
import pygame
import pygame_menu

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((700, 700))

player_name = 0

def MyTextValue(name):
    #on input change your value is returned here
    global player_name
    player_name = name

def start_the_game():
  #Pass player name to database
    print(player_name)
    game.main()

menu = pygame_menu.Menu('Welcome', 700, 700,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Enter Your Name',onchange= MyTextValue)

menu.add.button('Play',start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

#game.main()
