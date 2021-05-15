import requests
import pygame
import sys
import os

from pygame.locals import *
from moviepy.editor import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.join(BASE_DIR, 'images')
FPS = 60
SPEED = 5
NO_PLAYER = -1
DUCK = 1

tx_path = os.path.join(RES_DIR, 'txgamevideo.mp4')
music_path = os.path.join(RES_DIR, 'shadiao.mp3')

wight, height = (800, 600)

def download_game():
    player0 = requests.get()

class MainWindow(object):
    def __init__(self, player_name=NO_PLAYER):
        self.player_name = player_name
        self.on_jump = False
        self.on_base = False
        self.on_trap = False
        self.on_conveyor_belt = False
        self.side = 'left'
        self.move = False
        self.kill = False
        self.y = 180
        self.x = 0
        self.player_n = 0
        pygame.display.set_caption('是男人就要下一百层')
        self.images = {'up': pygame.image.load(os.path.join(RES_DIR, 'up.png')),
                       'player0': pygame.image.load(os.path.join(RES_DIR, 'players/0.png')),
                       'player1': pygame.image.load(os.path.join(RES_DIR, 'players/1.png')),
                       'player2': pygame.image.load(os.path.join(RES_DIR, 'players/2.png')),
                       'player3': pygame.image.load(os.path.join(RES_DIR, 'players/3.png')),
                       }
        self.clock = pygame.time.Clock()

    def run(self):
        self.tx_game()
        self.pick_player()
        self.init_music()
        while True:
            self.blit_bg()
            self.blit_up()
            self.blit_player()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        self.side = 'left'
                        self.move = True
                    elif event.key == K_d:
                        self.side = 'right'
                        self.move = True

                elif event.type == KEYUP:
                    self.move = False
            if self.move:
                self.player_n += 1
                if self.side == 'left':
                    self.x -= SPEED
                if self.side == 'right':
                    self.x += SPEED
            
            if self.x > wight or self.y < 0 or self.y > height:
                self.kill = True

            if self.kill:
                self.blit_player()
            
            if not (self.on_conveyor_belt or self.on_trap or self.on_base):
                
                self.y += SPEED

            pygame.display.update()
            self.clock.tick(FPS)
    
    def tx_game(self):
        clip = VideoFileClip(tx_path)
        clip.preview()
        self.DISPLAYSURF = pygame.display.set_mode((wight, height))

    def blit_bg(self):
        self.DISPLAYSURF.fill((0, 0, 0))

    def blit_player(self):
        if self.side == 'left':
            self.DISPLAYSURF.blit(self.get_player(), (self.x, self.y))
        elif self.side == 'right':
            self.DISPLAYSURF.blit(pygame.transform.flip(
                self.get_player(), True, False), (self.x, self.y))
        elif self.side == 'down':
            pass

    def get_player(self):
        return self.images['player' + str(self.player_n % 4)]

    def blit_up(self):
        self.DISPLAYSURF.blit(self.images['up'], (0, 0))

    def init_music(self):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()

    def pick_player(self):
        pass

def main():
    pygame.init()
    widget = MainWindow()
    widget.run()


if __name__ == "__main__":
    main()
