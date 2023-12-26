import pygame
from walking_girl.config import cfg_item
from walking_girl.character import Character
from walking_girl.spritesheet import SpriteSheet

class Animation:

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((cfg_item("animation", "screen_size")[0],cfg_item("animation", "screen_size")[1]),0,32)
        pygame.display.set_caption(cfg_item("animation","caption"))
        clock = pygame.time.Clock()
        sprite_sheet = SpriteSheet(cfg_item("entities","spritesheet_path"), 2, 10)  # 2 rows, 10 columns
        character = Character(sprite_sheet)

        running = True
        last_update = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            now = pygame.time.get_ticks()
            delta_time = (now - last_update)/ 1000.0 # Delta time en segundos
            
            character.update(delta_time)

            last_update = now

            screen.fill((0, 0, 0))
            character.draw(screen)

            pygame.display.update()
            clock.tick(cfg_item("animation","sync","fps")) # Intenta mantener 60 FPS

        pygame.quit()