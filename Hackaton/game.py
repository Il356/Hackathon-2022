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
GREEN = (0, 255, 0)
BOARD_OFFSET = 10

myBoard = game_board.Board()

is_ship_selected = False
selected_ship_text = ""
error_text = ""

def modify_ship(tile_pos, blockSize):
    blockSize *= 1.13
    x_scaling = blockSize - 10
    y_scaling = blockSize * max(tile_pos)
    is_rotate = not tile_pos[0] == 1
    
    return (x_scaling, y_scaling, is_rotate)

def main():
    global screen, CLOCK, my_font, ship_image, selected_ship_text, error_text
    pygame.init()
    pygame.font.init()
    error_time = 0
    my_font = pygame.font.SysFont('Comic Sans MS', 15)
        
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    screen.fill(BLUE)
    ship_image = pygame.image.load("ship.png")
    selected_ship = 0
    x = None
    y = None
    while True:
        screen.fill(BLUE)
        drawGrid(myBoard)
        create_editor()
        CLOCK.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 675 > pos[0] > 575 and 625 > pos[1] > 575:
                   print("RESET")
                   is_ship_selected = False
                   selected_ship_text = ""
                   
                   for letter in game_board.alphabet[:myBoard.size]:
                       for num in game_board.numbers[:myBoard.size]:
                           myBoard.board[letter + str(num)] = 0
                        
                if 675 > pos[0] > 575 and 675 > pos[1] > 625:
                   print("SUBMIT")

                if select_ship(myBoard) is not None:
                    current_selected_ship = selected_ship
                    selected_ship_text = str(selected_ship[0]) + " Horizontal" if selected_ship[1] == "H" \
                        else str(selected_ship[0]) + " Vertical"
                    is_ship_selected = True
                
            if event.type == pygame.MOUSEBUTTONUP:
                if is_ship_selected and x != None:
                    myBoard.board[chr(x + 65) + str(y + 1)] = current_selected_ship
                    
                    if myBoard.check_overlap():
                        myBoard.board[chr(x + 65) + str(y + 1)] = 0
                        error_text = "OVERLAP!!"
                        error_time = pygame.time.get_ticks()
                        
                    myBoard.print_board()
                    
                    selected_ship_text = ""
                    current_selected_ship = None
        if abs(error_time - pygame.time.get_ticks()) >= 1000:
            error_text = ""
        
        x, y = get_tile_under_mouse(myBoard)
        if x != None:
            new_rect = (BORDER_LENGTH + x * blockSize, BORDER_LENGTH + y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, RED, new_rect, 2)
        else:
            selected_ship = select_ship(myBoard)
            
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
            
            new_value = list(board.board.values())[board.size * i + j]
            if new_value != 0:
                new_image = pygame.transform.scale(ship_image, modify_ship((new_value[0], 1), blockSize)[:2])
                if new_value[1] == "H":
                    new_image = pygame.transform.rotate(new_image, 90)
                screen.blit(new_image, (x_pos, y_pos))
    
    

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
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = my_font.render("RESET", False, BLACK)
    screen.blit(textsurface, (WINDOW_HEIGHT - 2.35 * BORDER_LENGTH, WINDOW_HEIGHT - 2.25 * BORDER_LENGTH))

    submit_rect = pygame.Rect(WINDOW_HEIGHT - 2.5 * BORDER_LENGTH, WINDOW_HEIGHT - 1.5 * BORDER_LENGTH, BORDER_LENGTH*2, BORDER_LENGTH)
    pygame.draw.rect(screen, BLACK, submit_rect)

    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = my_font.render("SUBMIT", False, WHITE)
    screen.blit(textsurface, (WINDOW_HEIGHT - 2.4 * BORDER_LENGTH, WINDOW_HEIGHT - 1.25 * BORDER_LENGTH))
    
    textsurface = my_font.render("Selected Ship: " + selected_ship_text + error_text, False, BLACK)
    screen.blit(textsurface, (BORDER_LENGTH, EDITOR_BOARD_SIZE + BORDER_LENGTH))
    
def get_tile_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - (BORDER_LENGTH, BORDER_LENGTH)
    x, y = [int(v // blockSize) for v in mouse_pos]
    try:
        if x >= 0 and x < board.size and y >= 0 and y < board.size: return  (x, y)
    except IndexError: pass
    return None, None

def select_ship(board: game_board.Board, colour = RED):
    if get_tile_under_mouse(board)[0] != None:
        return
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    
    horizantal_ships_rect = pygame.Rect(BORDER_LENGTH, 1.5 * BORDER_LENGTH + EDITOR_BOARD_SIZE, \
                        EDITOR_BOARD_SIZE, 2 * BORDER_LENGTH)
        
    vertical_ships_rect = pygame.Rect(EDITOR_BOARD_SIZE + 1.5 * BORDER_LENGTH, BORDER_LENGTH, \
                      2 * BORDER_LENGTH, EDITOR_BOARD_SIZE)
    
    if horizantal_ships_rect.collidepoint(mouse_pos):
        h_ship5 = (pygame.Rect(BORDER_LENGTH, EDITOR_BOARD_SIZE + 1.5 * BORDER_LENGTH, \
                            EDITOR_BOARD_SIZE * 5 / 7, BORDER_LENGTH), (5, "H"))
        h_ship2 = (pygame.Rect(BORDER_LENGTH + EDITOR_BOARD_SIZE * 5 / 7, EDITOR_BOARD_SIZE + 1.5 * BORDER_LENGTH, \
                            EDITOR_BOARD_SIZE * 2 / 7, BORDER_LENGTH), (2, "H"))
        h_ship3 = (pygame.Rect(BORDER_LENGTH, EDITOR_BOARD_SIZE + 2.5 * BORDER_LENGTH, \
                            EDITOR_BOARD_SIZE * 3 / 7, BORDER_LENGTH), (3, "H"))
        h_ship4 = (pygame.Rect(BORDER_LENGTH + EDITOR_BOARD_SIZE * 3 / 7 , EDITOR_BOARD_SIZE + 2.5 * BORDER_LENGTH, \
                            EDITOR_BOARD_SIZE * 4 / 7, BORDER_LENGTH), (4, "H"))
            
        horizontal_ships = [h_ship5, h_ship2, h_ship3, h_ship4]
        
        for ship in horizontal_ships:
            if ship[0].collidepoint(mouse_pos):
                pygame.draw.rect(screen, colour, ship[0], 2)
                return ship[1]
    if vertical_ships_rect.collidepoint(mouse_pos):
        v_ship5 = (pygame.Rect(EDITOR_BOARD_SIZE + 1.5 * BORDER_LENGTH, BORDER_LENGTH, \
                            BORDER_LENGTH, EDITOR_BOARD_SIZE * 5 / 7), (5, "V"))
        v_ship2 = (pygame.Rect(EDITOR_BOARD_SIZE + 1.5 * BORDER_LENGTH, BORDER_LENGTH + EDITOR_BOARD_SIZE * 5 / 7, \
                            BORDER_LENGTH, EDITOR_BOARD_SIZE * 2 / 7), (2, "V"))
        v_ship3 = (pygame.Rect(EDITOR_BOARD_SIZE + 2.5 * BORDER_LENGTH, BORDER_LENGTH, \
                            BORDER_LENGTH, EDITOR_BOARD_SIZE * 3 / 7), (3, "V"))
        v_ship4 = (pygame.Rect(EDITOR_BOARD_SIZE + 2.5 * BORDER_LENGTH, BORDER_LENGTH + EDITOR_BOARD_SIZE * 3 / 7, \
                            BORDER_LENGTH, EDITOR_BOARD_SIZE * 4 / 7), (4, "V"))
            
        vertical_ships = [v_ship5, v_ship2, v_ship3, v_ship4]
        for ship in vertical_ships:
            if ship[0].collidepoint(mouse_pos):
                pygame.draw.rect(screen, colour, ship[0], 2)
                return ship[1]
    return