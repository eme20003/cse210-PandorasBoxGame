import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from game.director import Director

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.BLACK, font_size = 40, anchor_x = "center")
        arcade.draw_text("Pandora’s box has been opened! It is up to you to fix what you broke in the first place ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size = 14, anchor_x = "center") 
        arcade.draw_text("and save the world that you put in jeopardy! Shoot your arrows at plagues, monsters, hunger, ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 130, arcade.color.BLACK, font_size = 13, anchor_x = "center")
        arcade.draw_text("emotional stresses like when Pluto was a planet, then a mass of rocks, then a planet, then a star,", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 110, arcade.color.BLACK, font_size = 13, anchor_x = "center") 
        arcade.draw_text("homework, and other life-threatening items as they hurtle at your face!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size = 15, anchor_x = "center")
        arcade.draw_text("Eliminate these from existence and return the world to its state of progress-less, blissful ignorance ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50, arcade.color.BLACK, font_size = 13, anchor_x = "center") 
        arcade.draw_text("where nothing good nor bad ever happens.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25, arcade.color.BLACK, font_size = 20, anchor_x = "center")
        arcade.draw_text("Click to begin saving the world from your dastardly deeds.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.GRAY, font_size = 20, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Call to setup method in PandorasBox class
        director_view = Director()
        director_view.setup()
        self.window.show_view(director_view)
    
      