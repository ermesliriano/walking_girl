from importlib import resources
import pygame

from walking_girl.assets.sound_manager import SoundManager

from walking_girl.config import cfg_item

class Character:
    def __init__(self, sprite_sheet, sound_manager):
        self.screen_width, self.screen_height = cfg_item("animation", "screen_size")[0],cfg_item("animation", "screen_size")[1]
        self.x_pos = 0
        self.y_pos = self.screen_height - sprite_sheet.frame_height
        self.speed = cfg_item("entities", "girl", "speed")
        self.frames_per_action = cfg_item("entities", "frames_per_action")
        self.frame = 0
        self.smooth = 0
        self.direction = 'right'
        self.last_direction = self.direction
        self.sprite_sheet = sprite_sheet
        self.walk_right = [self.sprite_sheet.get_image(0, i) for i in range(1, self.frames_per_action + 1)]
        self.walk_left = [self.sprite_sheet.get_image(1, i) for i in range(1, self.frames_per_action + 1)]
        self.stand_frame_right = self.sprite_sheet.get_image(0, 0)
        self.stand_frame_left = self.sprite_sheet.get_image(1, 0)
        self.sound_path = cfg_item("entities", "sound_path")
        self.sound_manager = sound_manager
        self.sound_manager.load_sound('step', self.sound_path)
        self.sound_played = False
        pygame.mixer.init()
        with resources.path(self.sound_path[0], self.sound_path[1]) as sound_filename:
            self.step_sound = pygame.mixer.Sound(sound_filename)

    def handle_input(self, key, is_pressed):
        if key == pygame.K_LEFT:
            self.last_direction = self.direction if self.direction == 'anyone' else None
            self.direction = 'left'
        if key == pygame.K_RIGHT:
            self.last_direction = self.direction if self.direction == 'anyone' else None
            self.direction = 'right'
        if key == pygame.K_SPACE:
            if self.direction == 'anyone':
                pass
            else:
                self.last_direction = self.direction
                self.direction = 'anyone'

    def update(self, delta_time):
        if self.direction == 'anyone':
            pass
        else:
            self.x_pos += self.speed * delta_time if self.direction == 'right' else -self.speed * delta_time
            if (self.smooth == cfg_item("entities", "girl", "smooth")):
                self.frame += 1
                self.sound_played = False
                self.smooth = 0
            else:
                self.smooth += 1
            if self.frame >= len(self.walk_right):
                self.frame = 0

            if self.x_pos <= 0 and self.direction == 'left':
                self.last_direction = self.direction
                self.direction = 'right'
                self.x_pos = 0
            elif self.x_pos + self.sprite_sheet.frame_width >= self.screen_width and self.direction == 'right':
                self.last_direction = self.direction
                self.direction = 'left'
                self.x_pos = self.screen_width - self.sprite_sheet.frame_width

            if (((self.frame == ((self.frames_per_action//2)-1)) or (self.frame == (self.frames_per_action - 1))) and (self.sound_played == False)):
                self.sound_manager.play_stereo('step', self.x_pos, self.screen_width)
                self.sound_played = True

    def draw(self, screen):
        if self.direction == 'anyone':
            image = self.stand_frame_right if self.last_direction == 'right' else self.stand_frame_left
        else:
            if self.direction == 'right':
                image = self.walk_right[self.frame] if self.speed != 0 else self.stand_frame_right
            else:
                image = self.walk_left[self.frame] if self.speed != 0 else self.stand_frame_left
        screen.blit(image, (self.x_pos, self.y_pos))