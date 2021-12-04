import arcade
from game.constants import SCREEN_WIDTH

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """Draw "Game over" across the screen."""
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
            SCREEN_WIDTH / 2,
            200,
            arcade.color.GRAY,
            font_size = 15,
            anchor_x = "center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     game_view = Director()
    #     self.window.show_view(game_view)