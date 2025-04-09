from pygame import *
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
wondow.fill(back)
clock = time.Clock()
FPS = 60
game = True
while game:
    from e in event.get():
        if e.type = QUIT:
            game = False
    display.update()
    clock.tick(FPS)