import pygame as pg
from playsound import playsound
import math, keyboard, os





w, h = 1, 10
W, H = 20, 10
TILE_SIZE = 40
STUDIO_RES = W* TILE_SIZE, H* TILE_SIZE
grid = [pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) for x in range(4, W) for y in range(H)]
soundselection = [pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE * 4, TILE_SIZE) for x in range(w) for y in range(H)]
BEATS = []

DISPLAYSURF = pg.display.set_mode(STUDIO_RES)
pg.display.set_caption('Beatnerd')
clock = pg.time.Clock()
FPS = 60


colours = [[0,255,255],[0, 0, 255],[0, 255, 0],[255, 255, 0],[255, 0, 0], [128, 0, 128]]
pg.font.init() 
my_font = pg.font.SysFont('Comic Sans MS', 25)
soundscreen = False

soundclicked = []
localdir = [f for f in os.listdir('.') if os.path.isfile(f)]
del localdir[0]





def main(soundscreen):
    DISPLAYSURF.fill(pg.Color('black'))

    while True:
        if keyboard.is_pressed('esc'):
            pg.quit()
            exit()

        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                        
                    pos = pg.mouse.get_pos()
                    mouse_pos = (40 * math.floor(pos[0]/40), 40 * math.floor(pos[1]/40))
                        
                    if mouse_pos[1] <= 360 and mouse_pos[0] <= 80: 
                        soundscreen = True
        
                        pg.draw.rect(DISPLAYSURF, (0, 0, 0), pg.Rect(160, 0, 18 * TILE_SIZE,  10 * TILE_SIZE), 0)
                        
               
                        [DISPLAYSURF.blit(my_font.render(localdir[mp3], False, (255, 255, 255)), (160 ,mp3 * 40)) for mp3 in range(len(localdir))]
                        pg.display.flip()
                        
                        while soundscreen == True:
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        
                                        pos = pg.mouse.get_pos()
                                        mouse_pos = (40 * math.floor(pos[0]/40), 40 * math.floor(pos[1]/40))
                                        soundclicked.append(localdir[int(mouse_pos[1]/40)])
                                        print(soundclicked)
                                        DISPLAYSURF.fill((0,0, 0))
                                    
                                        [DISPLAYSURF.blit(my_font.render(soundclicked[mp3], False, (255, 255, 255)), (0 ,mp3 * 40)) for mp3 in range(len(soundclicked))]
                                        
                                        soundscreen = False
                                        

                    else:
                        if soundscreen == False:
                            BEATS.append(pg.Rect(mouse_pos[0]+3, mouse_pos[1]+3, TILE_SIZE-6, TILE_SIZE-6))
                            
                
        [pg.draw.rect(DISPLAYSURF, (40, 40, 40), i_rect, 1) for i_rect in grid]
        [pg.draw.rect(DISPLAYSURF, colours[0],  i_rect, 0) for i_rect in BEATS]
        [pg.draw.rect(DISPLAYSURF, (0, 255, 0), i_rect, 1) for i_rect in soundselection]
        
        
        pg.display.flip()
        clock.tick(FPS)
        




main(soundscreen)


fart = 'fart.mp3'

