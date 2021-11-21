import arcade
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCALE_BOX,
    SCALE_OBJECT,
    SCALE_PANDORA,
    SCALE_ARROW,
    ARROW_SPEED,
)


# Arrow Sprite
class Arrow(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""
        self.center_y += ARROW_SPEED


# Box Sprite
class Box(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Objects coming from Pandora's Box
class Objects(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Pandora Sprite
class Pandora(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """"""
        self.center_x += self.change_x
        self.center_y += self.change_y


# Main Window
class PandorasBox(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.box_list = None

        # Player info
        self.pandora = None
        self.score = 0

        # Box info
        self.box = None

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        """Setup the window. Allows you to refresh the screen
        instead of creating another instance."""

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()

        # add score
        self.score = 0

        # Player info
        self.pandora = Pandora("pandorasbox\game\pb_images\pandora3.jpg", SCALE_PANDORA)
        self.pandora.bottom = 0
        self.pandora.left = 0

        self.box = Box("pandorasbox\game\pb_images\ptreasure_chest.png", SCALE_BOX)
        self.box.top = 600
        self.box.center_x = SCREEN_WIDTH / 2

        # add pandora to the player list
        self.player_list.append(self.pandora)
        self.box_list.append(self.box)

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """THIS IS ALWAYS NEEDED. OVERRIDES default method in parent class"""

        # prepare screen to draw
        arcade.start_render()

        # Draw player lists
        self.player_list.draw()
        self.object_list.draw()
        self.arrow_list.draw()
        self.box_list.draw()

        # draw the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)

    def update(self, deltatime):
        """Movement and game logic. THIS IS AUTOMATICALLY CALLED.
        Refresh rate is 60 Hz"""

        # update all the sprites
        self.player_list.update()
        self.object_list.update()
        self.arrow_list.update()

        # Create a collision list
        for arrow in self.arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, self.object_list)
            for obj in hit_objects:
                self.score += int(10)
                obj.remove_from_sprite_lists()
                arrow.remove_from_sprite_lists()

            if self.arrow.bottom > SCREEN_HEIGHT:
                self.arrow.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """Method for moving Pandora left and right.
        Also fires arrows."""

        # Move using left or right arrow keys
        if key == arcade.key.RIGHT:
            self.pandora.change_x = 3
        if key == arcade.key.LEFT:
            self.pandora.change_x = -3

        # Fire arrows with spacebar.
        if key == arcade.key.SPACE:
            self.arrow = Arrow("pandorasbox\game\pb_images\Parrow_up1.png", SCALE_ARROW)
            self.arrow.center_x = self.pandora.center_x
            self.arrow.center_y = self.pandora.center_y + 50
            self.arrow_list.append(self.arrow)

    def on_key_release(self, key, modifiers):
        """Resets the movement to 0."""
        if key == arcade.key.RIGHT:
            self.pandora.change_x = 0
        if key == arcade.key.LEFT:
            self.pandora.change_x = 0


if __name__ == "__main__":
    window = PandorasBox(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Call to setup method in PandorasBox class
    window.setup()

    # Run arcade
    arcade.run()
