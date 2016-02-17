""" TODO: Put your header comment here """

import random
from math import *
from PIL import Image

#Functions 

def prod(a,b):
    return a*b 

def avg(a,b):
    return .5*(a+b)

def cos_pi(a):
    return cos(pi*a)

def sin_pi(a):
    return sin(pi*a)

def x(a,b):
    return a 

def y(a,b):
    return b

def sqrtx(a): 
    return a**(1/2)

def x3(a):
    return a**3 




def build_random_function(min_depth, max_depth):
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
    
    # TODO: implement this

    listf = ['x', 'y', 'cos_pi', 'sin_pi', 'prod', 'avg', 'sqrtx','x3']
    

    if max_depth == 0: 
        a = random.choice(listf[0:2])
    elif min_depth > 0: 
        a = random.choice(listf[2:])
    else: 
        a = random.choice(listf)

    if a == 'x' or a == 'y': 
        return [a]
    elif a == 'prod' or a == 'avg':
        input1 = build_random_function(min_depth-1, max_depth-1)
        input2 = build_random_function(min_depth-1, max_depth-1)
        return [a, input1, input2] 
    else: 
        return [a, build_random_function(min_depth -1, max_depth -1)]

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        # >>> evaluate_random_function(["x"],-0.5, 0.75)
        # -0.5
        # >>> evaluate_random_function(["y"],0.1,0.02)
        # 0.02
        # >>> evaluate_random_function(["prod"], 1, 2)
        # 2 
        # >>> evaluate_random_function(["avg"], 1, 2)
        # 1
        # >>> evaluate_random_function(["sin_pi"], 3, 2)
        # 0
        # >>> evaluate_random_function(["cos_pi"], 3, 2)
        # -.4
        # >>> evaluate_random_function(["sqrtx", 3, 2]) 
        # 1.73
        # >>>evaluate_random_function(["x3", 1, 2,]) 
        # 1
        These don't work because of how I've inputed f[1] and f[2]
    """
    # TODO: implement this

    #Like base case.
    if f[0] == "x": 
        return x 
    elif f[0] == "y":
        return y

    #Setting a to a thing.

    elif f[0] == 'prod':
         a = evaluate_random_function(f[1], x, y) 
         b = evaluate_random_function(f[2], x, y)
         return prod(a,b)

    elif f[0] == 'avg':
        a = evaluate_random_function(f[1], x, y) 
        b = evaluate_random_function(f[2], x, y)
        return avg(a,b)

    elif f[0] == 'sin_pi':
        a = evaluate_random_function(f[1], x, y) 
        return sin_pi(a)

    elif f[0] == 'cos_pi':
        a = evaluate_random_function(f[1], x, y)
        return cos_pi(a)

    elif f[0] == 'sqrtx':
        a = evaluate_random_function(f[1], x, y)
        return sqrtx(a)

    elif f[0] == 'x3':
        a = evaluate_random_function(f[1], x, y) 
        return x3(a)


def remap_interval(val,
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

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this

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


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
        >>> color_map(.1)
        140
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)



def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(2, 3)
    green_function = build_random_function(2, 3)
    blue_function = build_random_function(2, 3)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y)))

    im.save(filename)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #implement remap_interval and evaluate_random_function
generate_art("example2.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
#test_image("noise.png")
