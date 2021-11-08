"""
This module is used to generate 
random hex code of colors

color_generate() --> func
It will return random color
"""

import numpy as np

def color_generate():
    """This function will generate and return random color"""
    val = list("abcdef0123456789") 
    color = "".join(np.random.choice(val, 6))
    return "#" + color
