import pygame, math, random

pygame.init()
window = pygame.display.set_mode((1800, 1200))
pygame.display.set_caption("Fractal tree")
screen = pygame.display.get_surface()

def get_colors():
    red_color = random.randrange(64, 192)
    green_color = random.randrange(64, 192)
    blue_color =random.randrange(64, 192)
    return (red_color, green_color, blue_color)


def draw_tree(x1, y1, angle, depth):
    angle = random.randrange(angle - 10, angle + 10)
    fork_angle = 20
    base_len = 10.0
    colors = get_colors()
    if depth >= 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
        pygame.draw.line(screen, (colors), (x1, y1), (x2, y2), 2)
        draw_tree(x2, y2, angle - fork_angle, depth - 1)
        draw_tree(x2, y2, angle + fork_angle, depth - 1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

draw_tree(900, 1150, -90, 14)

pygame.display.flip()

while True:
    input(pygame.event.wait())
