from walking_girl.config import cfg_item

class Character:
    def __init__(self, sprite_sheet):
        self.screen_width, self.screen_height = cfg_item("animation", "screen_size")[0],cfg_item("animation", "screen_size")[1]
        self.x_pos = 0
        self.y_pos = self.screen_height - sprite_sheet.frame_height
        self.speed = cfg_item("entities", "girl", "speed")
        self.frames_per_action = cfg_item("entities", "frames_per_action")
        self.frame = 0
        self.smooth = 0
        self.direction = 'right'
        self.sprite_sheet = sprite_sheet
        self.walk_right = [self.sprite_sheet.get_image(0, i) for i in range(1, self.frames_per_action + 1)]
        self.walk_left = [self.sprite_sheet.get_image(1, i) for i in range(1, self.frames_per_action + 1)]
        self.stand_frame_right = self.sprite_sheet.get_image(0, 0)
        self.stand_frame_left = self.sprite_sheet.get_image(1, 0)

    def update(self, delta_time):
        self.x_pos += self.speed * delta_time if self.direction == 'right' else -self.speed * delta_time
        if (self.smooth == cfg_item("entities", "girl", "smooth")):
            self.frame += 1
            self.smooth = 0
        else:
            self.smooth += 1
        if self.frame >= len(self.walk_right):
            self.frame = 0

        if self.x_pos <= 0 and self.direction == 'left':
            self.direction = 'right'
            self.x_pos = 0
        elif self.x_pos + self.sprite_sheet.frame_width >= self.screen_width and self.direction == 'right':
            self.direction = 'left'
            self.x_pos = self.screen_width - self.sprite_sheet.frame_width

    def draw(self, screen):
        if self.direction == 'right':
            image = self.walk_right[self.frame] if self.speed != 0 else self.stand_frame_right
        else:
            image = self.walk_left[self.frame] if self.speed != 0 else self.stand_frame_left
        screen.blit(image, (self.x_pos, self.y_pos))
