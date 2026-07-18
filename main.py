#2026 Cy

# im going to start commenting on this project too because it worked well on the game engine


import pygame as pg
import math as M
import wave
import struct
import random as R
import numpy as np
from CybrocksLibrary import Button
import time
import tkinter as tk
from tkinter import filedialog
import json

def main():
    # ----== Inits ==----------------------------------------------------------------------------------------------------------------------------------------------
    pg.init()
    pg.font.init()
    pg.mixer.init()
    
    '''pg.mixer.music.load("resources/Fallen Angel (An Adaptation of Bach_ BWV 639) - Arsi _Hakita_ Patala.mid")
    pg.mixer.music.play()
    '''

    font = pg.font.SysFont('Arial', 25)

    RES = (1700, 900) # had to slightly extend the bottom to make space for all the buttons
    window = pg.display.set_mode(RES)
    pg.display.set_caption('Organ Simulation')

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    
    clock = pg.time.Clock()
    



    
    

    # ----== Buttons ==----------------------------------------------------------------------------------------------------------------------------------------------

    saveB = Button("resources/textures/saveB.png", (1250, 50), 3, 3) #there is a lot of repitition in this entire script
    testB = Button("resources/textures/testB.png", (1250, 125), 3, 3)
    fadeB = Button("resources/textures/fadeon.png", (1425, 50), 3, 3)
    attackb = Button("resources/textures/attackon.png", (1425, 125), 3, 3)
    noiseb = Button("resources/textures/noiseon.png", (1505, 50), 3, 3)
    lengthb = Button("resources/textures/speed2.png", (1505, 125), 3, 3)
    clearB = Button("resources/textures/clear.png", (1580, 50), 3, 3)
    scrollB = Button("resources/textures/scroll.png", (30, 230), 3, 3)
    reverbB = Button("resources/textures/reverbon.png", (1580, 125), 3, 3)


    l1bUP = Button("resources/textures/up.png", (75+175, 250), 3, 3)
    l1bDN = Button("resources/textures/down.png", (75+175, 350), 3, 3)
    
    l2bUP = Button("resources/textures/up.png", (150+175, 250), 3, 3)
    l2bDN = Button("resources/textures/down.png", (150+175, 350), 3, 3)
    
    l3bUP = Button("resources/textures/up.png", (225+175, 250), 3, 3)
    l3bDN = Button("resources/textures/down.png", (225+175, 350), 3, 3)
    
    l4bUP = Button("resources/textures/up.png", (300+175, 250), 3, 3)
    l4bDN = Button("resources/textures/down.png", (300+175, 350), 3, 3)
    
    l5bUP = Button("resources/textures/up.png", (375+175, 250), 3, 3)
    l5bDN = Button("resources/textures/down.png", (375+175, 350), 3, 3)
    
    l6bUP = Button("resources/textures/up.png", (450+175, 250), 3, 3)
    l6bDN = Button("resources/textures/down.png", (450+175, 350), 3, 3)
    
    l7bUP = Button("resources/textures/up.png", (525+175, 250), 3, 3)
    l7bDN = Button("resources/textures/down.png", (525+175, 350), 3, 3)
    
    l8bUP = Button("resources/textures/up.png", (600+175, 250), 3, 3)
    l8bDN = Button("resources/textures/down.png", (600+175, 350), 3, 3)
    
    l9bUP = Button("resources/textures/up.png", (675+175, 250), 3, 3)
    l9bDN = Button("resources/textures/down.png", (675+175, 350), 3, 3)
    
    l10bUP = Button("resources/textures/up.png", (750+175, 250), 3, 3)
    l10bDN = Button("resources/textures/down.png", (750+175, 350), 3, 3)
    
    l11bUP = Button("resources/textures/up.png", (825+175, 250), 3, 3)
    l11bDN = Button("resources/textures/down.png", (825+175, 350), 3, 3)
    
    l12bUP = Button("resources/textures/up.png", (900+175, 250), 3, 3)
    l12bDN = Button("resources/textures/down.png", (900+175, 350), 3, 3)
    
    l13bUP = Button("resources/textures/up.png", (975+175, 250), 3, 3)
    l13bDN = Button("resources/textures/down.png", (975+175, 350), 3, 3)
    
    l14bUP = Button("resources/textures/up.png", (1050+175, 250), 3, 3)
    l14bDN = Button("resources/textures/down.png", (1050+175, 350), 3, 3)
    
    l15bUP = Button("resources/textures/up.png", (1125+175, 250), 3, 3)
    l15bDN = Button("resources/textures/down.png", (1125+175, 350), 3, 3)
    
    l16bUP = Button("resources/textures/up.png", (1200+175, 250), 3, 3)
    l16bDN = Button("resources/textures/down.png", (1200+175, 350), 3, 3)
    


    da1bUP = Button("resources/textures/up.png", (75+175, 450), 3, 3)
    da1bDN = Button("resources/textures/down.png", (75+175, 550), 3, 3)
    
    da2bUP = Button("resources/textures/up.png", (150+175, 450), 3, 3)
    da2bDN = Button("resources/textures/down.png", (150+175, 550), 3, 3)
    
    da3bUP = Button("resources/textures/up.png", (225+175, 450), 3, 3)
    da3bDN = Button("resources/textures/down.png", (225+175, 550), 3, 3)
    
    da4bUP = Button("resources/textures/up.png", (300+175, 450), 3, 3)
    da4bDN = Button("resources/textures/down.png", (300+175, 550), 3, 3)
    
    da5bUP = Button("resources/textures/up.png", (375+175, 450), 3, 3)
    da5bDN = Button("resources/textures/down.png", (375+175, 550), 3, 3)
    
    da6bUP = Button("resources/textures/up.png", (450+175, 450), 3, 3)
    da6bDN = Button("resources/textures/down.png", (450+175, 550), 3, 3)
    
    da7bUP = Button("resources/textures/up.png", (525+175, 450), 3, 3)
    da7bDN = Button("resources/textures/down.png", (525+175, 550), 3, 3)
    
    da8bUP = Button("resources/textures/up.png", (600+175, 450), 3, 3)
    da8bDN = Button("resources/textures/down.png", (600+175, 550), 3, 3)
    
    da9bUP = Button("resources/textures/up.png", (675+175, 450), 3, 3)
    da9bDN = Button("resources/textures/down.png", (675+175, 550), 3, 3)
    
    da10bUP = Button("resources/textures/up.png", (750+175, 450), 3, 3)
    da10bDN = Button("resources/textures/down.png", (750+175, 550), 3, 3)
    
    da11bUP = Button("resources/textures/up.png", (825+175, 450), 3, 3)
    da11bDN = Button("resources/textures/down.png", (825+175, 550), 3, 3)
    
    da12bUP = Button("resources/textures/up.png", (900+175, 450), 3, 3)
    da12bDN = Button("resources/textures/down.png", (900+175, 550), 3, 3)
    
    da13bUP = Button("resources/textures/up.png", (975+175, 450), 3, 3)
    da13bDN = Button("resources/textures/down.png", (975+175, 550), 3, 3)
    
    da14bUP = Button("resources/textures/up.png", (1050+175, 450), 3, 3)
    da14bDN = Button("resources/textures/down.png", (1050+175, 550), 3, 3)
    
    da15bUP = Button("resources/textures/up.png", (1125+175, 450), 3, 3)
    da15bDN = Button("resources/textures/down.png", (1125+175, 550), 3, 3)
    
    da16bUP = Button("resources/textures/up.png", (1200+175, 450), 3, 3)
    da16bDN = Button("resources/textures/down.png", (1200+175, 550), 3, 3)
    


    db1bUP = Button("resources/textures/up.png", (75+175, 650), 3, 3)
    db1bDN = Button("resources/textures/down.png", (75+175, 750), 3, 3)
    
    db2bUP = Button("resources/textures/up.png", (150+175, 650), 3, 3)
    db2bDN = Button("resources/textures/down.png", (150+175, 750), 3, 3)
    
    db3bUP = Button("resources/textures/up.png", (225+175, 650), 3, 3)
    db3bDN = Button("resources/textures/down.png", (225+175, 750), 3, 3)
    
    db4bUP = Button("resources/textures/up.png", (300+175, 650), 3, 3)
    db4bDN = Button("resources/textures/down.png", (300+175, 750), 3, 3)
    
    db5bUP = Button("resources/textures/up.png", (375+175, 650), 3, 3)
    db5bDN = Button("resources/textures/down.png", (375+175, 750), 3, 3)
    
    db6bUP = Button("resources/textures/up.png", (450+175, 650), 3, 3)
    db6bDN = Button("resources/textures/down.png", (450+175, 750), 3, 3)
    
    db7bUP = Button("resources/textures/up.png", (525+175, 650), 3, 3)
    db7bDN = Button("resources/textures/down.png", (525+175, 750), 3, 3)
    
    db8bUP = Button("resources/textures/up.png", (600+175, 650), 3, 3)
    db8bDN = Button("resources/textures/down.png", (600+175, 750), 3, 3)
    
    db9bUP = Button("resources/textures/up.png", (675+175, 650), 3, 3)
    db9bDN = Button("resources/textures/down.png", (675+175, 750), 3, 3)
    
    db10bUP = Button("resources/textures/up.png", (750+175, 650), 3, 3)
    db10bDN = Button("resources/textures/down.png", (750+175, 750), 3, 3)
    
    db11bUP = Button("resources/textures/up.png", (825+175, 650), 3, 3)
    db11bDN = Button("resources/textures/down.png", (825+175, 750), 3, 3)
    
    db12bUP = Button("resources/textures/up.png", (900+175, 650), 3, 3)
    db12bDN = Button("resources/textures/down.png", (900+175, 750), 3, 3)
    
    db13bUP = Button("resources/textures/up.png", (975+175, 650), 3, 3)
    db13bDN = Button("resources/textures/down.png", (975+175, 750), 3, 3)
    
    db14bUP = Button("resources/textures/up.png", (1050+175, 650), 3, 3)
    db14bDN = Button("resources/textures/down.png", (1050+175, 750), 3, 3)
    
    db15bUP = Button("resources/textures/up.png", (1125+175, 650), 3, 3)
    db15bDN = Button("resources/textures/down.png", (1125+175, 750), 3, 3)
    
    db16bUP = Button("resources/textures/up.png", (1200+175, 650), 3, 3)
    db16bDN = Button("resources/textures/down.png", (1200+175, 750), 3, 3)
    
    # ----== Organ Var Inits ==----------------------------------------------------------------------------------------------------------------------------------------------
    sample_rate = 44100
    frequency = 261.61   #C4
    duration = 2.0 
    amplitude = 32767
    attack = 1
    attack_time = 0.5
    attacklen = 0.00002
    attackenabled = True
    attack_samples = int(sample_rate * attack_time)
    release = 0.25
    fadeenabled = True
    reverbenabled = False
    noise = True
    
    tuned = False
    
    

    #organ wave vars
    length1  = 1.00    
    dista1  = 1    
    distb1 = 1
    
    length2  = 0.65    
    dista2  = 2    
    distb2 = 1
    
    length3  = 0.45    
    dista3  = 3    
    distb3 = 1
    
    length4  = 0.30    
    dista4  = 4    
    distb4 = 1
    
    length5  = 0.35    
    dista5  = 5    
    distb5 = 1
    
    length6  = 0.18    
    dista6  = 6    
    distb6 = 1
    
    length7  = 0.25    
    dista7  = 7    
    distb7 = 1
    
    length8  = 0.12    
    dista8  = 8    
    distb8 = 1

    length9  = 0.35    
    dista9  = 1    
    distb9 = 1.0
    
    length10 = 0.20    
    dista10 = 2    
    distb10 = 1.0
    
    length11 = 0.18    
    dista11 = 3    
    distb11 = 1.0

    length12 = 0.10    
    dista12 = 4    
    distb12 = 1.0
    
    length13 = 0.12    
    dista13 = 5    
    distb13 = 1.0
    
    length14 = 0.08    
    dista14 = 6    
    distb14 = 1.0
    
    length15 = 0.06    
    dista15 = 7    
    distb15 = 1
    
    length16 = 0.04    
    dista16 = 8    
    distb16 = 1

    #saveAudio(44100,0,2,32767,1,0.001,False,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    
    #other vars
    testing = True
    scroll = False
    scrollen = 0
    

    # ----== Audio ==----------------------------------------------------------------------------------------------------------------------------------------------
    
    click = pg.mixer.Sound('resources\sounds\click.wav')
    sclick = pg.mixer.Sound('resources\sounds\smoothclick.wav')



    # ----== Loop ==----------------------------------------------------------------------------------------------------------------------------------------------
    runningMain = True
    while runningMain:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                runningMain = False
            #if event.type == pg.KEYDOWN and event.key == pg.K_a:
            #    testS.play()
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) == "f1": #save
                print('written')
                with open("soundbank/yourSave.json", "w") as f:
                    json.dump({"length1": length1,"dista1": dista1, "distb1": distb1,"length2": length2, "dista2": dista2, "distb2": distb2,"length3": length3, "dista3": dista3, "distb3": distb3,"length4": length4, "dista4": dista4, "distb4": distb4,"length5": length5, "dista5": dista5, "distb5": distb5,"length6": length6, "dista6": dista6, "distb6": distb6,"length7": length7, "dista7": dista7, "distb7": distb7,"length8": length8, "dista8": dista8, "distb8": distb8,"length9": length9, "dista9": dista9, "distb9": distb9,"length10": length10,"dista10": dista10, "distb10": distb10,"length11": length11,"dista11": dista11, "distb11": distb11,"length12": length12,"dista12": dista12, "distb12": distb12,"length13": length13,"dista13": dista13, "distb13": distb13,"length14": length14,"dista14": dista14, "distb14": distb14,"length15": length15,"dista15": dista15, "distb15": distb15,"length16": length16,"dista16": dista16, "distb16": distb16}, f)
            if pg.key.name(event.key) == "f2": #load
                loaded = load()
                length1  = loaded['length1']
                dista1  = loaded['dista1']   
                distb1 = loaded['distb1']  
                
                length2  = loaded['length2'] 
                dista2  = loaded['dista2']   
                distb2 = loaded['distb2']  
                
                length3  = loaded['length3']   
                dista3  = loaded['dista3']   
                distb3 = loaded['distb3']  
                
                length4  = loaded['length4']  
                dista4  = loaded['dista4']   
                distb4 = loaded['distb4']  
                
                length5  = loaded['length5']  
                dista5  = loaded['dista5']   
                distb5 = loaded['distb5']  
                
                length6  = loaded['length6']  
                dista6  = loaded['dista6']   
                distb6 = loaded['distb6']  
                
                length7  = loaded['length7']
                dista7  = loaded['dista7']   
                distb7 = loaded['distb7']  
                
                length8  = loaded['length8'] 
                dista8  = loaded['dista8']   
                distb8 = loaded['distb8']  

                length9  = loaded['length9']
                dista9  = loaded['dista9']   
                distb9 = loaded['distb9']  
                
                length10 = loaded['length10']
                dista10 = loaded['dista10']   
                distb10 = loaded['distb10']  
                
                length11 = loaded['length11']
                dista11 = loaded['dista11']   
                distb11 = loaded['distb11']  

                length12 = loaded['length12']
                dista12 = loaded['dista12']   
                distb12 = loaded['distb12']  
                
                length13 = loaded['length13']
                dista13 = loaded['dista13']   
                distb13 = loaded['distb13']  
                
                length14 = loaded['length14']
                dista14 = loaded['dista14']   
                distb14 = loaded['distb14']  
                
                length15 = loaded['length15']
                dista15 = loaded['dista15']    
                distb15 = loaded['distb15']  
                
                length16 = loaded['length16']
                dista16 = loaded['dista16']   
                distb16 = loaded['distb16']  

                
        



        #now here is the start of a very long line of nearly idendical button scripts


        #lb

        if l1bUP.is_pressed():
            
            sclick.play()
            length1 += 0.01
            length1 = round(length1, 3) #my first case of why the heck is the value 3.20000000009
            
        if l1bDN.is_pressed():
            
            sclick.play()
            length1 -= 0.01
            length1 = round(length1, 3)
            


        if l2bUP.is_pressed():
            
            sclick.play()
            length2 += 0.01
            length2 = round(length2, 3)       
             
        if l2bDN.is_pressed():
            
            sclick.play()
            length2 -= 0.01
            length2 = round(length2, 3)
            


        if l3bUP.is_pressed():
            
            sclick.play()
            length3 += 0.01
            length3 = round(length3, 3) 
             
        if l3bDN.is_pressed():
            
            sclick.play()
            length3 -= 0.01
            length3 = round(length3, 3)
            


        if l4bUP.is_pressed():
            
            sclick.play()
            length4 += 0.01
            length4 = round(length4, 3) 
             
        if l4bDN.is_pressed():
            
            sclick.play()
            length4 -= 0.01
            length4 = round(length4, 3)
            


        if l5bUP.is_pressed():
            
            sclick.play()
            length5 += 0.01
            length5 = round(length5, 3) 
             
        if l5bDN.is_pressed():
            
            sclick.play()
            length5 -= 0.01
            length5 = round(length5, 3)
            


        if l6bUP.is_pressed():
            
            sclick.play()
            length6 += 0.01
            length6 = round(length6, 3) 
             
        if l6bDN.is_pressed():
            
            sclick.play()
            length6 -= 0.01
            length6 = round(length6, 3)
            

        if l7bUP.is_pressed():
            
            sclick.play()
            length7 += 0.01
            length7 = round(length7, 3) 
             
        if l7bDN.is_pressed():
            
            sclick.play()
            length7 -= 0.01
            length7 = round(length7, 3)
            


        if l8bUP.is_pressed():
            
            sclick.play()
            length8 += 0.01
            length8 = round(length8, 3) 
             
        if l8bDN.is_pressed():
            
            sclick.play()
            length8 -= 0.01
            length8 = round(length8, 3)
            

        if l9bUP.is_pressed():
            
            sclick.play()
            length9 += 0.01
            length9 = round(length9, 3) 
             
        if l9bDN.is_pressed():
            
            sclick.play()
            length9 -= 0.01
            length9 = round(length9, 3)
            

        if l10bUP.is_pressed():
            
            sclick.play()
            length10 += 0.01
            length10 = round(length10, 3)
            
        if l10bDN.is_pressed():
            
            sclick.play()
            length10 -= 0.01
            length10 = round(length10, 3)
            


        if l11bUP.is_pressed():
            
            sclick.play()
            length11 += 0.01
            length11 = round(length11, 3)       
             
        if l11bDN.is_pressed():
            
            sclick.play()
            length11 -= 0.01
            length11 = round(length11, 3)
            


        if l12bUP.is_pressed():
            
            sclick.play()
            length12 += 0.01
            length12 = round(length12, 3) 
             
        if l12bDN.is_pressed():
            
            sclick.play()
            length12 -= 0.01
            length12 = round(length12, 3)
            


        if l13bUP.is_pressed():
            
            sclick.play()
            length13 += 0.01
            length13= round(length13, 3) 
             
        if l13bDN.is_pressed():
            
            sclick.play()
            length13 -= 0.01
            length13 = round(length13, 3)
            


        if l14bUP.is_pressed():
            
            sclick.play()
            length14 += 0.01
            length14 = round(length14, 3) 
             
        if l14bDN.is_pressed():
            
            sclick.play()
            length14 -= 0.01
            length14 = round(length14, 3)
            


        if l15bUP.is_pressed():
            
            sclick.play()
            length15 += 0.01
            length15 = round(length15, 3) 
             
        if l15bDN.is_pressed():
            
            sclick.play()
            length15 -= 0.01
            length15 = round(length15, 3)
            

        if l16bUP.is_pressed():
            
            sclick.play()
            length16 += 0.01
            length16 = round(length16, 3) 
             
        if l16bDN.is_pressed():
            
            sclick.play()
            length16 -= 0.01
            length16 = round(length16, 3)
            

            


        # dab

        if da1bUP.is_pressed():
            
            sclick.play()
            dista1 += 0.01
            dista1 = round(dista1, 3)
            
        if da1bDN.is_pressed():
            
            sclick.play()
            dista1 -= 0.01
            dista1 = round(dista1, 3)
            


        if da2bUP.is_pressed():
            
            sclick.play()
            dista2 += 0.01
            dista2 = round(dista2, 3)       
             
        if da2bDN.is_pressed():
            
            sclick.play()
            dista2 -= 0.01
            dista2 = round(dista2, 3)
            


        if da3bUP.is_pressed():
            
            sclick.play()
            dista3 += 0.01
            dista3 = round(dista3, 3) 
             
        if da3bDN.is_pressed():
            
            sclick.play()
            dista3 -= 0.01
            dista3 = round(dista3, 3)
            


        if da4bUP.is_pressed():
            
            sclick.play()
            dista4 += 0.01
            dista4 = round(dista4, 3) 
             
        if da4bDN.is_pressed():
            
            sclick.play()
            dista4 -= 0.01
            dista4 = round(dista4, 3)
            


        if da5bUP.is_pressed():
            
            sclick.play()
            dista5 += 0.01
            dista5 = round(dista5, 3) 
             
        if da5bDN.is_pressed():
            
            sclick.play()
            dista5 -= 0.01
            dista5 = round(dista5, 3)


        if da6bUP.is_pressed():
            
            sclick.play()
            dista6 += 0.01
            dista6 = round(dista6, 3) 
             
        if da6bDN.is_pressed():
            
            sclick.play()
            dista6 -= 0.01
            dista6 = round(dista6, 3)
            

        if da7bUP.is_pressed():
            
            sclick.play()
            dista7 += 0.01
            dista7 = round(dista7, 3) 
             
        if da7bDN.is_pressed():
            
            sclick.play()
            dista7 -= 0.01
            dista7 = round(dista7, 3)
            

        if da8bUP.is_pressed():
            
            sclick.play()
            dista8 += 0.01
            dista8 = round(dista8, 3) 
             
        if da8bDN.is_pressed():
            
            sclick.play()
            dista8 -= 0.01
            dista8 = round(dista8, 3)
            

        if da9bUP.is_pressed():
            
            sclick.play()
            dista9 += 0.01
            dista9 = round(dista9, 3)
            
        if da9bDN.is_pressed():
            
            sclick.play()
            dista9 -= 0.01
            dista9 = round(dista9, 3)
            


        if da10bUP.is_pressed():
            
            sclick.play()
            dista10 += 0.01
            dista10 = round(dista10, 3)       
             
        if da10bDN.is_pressed():
            
            sclick.play()
            dista10 -= 0.01
            dista10 = round(dista10, 3)
            

        if da11bUP.is_pressed():
            
            sclick.play()
            dista11 += 0.01
            dista11 = round(dista11, 3) 
             
        if da11bDN.is_pressed():
            
            sclick.play()
            dista11 -= 0.01
            dista11 = round(dista11, 3)
            


        if da12bUP.is_pressed():
            
            sclick.play()
            dista12 += 0.01
            dista12 = round(dista12, 3) 
             
        if da12bDN.is_pressed():
            
            sclick.play()
            dista12 -= 0.01
            dista12 = round(dista12, 3)
            


        if da13bUP.is_pressed():
            
            sclick.play()
            dista13 += 0.01
            dista13 = round(dista13, 3) 
             
        if da13bDN.is_pressed():
            
            sclick.play()
            dista13 -= 0.01
            dista13 = round(dista13, 3)



        if da14bUP.is_pressed():
            
            sclick.play()
            dista14 += 0.01
            dista14 = round(dista14, 3) 
             
        if da14bDN.is_pressed():
            
            sclick.play()
            dista14 -= 0.01
            dista14 = round(dista14, 3)
            

        if da15bUP.is_pressed():
            
            sclick.play()
            dista15 += 0.01
            dista15 = round(dista15, 3) 
             
        if da15bDN.is_pressed():
            
            sclick.play()
            dista15 -= 0.01
            dista15 = round(dista15, 3)
            

        if da16bUP.is_pressed():
            
            sclick.play()
            dista16 += 0.01
            dista16 = round(dista16, 3) 
             
        if da16bDN.is_pressed():
            
            sclick.play()
            dista16 -= 0.01
            dista16 = round(dista16, 3)



        # dbb

        if db1bUP.is_pressed():
            
            sclick.play()
            distb1 += 0.01
            distb1 = round(distb1, 3)
            
        if db1bDN.is_pressed():
            
            sclick.play()
            distb1 -= 0.01
            distb1 = round(distb1, 3)
            


        if db2bUP.is_pressed():
            
            sclick.play()
            distb2 += 0.01
            distb2 = round(distb2, 3)       
             
        if db2bDN.is_pressed():
            
            sclick.play()
            distb2 -= 0.01
            distb2 = round(distb2, 3)
            


        if db3bUP.is_pressed():
            
            sclick.play()
            distb3 += 0.01
            distb3 = round(distb3, 3) 
             
        if db3bDN.is_pressed():
            
            sclick.play()
            distb3 -= 0.01
            distb3 = round(distb3, 3)
            


        if db4bUP.is_pressed():
            
            sclick.play()
            distb4 += 0.01
            distb4 = round(distb4, 3) 
             
        if db4bDN.is_pressed():
            
            sclick.play()
            distb4 -= 0.01
            distb4 = round(distb4, 3)
            


        if db5bUP.is_pressed():
            
            sclick.play()
            distb5 += 0.01
            distb5 = round(distb5, 3) 
             
        if db5bDN.is_pressed():
            
            sclick.play()
            distb5 -= 0.01
            distb5 = round(distb5, 3)
            


        if db6bUP.is_pressed():
            
            sclick.play()
            distb6 += 0.01
            distb6 = round(distb6, 3) 
             
        if db6bDN.is_pressed():
            
            sclick.play()
            distb6 -= 0.01
            distb6 = round(distb6, 3)
            

        if db7bUP.is_pressed():
            
            sclick.play()
            distb7 += 0.01
            distb7 = round(distb7, 3) 
             
        if db7bDN.is_pressed():
            
            sclick.play()
            distb7 -= 0.01
            distb7 = round(distb7, 3)
            

        if db8bUP.is_pressed():
            
            sclick.play()
            distb8 += 0.01
            distb8 = round(distb8, 3) 
             
        if db8bDN.is_pressed():
            
            sclick.play()
            distb8 -= 0.01
            distb8 = round(distb8, 3)
            

        if db9bUP.is_pressed():
            
            sclick.play()
            distb9 += 0.01
            distb9 = round(distb9, 3)
            
        if db9bDN.is_pressed():
            
            sclick.play()
            distb9 -= 0.01
            distb9 = round(distb9, 3)
            


        if db10bUP.is_pressed():
            
            sclick.play()
            distb10 += 0.01
            distb10 = round(distb10, 3)       
             
        if db10bDN.is_pressed():
            
            sclick.play()
            distb10 -= 0.01
            distb10 = round(distb10, 3)
            


        if db11bUP.is_pressed():
            
            sclick.play()
            distb11 += 0.01
            distb11 = round(distb11, 3) 
             
        if db11bDN.is_pressed():
            
            sclick.play()
            distb11 -= 0.01
            distb11 = round(distb11, 3)
            


        if db12bUP.is_pressed():
            
            sclick.play()
            distb12 += 0.01
            distb12 = round(distb12, 3) 
             
        if db12bDN.is_pressed():
            
            sclick.play()
            distb12 -= 0.01
            distb12 = round(distb12, 3)
            


        if db13bUP.is_pressed():
            
            sclick.play()
            distb13 += 0.01
            distb13 = round(distb13, 3) 
             
        if db13bDN.is_pressed():
            
            sclick.play()
            distb13 -= 0.01
            distb13 = round(distb13, 3)
            


        if db14bUP.is_pressed():
            
            sclick.play()
            distb14 += 0.01
            distb14 = round(distb14, 3) 
             
        if db14bDN.is_pressed():
            
            sclick.play()
            distb14 -= 0.01
            distb14 = round(distb14, 3)
            

        if db15bUP.is_pressed():
            
            sclick.play()
            distb15 += 0.01
            distb15 = round(distb15, 3) 
             
        if db15bDN.is_pressed():
            
            sclick.play()
            distb15 -= 0.01
            distb15 = round(distb15, 3)
            

        if db16bUP.is_pressed():
            
            sclick.play()
            distb16 += 0.01
            distb16 = round(distb16, 3) 
             
        if db16bDN.is_pressed():
            
            sclick.play()
            distb16 -= 0.01
            distb16 = round(distb16, 3)
            





        if saveB.is_pressed() and buttonDelay == False:
            
            click.play()
            saveAudio(sample_rate,frequency,duration,amplitude,attack,attacklen,attackenabled,length1,dista1,distb1,length2,dista2,distb2,length3,dista3,distb3,length4,dista4,distb4,length5,dista5,distb5,length6,dista6,distb6,length7,dista7,distb7,length8,dista8,distb8,length9,dista9,distb9,length10,dista10,distb10,length11,dista11,distb11,length12,dista12,distb12,length13,dista13,distb13,length14,dista14,distb14,length15,dista15,distb15,length16,dista16,distb16,testing,tuned,fadeenabled,attack_time,attack_samples,noise,release,reverbenabled)
            buttonDelay = True
            
        elif saveB.is_pressed() and buttonDelay == True:
            pass
        else: 
             buttonDelay = False
             
        if testB.is_pressed() and buttonDelay2 == False:
            
            click.play()
            testing = True
            saveAudio(sample_rate,frequency,duration,amplitude,attack,attacklen,attackenabled,length1,dista1,distb1,length2,dista2,distb2,length3,dista3,distb3,length4,dista4,distb4,length5,dista5,distb5,length6,dista6,distb6,length7,dista7,distb7,length8,dista8,distb8,length9,dista9,distb9,length10,dista10,distb10,length11,dista11,distb11,length12,dista12,distb12,length13,dista13,distb13,length14,dista14,distb14,length15,dista15,distb15,length16,dista16,distb16,testing,tuned,fadeenabled,attack_time,attack_samples,noise,release,reverbenabled)
            testS = pg.mixer.Sound('output/test.wav')
            testing = False
            testS.play()
            buttonDelay2 = True
            
        elif testB.is_pressed() and buttonDelay2 == True:
            pass
        else: 
             buttonDelay2 = False
             
        if fadeB.is_pressed() and buttonDelay3 == False:
            
            click.play()
            buttonDelay3 = True
            
            if fadeenabled == False:
                fadeenabled = True
                release = 0.25
                fadeB.new_image("resources/textures/fadeon.png", (1425, 50), 3, 3)
            elif release == 0.25 and fadeenabled == True:
                release = 0.5
                fadeB.new_image("resources/textures/fadeon2.png", (1425, 50), 3, 3)
            elif release == 0.5 and fadeenabled == True:
                release = 1.5
                fadeB.new_image("resources/textures/fadeon3.png", (1425, 50), 3, 3)
            elif release == 1.5 and fadeenabled == True:
                release = 2.5
                fadeB.new_image("resources/textures/fadeon4.png", (1425, 50), 3, 3)
            elif release == 2.5 and fadeenabled == True:
                release = 0.25
                fadeenabled = False
                fadeB.new_image("resources/textures/fadeoff.png", (1425, 50), 3, 3)
            
        elif fadeB.is_pressed() and buttonDelay3 == True:
            pass
        else: 
             buttonDelay3 = False
             
        if attackb.is_pressed() and buttonDelay4 == False:
            
            click.play()
            if attackenabled == True:
                attackenabled = False
                attackb.new_image("resources/textures/attackoff.png", (1425, 125), 3, 3)
            else:
                attackenabled = True
                attackb.new_image("resources/textures/attackon.png", (1425, 125), 3, 3)
            buttonDelay4 = True
            
        elif attackb.is_pressed() and buttonDelay4 == True:
            pass
        else: 
             buttonDelay4 = False
             
        if noiseb.is_pressed() and buttonDelay5 == False:
            
            click.play()
            if noise == True:
                noise = False
                noiseb.new_image("resources/textures/noiseoff.png", (1505, 50), 3, 3)
            else:
                noise = True
                noiseb.new_image("resources/textures/noiseon.png", (1505, 50), 3, 3)
            buttonDelay5 = True
            
        elif noiseb.is_pressed() and buttonDelay5 == True:
            pass
        else: 
             buttonDelay5 = False
             
        if lengthb.is_pressed() and buttonDelay6 == False:
            
            click.play()
            
            if duration == 1:
                duration = 2
                lengthb.new_image("resources/textures/speed2.png", (1505, 125), 3, 3)
            elif duration == 2:
                duration = 5
                lengthb.new_image("resources/textures/speed5.png", (1505, 125), 3, 3)
            elif duration == 5:
                duration = 10
                lengthb.new_image("resources/textures/speed10.png", (1505, 125), 3, 3)
            elif duration == 10:
                duration = 1
                lengthb.new_image("resources/textures/speed1.png", (1505, 125), 3, 3)
                
            
            buttonDelay6 = True
            
        elif lengthb.is_pressed() and buttonDelay6 == True:
            pass
        
        else: 
             buttonDelay6 = False
             
        if scrollB.is_pressed() and buttonDelay8 == False:
            
            click.play()
            if scroll:
                scroll = False
            else:
                scroll = True
            buttonDelay8 = True
            
        elif scrollB.is_pressed() and buttonDelay8 == True:
            pass
        else: 
             buttonDelay8 = False
             
        if clearB.is_pressed() and buttonDelay7 == False:
            
            click.play()
            length1  = 0 
            dista1  = 1    
            distb1 = 1
            
            length2  = 0  
            dista2  = 1    
            distb2 = 1
            
            length3  = 0   
            dista3  = 1   
            distb3 = 1
            
            length4  = 0    
            dista4  = 1  
            distb4 = 1
            
            length5  = 0   
            dista5  = 1    
            distb5 = 1
            
            length6  = 0  
            dista6  = 1  
            distb6 = 1
            
            length7  = 0   
            dista7  = 1  
            distb7 = 1
            
            length8  = 0  
            dista8  = 1    
            distb8 = 1

            length9  = 0    
            dista9  = 1    
            distb9 = 1.0
            
            length10 = 0   
            dista10 = 1   
            distb10 = 1.0
            
            length11 = 0  
            dista11 = 1  
            distb11 = 1.0

            length12 = 0   
            dista12 = 1   
            distb12 = 1.0
            
            length13 = 0  
            dista13 = 1   
            distb13 = 1.0
            
            length14 = 0  
            dista14 = 1  
            distb14 = 1.0
            
            length15 = 0   
            dista15 = 1    
            distb15 = 1
            
            length16 = 0   
            dista16 = 1   
            distb16 = 1
            buttonDelay7 = True
            
        elif clearB.is_pressed() and buttonDelay7 == True:
            pass
        else: 
             buttonDelay7 = False
             

        # ----== Drawing ==----------------------------------------------------------------------------------------------------------------------------------------------
        pg.display.set_caption(f'-=Cy`s Pipe Organ Simulation=-    -= Version Demo =-      -= FPS: {clock.get_fps():.1f} =-      -={time.strftime('%H:%M:%S:')}=-') # i really liked the layout of my engine
        
        window.fill('#492d13') #fun fact: the whole color sceem is based off of a charactor i made which is a mechanical pipe organ
                                        #[x,y,w,h]
        pg.draw.rect(window,'black',[0, 0, 1200, 200])
        pg.draw.rect(window,'#ffd700',[0, 200, 1200, 20])
        pg.draw.rect(window,'#ffd700',[0, 200, 20, 900])
        pg.draw.rect(window,'#ffd700',[1680, 0, 20, 1700])
        pg.draw.rect(window,'#ffd700',[1200, 0, 20, 220])
        pg.draw.rect(window,'#ffd700',[0, 880, 1700, 20])
        pg.draw.rect(window,'#ffd700',[1200, 0, 500, 20])
        pg.draw.rect(window,'#ffd700',[1200, 200, 500, 20])
        

        if scroll:
                scrollen += 1
        else:
                scrollen = 0

        for n in range(1200): # drawing the wavelength across the screen
            phase = R.uniform(0, 2*M.pi)
            frequency *= 1 + 0.0005 * M.sin(2*M.pi*5)
            
            m = n + scrollen
            
            sample = ((length1  * M.sin(dista1  * M.pi * frequency * distb1  * m / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * m / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * m / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * m / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * m / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * m / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * m / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * m / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * m / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * m / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * m / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * m / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * m / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * m / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * m / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * m / sample_rate)))
            sample = (sample * amplitude * 0.00025)
            sample = max(-32.768, min(32.767, int(sample)))
            pg.draw.circle(window,'red',(n,sample+100),1)
            

        l1bUP.draw(window)
        l1bDN.draw(window)
        l1bts = font.render(f'{length1}',False,(0,0,0))
        window.blit(l1bts,(75+175,315))
        
        l2bUP.draw(window)
        l2bDN.draw(window)
        l2bts = font.render(f'{length2}',False,(0,0,0))
        window.blit(l2bts,(150+175,315))
        
        l3bUP.draw(window)
        l3bDN.draw(window)
        l3bts = font.render(f'{length3}',False,(0,0,0))
        window.blit(l3bts,(225+175,315))
        
        l4bUP.draw(window)
        l4bDN.draw(window)
        l4bts = font.render(f'{length4}',False,(0,0,0))
        window.blit(l4bts,(300+175,315))
        
        l5bUP.draw(window)
        l5bDN.draw(window)
        l5bts = font.render(f'{length5}',False,(0,0,0))
        window.blit(l5bts,(375+175,315))
        
        l6bUP.draw(window)
        l6bDN.draw(window)
        l6bts = font.render(f'{length6}',False,(0,0,0))
        window.blit(l6bts,(450+175,315))
        
        l7bUP.draw(window)
        l7bDN.draw(window)
        l7bts = font.render(f'{length7}',False,(0,0,0))
        window.blit(l7bts,(525+175,315))
        
        l8bUP.draw(window)
        l8bDN.draw(window)
        l8bts = font.render(f'{length8}',False,(0,0,0))
        window.blit(l8bts,(600+175,315))
        
        l9bUP.draw(window)
        l9bDN.draw(window)
        l9bts = font.render(f'{length9}',False,(0,0,0))
        window.blit(l9bts,(675+175,315))
        
        l10bUP.draw(window)
        l10bDN.draw(window)
        l10bts = font.render(f'{length10}',False,(0,0,0))
        window.blit(l10bts,(750+175,315))
        
        l11bUP.draw(window)
        l11bDN.draw(window)
        l11bts = font.render(f'{length11}',False,(0,0,0))
        window.blit(l11bts,(825+175,315))
        
        l12bUP.draw(window)
        l12bDN.draw(window)
        l12bts = font.render(f'{length12}',False,(0,0,0))
        window.blit(l12bts,(900+175,315))
        
        l13bUP.draw(window)
        l13bDN.draw(window)
        l13bts = font.render(f'{length13}',False,(0,0,0))
        window.blit(l13bts,(975+175,315))
        
        l14bUP.draw(window)
        l14bDN.draw(window)
        l14bts = font.render(f'{length14}',False,(0,0,0))
        window.blit(l14bts,(1050+175,315))
        
        l15bUP.draw(window)
        l15bDN.draw(window)
        l15bts = font.render(f'{length15}',False,(0,0,0))
        window.blit(l15bts,(1125+175,315))
        
        l16bUP.draw(window)
        l16bDN.draw(window)
        l16bts = font.render(f'{length16}',False,(0,0,0))
        window.blit(l16bts,(1200+175,315))
        


        da1bUP.draw(window)
        da1bDN.draw(window)
        da1bts = font.render(f'{dista1}',False,(0,0,0))
        window.blit(da1bts,(75+175,515))
        
        da2bUP.draw(window)
        da2bDN.draw(window)
        da2bts = font.render(f'{dista2}',False,(0,0,0))
        window.blit(da2bts,(150+175,515))
        
        da3bUP.draw(window)
        da3bDN.draw(window)
        da3bts = font.render(f'{dista3}',False,(0,0,0))
        window.blit(da3bts,(225+175,515))
        
        da4bUP.draw(window)
        da4bDN.draw(window)
        da4bts = font.render(f'{dista4}',False,(0,0,0))
        window.blit(da4bts,(300+175,515))
            
        da5bUP.draw(window)
        da5bDN.draw(window)
        da5bts = font.render(f'{dista5}',False,(0,0,0))
        window.blit(da5bts,(375+175,515))
        
        da6bUP.draw(window)
        da6bDN.draw(window)
        da6bts = font.render(f'{dista6}',False,(0,0,0))
        window.blit(da6bts,(450+175,515))
        
        da7bUP.draw(window)
        da7bDN.draw(window)
        da7bts = font.render(f'{dista7}',False,(0,0,0))
        window.blit(da7bts,(525+175,515))
        
        da8bUP.draw(window)
        da8bDN.draw(window)
        da8bts = font.render(f'{dista8}',False,(0,0,0))
        window.blit(da8bts,(600+175,515))
        
        da9bUP.draw(window)
        da9bDN.draw(window)
        da9bts = font.render(f'{dista9}',False,(0,0,0))
        window.blit(da9bts,(675+175,515))
        
        da10bUP.draw(window)
        da10bDN.draw(window)
        da10bts = font.render(f'{dista10}',False,(0,0,0))
        window.blit(da10bts,(750+175,515))
        
        da11bUP.draw(window)
        da11bDN.draw(window)
        da11bts = font.render(f'{dista11}',False,(0,0,0))
        window.blit(da11bts,(825+175,515))
        
        da12bUP.draw(window)
        da12bDN.draw(window)
        da12bts = font.render(f'{dista12}',False,(0,0,0))
        window.blit(da12bts,(900+175,515))
            
        da13bUP.draw(window)
        da13bDN.draw(window)
        da13bts = font.render(f'{dista13}',False,(0,0,0))
        window.blit(da13bts,(975+175,515))
        
        da14bUP.draw(window)
        da14bDN.draw(window)
        da14bts = font.render(f'{dista14}',False,(0,0,0))
        window.blit(da14bts,(1050+175,515))
        
        da15bUP.draw(window)
        da15bDN.draw(window)
        da15bts = font.render(f'{dista15}',False,(0,0,0))
        window.blit(da15bts,(1125+175,515))
        
        da16bUP.draw(window)
        da16bDN.draw(window)
        da16bts = font.render(f'{dista16}',False,(0,0,0))
        window.blit(da16bts,(1200+175,515))
        


        db1bUP.draw(window)
        db1bDN.draw(window)
        db1bts = font.render(f'{distb1}',False,(0,0,0))
        window.blit(db1bts,(75+175,715))
        
        db2bUP.draw(window)
        db2bDN.draw(window)
        db2bts = font.render(f'{distb2}',False,(0,0,0))
        window.blit(db2bts,(150+175,715))
        
        db3bUP.draw(window)
        db3bDN.draw(window)
        db3bts = font.render(f'{distb3}',False,(0,0,0))
        window.blit(db3bts,(225+175,715))
        
        db4bUP.draw(window)
        db4bDN.draw(window)
        db4bts = font.render(f'{distb4}',False,(0,0,0))
        window.blit(db4bts,(300+175,715))
            
        db5bUP.draw(window)
        db5bDN.draw(window)
        db5bts = font.render(f'{distb5}',False,(0,0,0))
        window.blit(db5bts,(375+175,715))
        
        db6bUP.draw(window)
        db6bDN.draw(window)
        db6bts = font.render(f'{distb6}',False,(0,0,0))
        window.blit(db6bts,(450+175,715))
        
        db7bUP.draw(window)
        db7bDN.draw(window)
        db7bts = font.render(f'{distb7}',False,(0,0,0))
        window.blit(db7bts,(525+175,715))
        
        db8bUP.draw(window)
        db8bDN.draw(window)
        db8bts = font.render(f'{distb8}',False,(0,0,0))
        window.blit(db8bts,(600+175,715))
        
        db9bUP.draw(window)
        db9bDN.draw(window)
        db9bts = font.render(f'{distb9}',False,(0,0,0))
        window.blit(db9bts,(675+175,715))
        
        db10bUP.draw(window)
        db10bDN.draw(window)
        db10bts = font.render(f'{distb10}',False,(0,0,0))
        window.blit(db10bts,(750+175,715))
        
        db11bUP.draw(window)
        db11bDN.draw(window)
        db11bts = font.render(f'{distb11}',False,(0,0,0))
        window.blit(db11bts,(825+175,715))
        
        db12bUP.draw(window)
        db12bDN.draw(window)
        db12bts = font.render(f'{distb12}',False,(0,0,0))
        window.blit(db12bts,(900+175,715))
            
        db13bUP.draw(window)
        db13bDN.draw(window)
        db13bts = font.render(f'{distb13}',False,(0,0,0))
        window.blit(db13bts,(975+175,715))
        
        db14bUP.draw(window)
        db14bDN.draw(window)
        db14bts = font.render(f'{distb14}',False,(0,0,0))
        window.blit(db14bts,(1050+175,715))
        
        db15bUP.draw(window)
        db15bDN.draw(window)
        db15bts = font.render(f'{distb15}',False,(0,0,0))
        window.blit(db15bts,(1125+175,715))
        
        db16bUP.draw(window)
        db16bDN.draw(window)
        db16bts = font.render(f'{distb16}',False,(0,0,0))
        window.blit(db16bts,(1200+175,715))
        


        saveB.draw(window)
        testB.draw(window)
        fadeB.draw(window)
        attackb.draw(window)
        noiseb.draw(window)
        lengthb.draw(window)
        clearB.draw(window)
        scrollB.draw(window)
        #reverbB.draw(window)
        
        tip = font.render('F1=Save,F2=Load',False,(0,0,0))
        window.blit(tip,(1375,-5))
        wh = font.render('Wave Height',False,(0,0,0))
        window.blit(wh,(100,315))
        ww = font.render('Wave Width',False,(0,0,0))
        window.blit(ww,(100,515))
        ww2 = font.render('Wave Width 2',False,(0,0,0))
        window.blit(ww2,(100,715))
        num = font.render('1           2           3           4           5           6          7          8          9          10          11         12         13         14         15        16',False,(75,10,10))
        window.blit(num,(270,220))


        pg.display.flip()
        clock.tick(60)
        




def saveAudio(sample_rate,frequency,duration,amplitude,attack,attacklen,attackenabled,length1,dista1,distb1,length2,dista2,distb2,length3,dista3,distb3,length4,dista4,distb4,length5,dista5,distb5,length6,dista6,distb6,length7,dista7,distb7,length8,dista8,distb8,length9,dista9,distb9,length10,dista10,distb10,length11,dista11,distb11,length12,dista12,distb12,length13,dista13,distb13,length14,dista14,distb14,length15,dista15,distb15,length16,dista16,distb16,test,tuned,fadeenabled,attack_time,attack_samples,noiseenabled,release,reverbenabled): # that is a lot of parameters
    phase = 0
    
    if test == True:
        if tuned == True: #i might add the feature to make it out of tune but still sound good sometime
            with wave.open("output/test.wav", "w") as wav:
                wav.setnchannels(1) #mono
                wav.setsampwidth(2) #16 bit
                wav.setframerate(sample_rate)
                t = 0
                j=0
                if noiseenabled:
                    noise = np.random.normal(0,20,int(sample_rate * duration))
                else:
                    noise = np.zeros(int(sample_rate * duration))

                for n in range(int(sample_rate * duration)):
                    
                    frequency *= 1 + 0.0005 * M.sin(2*M.pi*5*t)
                    sample = ((length1  * M.sin(dista1  * M.pi * frequency * distb1  * n / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * n / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * n / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * n / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * n / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * n / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * n / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * n / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * n / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * n / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * n / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * n / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * n / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * n / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * n / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * n / sample_rate)))
                    if reverbenabled == True:
                        sample = sample + (((length1  * M.sin(dista1  * M.pi * frequency * distb1  * n+500 / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * n+500 / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * n+500 / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * n+500 / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * n+500 / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * n+500 / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * n+500 / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * n+500 / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * n+500 / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * n+500 / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * n+500 / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * n+500 / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * n+500 / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * n+500 / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * n+500 / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * n+500 / sample_rate)))*0.75)

                    if attackenabled:
                        if n < attack_samples:
                            envelope = n / attack_samples
                        else:
                            envelope = 1.0
                    else:
                        envelope = 1.0
                        
                    sample *= amplitude * 0.25 * envelope
                    sample += noise[n]*5
                    
                    
                    if n > sample_rate * (duration - release) and fadeenabled:
                        fade = (sample_rate * duration - n) / (sample_rate * release)
                        sample *= fade
                        
                    sample = max(-32768, min(32767, int(sample)))
                    wav.writeframes(struct.pack("<h", int(sample)))
                    

        if tuned == False:
            with wave.open("output/test.wav", "w") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(sample_rate)
                t = 0
                if noiseenabled:
                    noise = np.random.normal(0,20,int(sample_rate * duration))
                else:
                    noise = np.zeros(int(sample_rate * duration))

                for n in range(int(sample_rate * duration)):
                    
                    frequency *= 1 + 0.0005 * M.sin(2*M.pi*5*t)
                    sample = ((length1  * M.sin(dista1  * M.pi * frequency * distb1  * n / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * n / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * n / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * n / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * n / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * n / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * n / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * n / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * n / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * n / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * n / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * n / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * n / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * n / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * n / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * n / sample_rate)))
                    
                    if attackenabled:
                        if n < attack_samples:
                            envelope = n / attack_samples
                        else:
                            envelope = 1.0
                    else:
                        envelope = 1.0
                        
                    sample *= amplitude * 0.25 * envelope
                    
                    sample += noise[n]*5
                    

                    if n > sample_rate * (duration - release) and fadeenabled:
                        fade = (sample_rate * duration - n) / (sample_rate * release)
                        sample *= fade
                        
                    sample = max(-32768, min(32767, int(sample)))
                    wav.writeframes(struct.pack("<h", int(sample)))
                    


    if test == False:
        if tuned == True:
            with wave.open("output/organ.wav", "w") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(sample_rate)
                t = 0
                if noiseenabled:
                    noise = np.random.normal(0,20,int(sample_rate * duration))
                else:
                    noise = np.zeros(int(sample_rate * duration))

                for n in range(int(sample_rate * duration)):
                    
                    frequency *= 1 + 0.0005 * M.sin(2*M.pi*5*t)
                    sample = ((length1  * M.sin(dista1  * M.pi * frequency * distb1  * n / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * n / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * n / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * n / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * n / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * n / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * n / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * n / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * n / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * n / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * n / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * n / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * n / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * n / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * n / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * n / sample_rate)))
                    
                    if attackenabled:
                        if n < attack_samples:
                            envelope = n / attack_samples
                        else:
                            envelope = 1.0
                    else:
                        envelope = 1.0
                        
                    sample *= amplitude * 0.25 * envelope
                    
                    sample += noise[n]*5


                    if n > sample_rate * (duration - release) and fadeenabled:
                        fade = (sample_rate * duration - n) / (sample_rate * release)
                        sample *= fade
                        
                    sample = max(-32768, min(32767, int(sample)))
                    wav.writeframes(struct.pack("<h", int(sample)))
                    

        if tuned == False:
            with wave.open("output/organ.wav", "w") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(sample_rate)
                t = 0
                if noiseenabled:
                    noise = np.random.normal(0,20,int(sample_rate * duration))
                else:
                    noise = np.zeros(int(sample_rate * duration))

                for n in range(int(sample_rate * duration)):
                    
                    frequency *= 1 + 0.0005 * M.sin(2*M.pi*5*t)
                    sample = ((length1  * M.sin(dista1  * M.pi * frequency * distb1  * n / sample_rate)) +(length2  * M.sin(dista2  * M.pi * frequency * distb2  * n / sample_rate)) +(length3  * M.sin(dista3  * M.pi * frequency * distb3  * n / sample_rate)) +(length4  * M.sin(dista4  * M.pi * frequency * distb4  * n / sample_rate)) +(length5  * M.sin(dista5  * M.pi * frequency * distb5  * n / sample_rate)) +(length6  * M.sin(dista6  * M.pi * frequency * distb6  * n / sample_rate)) +(length7  * M.sin(dista7  * M.pi * frequency * distb7  * n / sample_rate)) +(length8  * M.sin(dista8  * M.pi * frequency * distb8  * n / sample_rate)) +(length9  * M.sin(dista9  * M.pi * frequency * distb9  * n / sample_rate)) +(length10 * M.sin(dista10 * M.pi * frequency * distb10 * n / sample_rate)) +(length11 * M.sin(dista11 * M.pi * frequency * distb11 * n / sample_rate)) +(length12 * M.sin(dista12 * M.pi * frequency * distb12 * n / sample_rate)) +(length13 * M.sin(dista13 * M.pi * frequency * distb13 * n / sample_rate)) +(length14 * M.sin(dista14 * M.pi * frequency * distb14 * n / sample_rate)) +(length15 * M.sin(dista15 * M.pi * frequency * distb15 * n / sample_rate)) +(length16 * M.sin(dista16 * M.pi * frequency * distb16 * n / sample_rate)))
                    
                    if attackenabled:
                        if n < attack_samples:
                            envelope = n / attack_samples
                        else:
                            envelope = 1.0
                    else:
                        envelope = 1.0
                        
                    sample *= amplitude * 0.25 * envelope
                    
                    sample += noise[n]*5
                    

                    if n > sample_rate * (duration - release) and fadeenabled:
                        fade = (sample_rate * duration - n) / (sample_rate * release)
                        sample *= fade
                        
                    sample = max(-32768, min(32767, int(sample)))
                    wav.writeframes(struct.pack("<h", int(sample)))


def load(): #strait from the ide but loads jsons
    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("JSON files", "*.json")]
    )

    root.destroy()

    if not filename:
        return None

    with open(filename, "r") as f:
        d = json.load(f)
        return d



if __name__ == "__main__":
    main()
    


pg.quit()




# /\_/\
#( o.o )
# > ^ <
#you found bob the cat