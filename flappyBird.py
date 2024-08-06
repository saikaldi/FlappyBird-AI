import pygame
import neat
import time
import os
import random


WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "b1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "b2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "b3.png"))),
]
PIPE_IMG = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
]
BASE_IMG = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
]
BG_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))]


class Birds:
    IMGS = BIRD_IMGS
    MAX_ROATATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
