from os import remove
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandelCollisions(Action):

    def execute(self, cast):
        balls = cast['ball'][0]
        arrow = cast['arrow'][0]
        pandora = cast['pandora'][0]

        for ball in balls:
            # right wall
            if ball.get_position().equals(constants.MAX_X - 1):
                ball.set_velocity(ball._velocity.bounce_X())

            # left wall
            if ball.get_position().get_x() == 1:
                ball.set_velocity(ball._velocity.bounce_X())
            
            # floor
            if ball.get_position().get_y() == constants.MAX_Y - 1:
                 ball.set_velocity(ball._velocity.bounce_Y())

            # cealing
            if ball.get_position().get_y() == 40:
                 ball.set_velocity(ball._velocity.bounce_Y())
            
            # pandora
            if ball.get_position().equals(pandora.get_position()):
                sys.exit()

            #arrow - bal
            if ball.get_position().equals(arrow.get_position()):
                ball.remove(ball)
                arrow.remove(arrow)
                #get point
            
            #arrow - cealing
            if arrow.get_position().get_y() == 1:
                arrow.remove(arrow)
            #arcade.checkforcolision