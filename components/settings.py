import pygame
pygame.init()
pygame.font.init()

white_colour = (255, 255, 255)
black_colour = (0, 0, 0)
red_color = (255, 0, 0)
blue_colour = (0, 255, 0)
green_colour = (0, 0, 255)
yellow_colour = (255, 255, 0)
pink_colour = (255, 192, 203)
brown_colour = (150, 75, 0)

fps = 60
width, height = 700, 800

rows = colums = 50
toolbar_h = height - width
pixel_sizes = width // colums
bg_colour = white_colour
draw_lines = True

def get_font(size): 
    return pygame.font.SysFont("comicsans", size)