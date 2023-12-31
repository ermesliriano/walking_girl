import pygame
from importlib import resources

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sound(self, key, file_path):
        with resources.path(*file_path) as sound_filename:
            sound_l, sound_r = pygame.mixer.Sound(sound_filename), pygame.mixer.Sound(sound_filename)
            self.sounds[key] = {'left': sound_l, 'right': sound_r}


    def play_stereo(self, key, position, max_distance):
        left_sound = self.sounds[key]['left']
        right_sound = self.sounds[key]['right']

        left_volume = 1 - min(position / max_distance, 1)
        right_volume = min(position / max_distance, 1)

        left_sound.play().set_volume(left_volume, 0)  # Sonido izquierdo
        right_sound.play().set_volume(0, right_volume)  # Sonido derecho