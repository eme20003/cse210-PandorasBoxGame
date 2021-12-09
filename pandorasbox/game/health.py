import arcade
from game.constants import SCREEN_WIDTH
WIDTH = 30
HEIGHT = 20
MARGIN_LEFT = 5

class Health:
    def __init__(self) -> None:
        self.health = 3
        self.center_text = self.health * (WIDTH+MARGIN_LEFT)  

        self.color = arcade.color.RED


    def set(self, health_unit: int) -> None:
        self.health = health_unit

    def get(self) -> int:
        return self.health

    def add(self) -> None:
        self.health += 1

    def subtract(self) -> None:
        self.health -= 1

    def has_health(self) -> bool:
        if self.get() > 1:
            return True
        else:
            return False
    
    def draw_bar(self):
        center_x = self.health * (WIDTH+MARGIN_LEFT)
        center_y = 30
        margin_top = 3
        text_width = 88
        text_offset = self.center_text + text_width
        font_size = 16
        arcade.draw_text('Health:', SCREEN_WIDTH-text_offset, HEIGHT, self.color, font_size)

        for _ in range(self.health):
            arcade.draw_rectangle_filled(SCREEN_WIDTH-center_x, center_y-margin_top, WIDTH, HEIGHT, self.color)
            center_x -= WIDTH + MARGIN_LEFT
