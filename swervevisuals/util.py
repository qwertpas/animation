import numpy as np
from manim import *

def rotate_pt(point, radians, origin):
    relative_loc = point - origin

    c, s = np.cos(radians), np.sin(radians)
    rot = np.matrix([
        [c, -s, 0], 
        [s, c, 0],
        [0, 0, 1]
    ])

    rotated = rot.dot(relative_loc) + origin
    return rotated


