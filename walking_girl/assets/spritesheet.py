from importlib import resources
import pygame

class SpriteSheet:
    def __init__(self, file_path, rows, columns):
        with resources.path(file_path[0], file_path[1]) as image_filename:
            self.sprite_sheet = pygame.image.load(image_filename).convert_alpha()
        self.rows = rows
        self.columns = columns
        self.rect = self.sprite_sheet.get_rect()
        self.frame_width = self.rect.width // columns
        self.frame_height = self.rect.height // rows

    def get_image(self, row, column):
        frame = pygame.Rect(column * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height)
        image = pygame.Surface(frame.size).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), frame)
        image.set_colorkey((0,0,0))
        return image
