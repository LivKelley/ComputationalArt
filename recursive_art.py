""" This script generates random art using different mathematical functions. """ #Header comment added.

#My extension is to make the program object oriented.

import random
from math import *
from PIL import Image

#Functions

class Art(): 

    def __init__ (self, filepath):
        self.filename = filepath
        self.x_size = 350
        self.y_size = 350


    def run(self,filepath): 

        self.generate_art(filepath) 


    def build_random_function(self, min_depth, max_depth):
        """ Builds a random function of depth at least min_depth and depth
            at most max_depth (see assignment writeup for definition of depth
            in this context)

            min_depth: the minimum depth of the random function
            max_depth: the maximum depth of the random function
            returns: the randomly generated function represented as a nested list
                     (see assignment writeup for details on the representation of
                    ,0 thes
                     e functions)

    You can't build proper doctests for a function that spits
    out randomized answers. If you insert (0,0) as input, you should always get 
    either ['x'] or ['y'] as an outcome, but otherwise the function will just be 
    nested functions within lists. """

        listf = ['x', 'y', 'cos_pi', 'sin_pi', 'prod', 'avg', 'sqrtx','x3']
        

        if max_depth == 0: 
            a = random.choice(listf[0:2])
        elif min_depth > 0: 
            a = random.choice(listf[2:])
        else: 
            a = random.choice(listf)

        if a in ['x', 'y']:
            return [a]
        elif a in ['prod','avg']:
            input1 = self.build_random_function(min_depth-1, max_depth-1)
            input2 = self.build_random_function(min_depth-1, max_depth-1)
            return [a, input1, input2] 
        else: 
            return [a, self.build_random_function(min_depth -1, max_depth -1)]

    def evaluate_random_function(self, f, x, y):
        """ Evaluate the random function f with inputs x,y
            Representation of the function f is defined in the assignment writeup

            f: the function to evaluate
            x: the value of x to be used to evaluate the function
            y: the value of y to be used to evaluate the function
            returns: the function value

            >>> art = Art(filepath = "myart.png")
            >>> art.evaluate_random_function(["x"],-0.5, 0.75)
            -0.5
            >>> art.evaluate_random_function(["y"],0.1,0.02)
            0.02
            >>> art.evaluate_random_function(["prod",["x"],["y"]], 1, 2)
            2.0
            >>> art.evaluate_random_function(["avg",["x"],["y"]], 1, 3) 
            2.0
            >>> art.evaluate_random_function(["sin_pi",["x"],["y"]], 3, 2) #This doctest fails, but the ending value is for all practical purposes the same as 0.
            0
            >>> art.evaluate_random_function(["cos_pi",["x"],["y"]], 3, 2)
            -1.0
            >>> art.evaluate_random_function(["sqrtx",["x"],["y"]], 3, 2) 
            1.0
            >>> art.evaluate_random_function(["x3",["x"],["y"]], 1, 2,) 
            1.0
        """

        #Like base case
        if f[0] == "x": 
            return x
        elif f[0] == "y":
            return y

        #Setting a to a thing.

        #Rewrote the main function sequence to be more concise and include inline functions.

        args = [self.evaluate_random_function(arg, x, y ) for arg in f[1:]]

        if f[0] == "prod":
            return float(args[0])*float(args[1])

        elif f[0] == 'avg':
            return float(.5*(args[0]+args[1]))

        elif f[0] == 'sin_pi':
            return sin(pi*float(args[0]))

        elif f[0] == 'cos_pi':
            return cos(pi*float(args[0]))

        elif f[0] == 'sqrtx':
            return float(args[0])**(1/2)

        elif f[0] == 'x3':
            return float(args[0])**3

        elif f[0] == "absx":        #Attempted to add some more complex functions to make things more interesting.
            return abs(float(args[0]))

        elif f[0] == "absy":
            return abs(float(args[1]))

        elif f[0] == "x5":
            return float(args[0])**5 

        elif f[0] == "y5":
            return float(args[1])**5

        elif f[0] == "x10":
            return float(args[0])**10

        elif f[0] == "y10":
            return float(args[1])**10


    def remap_interval(self,
                       val,
                       input_interval_start,
                       input_interval_end,
                       output_interval_start,
                       output_interval_end):
        """ Given an input value in the interval [input_interval_start,
            input_interval_end], return an output value scaled to fall within
            the output interval [output_interval_start, output_interval_end].

            val: the value to remap
            input_interval_start: the start of the interval that contains all
                                  possible values for val
            input_interval_end: the end of the interval that contains all possible
                                values for val
            output_interval_start: the start of the interval that contains all
                                   possible output values
            output_inteval_end: the end of the interval that contains all possible
                                output values
            returns: the value remapped from the input to the output interval

            >>> art = Art(filepath) 

            >>> art.remap_interval(0.5, 0, 1, 0, 10)
            5.0
            >>> art.remap_interval(5, 4, 6, 0, 2)
            1.0
            >>> art.remap_interval(5, 4, 6, 1, 2)
            1.5
        """

        #Reassigning variables as floats. 

        val = float(val)
        output_interval_end = float(output_interval_end)
        output_interval_start = float(output_interval_start)
        input_interval_start = float(input_interval_start)
        input_interval_end = float(input_interval_end)

        #Breaking down elements of the final equation.
            
        f = (output_interval_end-output_interval_start)*(val-input_interval_start)
        r = input_interval_end - input_interval_start
        t = output_interval_start

        #The final equation.

        e = f/r+t

        return e 

    #print(remap_interval(0.5, 0, 1, 0, 10))


    def color_map(self, val):
        """ Maps input value between -1 and 1 to an integer 0-255, suitable for
            use as an RGB color code.

            val: value to remap, must be a float in the interval [-1, 1]
            returns: integer in the interval [0,255]

            >>> art = Art(filepath = "myart.png") 

            >>> art.color_map(-1.0)
            0
            >>> art.color_map(1.0)
            255
            >>> art.color_map(0.0)
            127
            >>> art.color_map(0.5)
            191
            >>> art.color_map(.1)
            140
        """
        # NOTE: This relies on remap_interval, which you must provide
        color_code = self.remap_interval(val, -1, 1, 0, 255)
        return int(color_code)


    def test_image(self, filename, x_size, y_size):
        """ Generate test image with random pixels and save as an image file.

            filename: string filename for image (should be .png)
            x_size, y_size: optional args to set image dimensions (default: 350)
        """
        # Create image and loop over all pixels
        im = Image.new("RGB", (x_size, y_size))
        pixels = im.load()
        for i in range(x_size):
            for j in range(y_size):
                x = self.remap_interval(i, 0, x_size, -1, 1)
                y = self.remap_interval(j, 0, y_size, -1, 1)
                pixels[i, j] = (random.randint(0, 255),  # Red channel
                                random.randint(0, 255),  # Green channel
                                random.randint(0, 255))  # Blue channel

        im.save(filename)


    def generate_art(self, filename):
        """ Generate computational art and save as an image file.

            filename: string filename for image (should be .png)
            x_size, y_size: optional args to set image dimensions (default: 350)
        """
        # Functions for red, green, and blue channels - where the magic happens!
        red_function = self.build_random_function(2, 3)
        green_function = self.build_random_function(2, 3)
        blue_function = self.build_random_function(2, 3)

        # Create image and loop over all pixels
        im = Image.new("RGB", (self.x_size, self.y_size))
        pixels = im.load()
        for i in range(self.x_size):
            for j in range(self.y_size):
                x = self.remap_interval(i, 0, self.x_size, -1, 1)
                y = self.remap_interval(j, 0, self.y_size, -1, 1)
                pixels[i, j] = (
                        self.color_map(self.evaluate_random_function(red_function, x, y)),
                        self.color_map(self.evaluate_random_function(green_function, x, y)),
                        self.color_map(self.evaluate_random_function(blue_function, x, y)))

        im.save(filename)

if __name__ == '__main__':
    filepath = "myart.png"
    variable1 = Art(filepath) 
    variable1.run(filepath)
    import doctest
    doctest.testmod()

    # Create some computational art!
    #implement remap_interval and evaluate_random_function

    # Test that PIL is installed correctly
#test_image("noise.png")
