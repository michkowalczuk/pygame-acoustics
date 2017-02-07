""" Some useful functions"""
from pygame import Color


def create_range_of_colors(start_color, end_color, n):
    colors = [start_color]
    dr = end_color.r - start_color.r
    dg = end_color.g - start_color.g
    db = end_color.b - start_color.b
    for i in range(n):
        t = float(i + 1) / n
        r = int(start_color.r + t * dr)
        g = int(start_color.g + t * dg)
        b = int(start_color.b + t * db)
        colors.append(Color(r, g, b))
    return colors
