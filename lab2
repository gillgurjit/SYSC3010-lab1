from sense_hat import SenseHat
import time

s = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)

def gurjit():
    B = blue
    O = nothing
    logo = [
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, O, O, O, O, O, O,
        B, B, O, O, B, B, B, B,
        B, B, O, O, B, B, B, B,
        B, B, O, O, O, O, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        ]
    return logo

def gill():
    R = red
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, R, R, R, R, O, O,
        O, O, R, O, O, O, O, O,
        O, O, R, O, R, R, O, O,
        O, O, R, O, O, R, O, O,
        O, O, R, R, R, R, O, O,
        O, O, O, O, O, O, O, O,
        ]
    return logo

while True:
        
    for event in s.stick.get_events():
        
        if event.action == "pressed":
            
            if event.direction == "left":
                
                s.set_pixels(gurjit())
                
            elif event.direction == "right":
                
                s.set_pixels(gill())
