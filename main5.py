#!/usr/bin/env python3

import utils, open_color, arcade                                                         # imports some libraries

utils.check_version((3,7))                                                               # checks the python version

SCREEN_WIDTH = 800                                                                       # assigns SCREEN_WIDTH a value of 800
SCREEN_HEIGHT = 600                                                                      # assigns SCREEN_HEIGHT a value of 600
SCREEN_TITLE = "Smiley Face Example"                                                     # assigns SCREEN_TITLE a value of "Smiley Face Example"

class Faces(arcade.Window):                                                              # creates the custom window class
    """ Our custom Window Class"""

    def __init__(self):                                                                  # this is the initializer
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)                      # calls the class initializer

        # Show the mouse cursor
        self.set_mouse_visible(True)                                                     # shows the mouse cursor

        self.x = SCREEN_WIDTH / 2                                                        # assigns self.x the value of 1/2 of the SCREEN_WIDTH variable
        self.y = SCREEN_HEIGHT / 2                                                       # assigns self.y the value of 1/2 of the SCREEN_HEIGHT variable

        arcade.set_background_color(open_color.white)                                    # sets the background color of the image to white

    def on_draw(self):                                                                   # draws the face
        """ Draw the face """
        arcade.start_render()                                                            # starts the arcade renderer
        face_x,face_y = (self.x,self.y)                                                  # assigns face_x and face_y the values of self.x and self.y respectfully
        smile_x,smile_y = (face_x + 0,face_y - 10)                                       # assigns smile_x and smile_y the values of face_x + 0 and face_y -10 respectfully
        eye1_x,eye1_y = (face_x - 30,face_y + 20)                                        # assigns eye1_x and eye1_y the values of face_x - 30 and face_y + 20 respectfully
        eye2_x,eye2_y = (face_x + 30,face_y + 20)                                        # assigns eye2_x and eye2_y the values of face_x  + 30 and face_y + 20 respectfully
        catch1_x,catch1_y = (face_x - 25,face_y + 25)                                    # assigns catch1_x and catch1_y the values of face_x -25 and face_y +25 respectfully
        catch2_x,catch2_y = (face_x + 35,face_y + 25)                                    # assigns catch2_x and catch2_y the values of face_x +35 and face_y +25 respectfully

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)              # this draws the filled circle at the location specified (which is where the mouse is)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)              # this draws the circle outline at the location specified (which is where the mouse is)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)                 # draws the left eye at the location specified (which is where the mouse is + offset)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)                 # draws the right eye at the location specified (which is where the mouse is + offset)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)                 # draws the left "catch" at the location specified (which is where the mouse is + offset)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)                 # draws the right "catch" at the location specified (which is where the mouse is + offset)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)        # draws the smile at the location specified (which is where the mouse is + offset)


    def on_mouse_motion(self, x, y, dx, dy):                                             # the handler for the mouse motion
        """ Handle Mouse Motion """
        self.x = x                                                                       # updates self.x to be equal to x
        self.y = y                                                                       # updates self.y to be equal to y



window = Faces()                                                                         # creates our custom Faces window
arcade.run()                                                                             # runs the arcade system