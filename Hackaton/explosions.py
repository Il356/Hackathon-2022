import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

animation_count = 0
explosions = []
clock = pygame.time.Clock()
is_explosion = False
current_explosion_pos = -1

for i in range(6):
    new_file_name = "blowup" + str(i + 1) + ".png"
    explosions.append(pygame.image.load(new_file_name))

is_running = True
while is_running:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if animation_count == 0:
                is_explosion = True
                current_pos = pygame.mouse.get_pos()
        if is_explosion:
            screen.blit(explosions[animation_count // 4], current_pos)
            animation_count += 1
            
            if animation_count >= 24:
                animation_count = 0
                is_explosion = False
        
        pygame.display.update()
        screen.fill((0, 0, 0))
            
pygame.quit()
