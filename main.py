import pygame as pg


def main():
    pg.init()
    RES = (1200, 800)
    window = pg.display.set_mode(RES)
    pg.display.set_caption('Organ Simulation')
    
    clock = pg.time.Clock()
    
    runningMain = True
    while runningMain:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                runningMain = False
                
        
        pg.display.set_caption(f'Engine   -=Organ Simulation=-    -= Version 1 =-      -= FPS: {clock.get_fps():.1f} =- ')
        window.fill('black')
        pg.display.flip()
        clock.tick(60)
        


if __name__ == "__main__":
    main()
    


pg.quit()