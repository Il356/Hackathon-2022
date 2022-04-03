import pygame
import game_board

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
BORDER_LENGTH = 50

EDITOR_BOARD_SIZE = WINDOW_HEIGHT - 4 * BORDER_LENGTH
SHIP_WIDTH = 80
SHIP_HEIGHT = 240

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 175, 255)

myBoard = game_board.Board()

def modify_ship(tile_pos, blockSize):
    blockSize *= 1.13
    x_scaling = blockSize - 10
    y_scaling = blockSize * max(tile_pos)
    is_rotate = not tile_pos[0] == 1
    
    return (x_scaling, y_scaling, is_rotate)

def main():
    global screen, CLOCK, my_font, ship_image
    pygame.init()
    pygame.font.init()
    
    my_font = pygame.font.SysFont('Comic Sans MS', 15)
        
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    screen.fill(BLUE)
    ship_image = pygame.image.load("ship.png")
    
    while True:
        drawGrid(myBoard)
        create_editor()
        CLOCK.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 675 > pos[0] > 575 and 625 > pos[1] > 575:
                  print("RESET")
                  create_editor()
                if 675 > pos[0] > 575 and 675 > pos[1] > 625:
                  print("SUBMIT")

        pygame.display.update()

def drawGrid(board):
    global blockSize
    blockSize = (WINDOW_HEIGHT - 4 * BORDER_LENGTH) // board.size
    
    for i in range(board.size):
        current_letter = game_board.alphabet[i]
        textsurface = my_font.render(current_letter, False, BLACK)
        screen.blit(textsurface, (BORDER_LENGTH * 3/2 + blockSize * i, BORDER_LENGTH / 2))
    
    for j in range(board.size):
        textsurface = my_font.render(str(j + 1), False, BLACK)
        screen.blit(textsurface, (BORDER_LENGTH / 2, BORDER_LENGTH * 3/2 + blockSize * j))

    for i in range(board.size):
        x_pos = i * blockSize + BORDER_LENGTH
        for j in range(board.size):
            y_pos = j * blockSize + BORDER_LENGTH
            rect = pygame.Rect(x_pos, y_pos, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

def create_editor():
    x_ships_rect = pygame.Rect(BORDER_LENGTH, WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, EDITOR_BOARD_SIZE, 2 * BORDER_LENGTH)
    pygame.draw.rect(screen, WHITE, x_ships_rect, 1)
    
    x_ship_sizes = [(5, 1), (2, 1)]
    previous_x = 0.5
    for new_modifier in x_ship_sizes:
        modifier = modify_ship(new_modifier, blockSize)
        if modifier[-1]:
            new_ship = pygame.transform.scale(ship_image, modifier[:2])
            new_ship = pygame.transform.rotate(new_ship, 90)
        else:
            new_ship = pygame.transform.scale(ship_image, modifier[:2])
            
        screen.blit(new_ship, (BORDER_LENGTH + (previous_x - 0.5) * SHIP_WIDTH, WINDOW_HEIGHT - 2.5 * BORDER_LENGTH))
        previous_x = new_modifier[0]

    x_ship_sizes = [(3, 1), (4, 1)]
    previous_x = 0.5
    for new_modifier in x_ship_sizes:
        modifier = modify_ship(new_modifier, blockSize)
        if modifier[-1]:
            new_ship = pygame.transform.scale(ship_image, modifier[:2])
            new_ship = pygame.transform.rotate(new_ship, 90)
        else:
            new_ship = pygame.transform.scale(ship_image, modifier[:2])
            
        screen.blit(new_ship, (BORDER_LENGTH + (previous_x - 0.5) * SHIP_WIDTH, WINDOW_HEIGHT - 1.5 * BORDER_LENGTH))
        previous_x = new_modifier[0]
    
    
    y_ships_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, BORDER_LENGTH, 2 * BORDER_LENGTH, EDITOR_BOARD_SIZE)
    pygame.draw.rect(screen, WHITE, y_ships_rect, 1)

    y_ship_sizes = [(5, 1), (2, 1)]
    previous_y = 0.5
    for new_modifier in y_ship_sizes:
        modifier = modify_ship(new_modifier, blockSize)
        
        new_ship = pygame.transform.scale(ship_image, modifier[:2])

        #y_ships_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, BORDER_LENGTH,
        screen.blit(new_ship,(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, BORDER_LENGTH+ (previous_y - 0.5)* SHIP_WIDTH))
        #screen.blit(new_ship, (BORDER_LENGTH + (previous_y - 0.5) * SHIP_WIDTH, WINDOW_HEIGHT - 2.5 * BORDER_LENGTH))
        previous_y = new_modifier[0]

    y_ship_sizes = [(3, 1), (4, 1)]
    previous_y = 0.5
    for new_modifier in y_ship_sizes:
        modifier = modify_ship(new_modifier, blockSize)
        
        new_ship = pygame.transform.scale(ship_image, modifier[:2])

        #y_ships_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, BORDER_LENGTH,
        screen.blit(new_ship,(WINDOW_HEIGHT - 1.5 * BORDER_LENGTH, BORDER_LENGTH+ (previous_y - 0.5)* SHIP_WIDTH))
        #screen.blit(new_ship, (BORDER_LENGTH + (previous_y - 0.5) * SHIP_WIDTH, WINDOW_HEIGHT - 2.5 * BORDER_LENGTH))
        previous_y = new_modifier[0]

    reset_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, BORDER_LENGTH*2, BORDER_LENGTH)
    pygame.draw.rect(screen, RED, reset_rect)
    my_font = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = my_font.render("RESET", False, BLACK)
    screen.blit(textsurface, (WINDOW_HEIGHT - 2.35 * BORDER_LENGTH, WINDOW_HEIGHT - 2.25 * BORDER_LENGTH))

    submit_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, WINDOW_HEIGHT - 1.5 * BORDER_LENGTH, BORDER_LENGTH*2, BORDER_LENGTH)
    pygame.draw.rect(screen, BLACK, submit_rect)

    my_font = pygame.font.SysFont('Comic Sans MS', 35)
    textsurface = my_font.render("SUBMIT", False, WHITE)
    screen.blit(textsurface, (WINDOW_HEIGHT - 2.4 * BORDER_LENGTH, WINDOW_HEIGHT - 1.25 * BORDER_LENGTH))
    
    
def get_tile_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - (BORDER_LENGTH, BORDER_LENGTH)
    
    