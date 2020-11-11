import sys

import pygame
import time
import math

pygame.init()
screen_width = 600
screen_height = 700
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font_logic = pygame.font.SysFont("cambriacambriamath",50, False, False)
font_text = pygame.font.SysFont("sans", 50, False, False)

text_1 = font_logic.render("+", True, BLACK)
text_2 = font_logic.render("+", True, BLACK)
text_3 = font_logic.render("-", True, BLACK)
text_4 = font_logic.render("-", True, BLACK)
text_5 = font_text.render("START", True, BLACK)
text_6 = font_text.render("RESET", True, BLACK)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock.exe")
sound = pygame.mixer.music.load("music.mp3")

def run_clock():

    start = False
    total = 0
    total_sec = 0

    while True:
        screen.fill(GREY)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw()
        blit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # When click the left mouse each button
                if event.button == 1:
                    # Click on "+" minutes button
                    if (50 < mouse_x < 100) and (50 < mouse_y < 100):
                        total_sec += 60
                        total = total_sec
                    # Click on "+" seconds button
                    if (200 < mouse_x < 250) and (50 < mouse_y < 100):
                        total_sec += 1
                        total = total_sec
                    # Click on "-" minutes button
                    if (50 < mouse_x < 100) and (250 < mouse_y < 300):
                        total_sec -= 60
                        total = total_sec
                    # Click on "-" seconds button
                    if (200 < mouse_x < 250) and (250 < mouse_y < 300):
                        total_sec -= 1
                        total = total_sec
                    # Click on Start button
                    if (350 < mouse_x < 550) and (100 < mouse_y < 150):
                        start = True
                        total = total_sec
                    # Click on Reset button
                    if (350 < mouse_x < 550) and (200 < mouse_y < 250):
                        total_sec = 0
                        start = False
                    if (0 < mouse_x < screen_width) and (0 < mouse_y < screen_height):
                        pygame.mixer.music.stop()
        # Start the count down
        if start:
            total_sec -= 1
            if total_sec == 0:
                print("het gio")
                pygame.mixer.music.play(-1)
            time.sleep(1)
        if total_sec < 0:
            start = False
            total_sec = 0
            total = 0

        # If seconds larger than 60 then add minutes
        secs = total_sec % 60
        mins = (total_sec - secs) / 60
        mins = int(mins)


        time_now = str(mins) + "  :  " + str(secs)
        text_time = font_text.render(time_now, True, BLACK)
        screen.blit(text_time, (120,120))


        x_sec = 300 + 100 * math.sin(6 * secs * math.pi /180)
        y_sec = 450 - 100 * math.cos(6 * secs * math.pi /180)
        pygame.draw.line(screen, BLACK, (300,450), (int(x_sec), int(y_sec)), 2)

        x_min = 300 + 60 * math.sin(6 * mins * math.pi / 180)
        y_min = 450 - 60 * math.cos(6 * mins * math.pi / 180)
        pygame.draw.line(screen, RED, (300, 450), (int(x_min), int(y_min)),3)

        if total != 0:
            pygame.draw.rect(screen, RED, (50, 600, int(380*(total_sec/total)) + 120, 50))

        pygame.display.flip()

def draw():
    pygame.draw.rect(screen, WHITE, (50, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (50, 250, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 250, 50, 50))

    pygame.draw.rect(screen, WHITE, (350, 100, 200, 50))
    pygame.draw.rect(screen, WHITE, (350, 200, 200, 50))

    pygame.draw.circle(screen, WHITE, (300, 450), 100)

def blit():
    screen.blit(text_1, (60, 45))
    screen.blit(text_2, (210, 45))
    screen.blit(text_3, (65, 245))
    screen.blit(text_4, (215, 245))
    screen.blit(text_5, (360, 100))
    screen.blit(text_6, (360, 200))


run_clock()
pygame.quit()
