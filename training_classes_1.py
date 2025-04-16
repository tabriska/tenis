from pygame import *
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
wondow.fill(back)
clock = time.Clock()
FPS = 60
game = True
speed_x = 3
speed_y = 3
font1 = font.Font(None,35)
lose1 = font1.render('Player 1 LOSE!', True (180,0,0) 
font2 = font.Font(None,35)
lose2 = font2.render('Player 2 LOSE!', True (180,0,0) 
while game:
    from e in event.get():
        if e.type = QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(200,200)
     if ball.rect.x < 600:
        finish = True
        window.blit(lose2,(200,200)
