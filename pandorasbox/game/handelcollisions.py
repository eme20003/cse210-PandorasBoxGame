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
                #bounce
                pass

            # left wall
            if ball.get_position().equals(1):
                #bounce
                pass
            
            # floor
            if ball.get_position().equals(constants.MAX_Y - 1):
                #bounce
                pass

            # cealing
            if ball.get_position().equals(50):
                #bounce
                pass
            
            # pandora
            if ball.get_position().equals(pandora.get_position()):
                #end game
                pass

            #arrow
            if ball.get_position().equals(arrow.get_position()):
                #kill ball
                #kill arrow
                pass


    #ball hit pandora
    #arrow hit ball
    #ball hit walls and floor