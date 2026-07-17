# Cy`s Pipe Organ Simulation #
A Complex Program Designed to Make Sounds and Synths Written in Python/Pygame.
<img width="1699" height="931" alt="image" src="https://github.com/user-attachments/assets/762ae373-ff5a-4654-908a-20323124734b" />
## Download

Download the latest version here:

[**Download**]((https://github.com/Cybrock9000/Organ-Simulation/releases/tag/Demo))

## Features

- 16 waves to control
- Inprogram sound testing
- Save and load presets
- Add attack, fade, and noise effects
- Written in Python and Pygame

## How To Use ##
This program can be very complicated and could leave people clueless on what they are looking at. So that is why I am writing this section. When the program starts, you'll see a grid containing 96 buttons. Each column represents one sine wave/harmonic/wave (all the same) , and the rows control different properties of that wave.There are 3 main rows, the top row is the wave height, and the bottom 2 are wavelengths. To make good sounding waves I would recommend having the middle row be even numbers that are square roots (1,2,4,8,16,32,ect) and simple fractions (0.125,0.25,0.50). I wouldt really touch the bottom row unless you have some experience because it multiplies the width, so if your width is an 8 and you set the bottom to 2 then it would be a 16. Your sound can be exported as a wav file by pressing SAVE WAV (this will save to the 'output' folder as organ.wav and does overwrite if you save again without changing the name) and you can test the sound in the program by pressing the TEST button (this will make another file in the 'output' folder called test.wav). Then there are ATTACK, FADE and NOISE buttons to the right of the save and test buttons all they do is enable or disable what they are. There is the duration button which shows how long you want the sound to output (the longer the duration, the longer the wait but its not that bad). And lastly for buttons, the clear button (big old C button). It sets all top row values to 0 and the botton 2 rows to 1. You can save your wave pattern for later by pressing F1 (will save to 'soundbank' as yourSound.json and does overwrite if you save again without changin the name). You can press F2 to load any compatible json file (this does rewrite your progress in the program).
## Thanks to ##
my absolute LEGEND of a hamster Sunny
