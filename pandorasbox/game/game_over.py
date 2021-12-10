import arcade
from game.constants import SCREEN_WIDTH

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.window.set_mouse_visible(True)
        self.score = 0
        self.background = None

    def on_show(self):
        '''Display the backround as one of the images stored in pb_images
        
        Args:
            self(InstructionView): an instance of InstructionView'''
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("pandorasbox\game\pb_images\phoenix_fire.png")

    def on_draw(self):
        """Draw "Game over" across the screen."""
        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, 400, arcade.color.WHITE, 54, anchor_x = "center", font_name = "garamond")
        
        arcade.draw_text("Clearly you missed shooting down the common cold, cancer, ", SCREEN_WIDTH / 2, 340, arcade.color.WHITE, 14,  anchor_x = "center", font_name = "candara")
        arcade.draw_text("and the monsters under your bed and in your closet. . . . ", SCREEN_WIDTH / 2, 320, arcade.color.WHITE, 14,  anchor_x = "center", font_name = "candara")
        arcade.draw_text("But perhaps you did some good, and restored some semblance of ", SCREEN_WIDTH / 2, 300, arcade.color.WHITE, 14, anchor_x = "center", font_name = "candara")
        arcade.draw_text("HOPE to an otherwise doomed world.", SCREEN_WIDTH / 2, 272, arcade.color.WHITE, 19,  anchor_x = "center", font_name = "candara")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken to fix what took you only a second to destroy: ",
            SCREEN_WIDTH / 2,
            200,
            arcade.color.GRAY,
            font_size = 15,
            anchor_x = "center",
            font_name = "candara")
        arcade.draw_text(time_taken_formatted,
            SCREEN_WIDTH / 2,
            170,
            arcade.color.WHITE_SMOKE,
            font_size = 22,
            anchor_x = "center",
            font_name = "candara")

        output_total = f"Total Score: {self.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14, font_name = "candara")

        # def hope_rise(self):
        #     if output_total >= 320:
