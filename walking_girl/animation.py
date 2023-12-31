import pygame
from walking_girl.assets.sound_manager import SoundManager
from walking_girl.config import Config, cfg_item
from walking_girl.entities.character import Character
from walking_girl.assets.spritesheet import SpriteSheet

class Animation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(cfg_item("animation", "screen_size"))
        pygame.display.set_caption(cfg_item("animation", "caption"))
        self.clock = pygame.time.Clock()
        self.spritesheet_rows, self.spritesheet_columns = cfg_item("entities", "spritesheet_structure", "rows"),cfg_item("entities", "spritesheet_structure", "columns")
        self.sprite_sheet = SpriteSheet(cfg_item("entities", "spritesheet_path"), 2, 10)  # 2 rows, 10 columns
        self.sound_manager = SoundManager()
        self.character = Character(self.sprite_sheet, self.sound_manager)
        self.last_update = pygame.time.get_ticks()
        self.delta_time = 0
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(cfg_item("animation", "sync", "fps"))
            self.__handle_input()
            self.__update()
            self.__render()

        self.__quit()

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_F5:
                    Config.get_instance().debug = not Config.get_instance().debug
                self.character.handle_input(event.key, True)
                pass
            if event.type == pygame.KEYUP:
                self.character.handle_input(event.key, False)
                
    def __update(self):
        now = pygame.time.get_ticks()
        self.delta_time = (now - self.last_update) / 1000.0  # Delta time in seconds
        self.character.update(self.delta_time)
        self.last_update = now

    def __render(self):
        self.screen.fill(cfg_item("animation", "bg_color"))
        self.character.draw(self.screen)
        pygame.display.update()

    def __quit(self):
        pygame.quit()
