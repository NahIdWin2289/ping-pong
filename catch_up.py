from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("dota2_fon.jpeg"), (700, 500))
mixer.init()
font.init()
space_music = mixer.Sound('space.ogg')
mixer.music.load('space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play(-1)
kick_music = mixer.Sound('kick.ogg')
kick_music.set_volume(0.1)
clock = time.Clock()
FPS = 60
left_count = 0
right_count = 0

font1 = font.SysFont('Arial', 50)
count_text = font1.render(str(left_count) + ':' + str(right_count), 1, (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (40, 110)):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= 460 or self.rect.y <= 0:
            self.speed_y *= -1



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < 500 - 110:
            self.rect.y += self.speed_y
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < 500 - 110:
            self.rect.y += self.speed_y

platform_left = Player('bita.png', 35, 200, 5)
platform_right = Player('bita.png', 625, 200, 5)
boll = Ball('beysboll_boll.png', 350, 250, 3, (40, 40))

game = True
finish = False
while game:
    window.blit(background, (0, 0))
    if finish == False:
        platform_left.reset()
        platform_right.reset()
        platform_left.update()
        platform_right.update2()
        boll.reset()
        boll.update()
        window.blit(count_text, (325, 2))
        



        if sprite.collide_rect(platform_left, boll):
            boll.speed_x = 3
            kick_music.play()
        if sprite.collide_rect(boll, platform_right):
            boll.speed_x = -3
            kick_music.play()
        if boll.rect.x <= 0:
            right_count += 1
            boll.rect.x = 350
            boll.rect.y = 250
            count_text = font1.render(str(left_count) + ':' + str(right_count), 1, (255, 255, 255))
        if boll.rect.x >= 700:
            left_count +=1
            boll.rect.x = 350
            boll.rect.y = 250
            count_text = font1.render(str(left_count) + ':' + str(right_count), 1, (255, 255, 255))
        if left_count == 3:
            finish = True
            win = font1.render('Left player win', 1, (255, 255, 255))
        if right_count == 3:
            finish = True
            win = font1.render('Right player win', 1, (255, 255, 255))
            
    if finish == True:
        window.blit(win, (200, 270))
        

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                    finish = False
                    left_count = 0
                    right_count = 0
                    count_text = font1.render(str(left_count) + ':' + str(right_count), 1, (255, 255, 255))
    clock.tick(FPS)
    display.update()
    


#обработай событие «клик по кнопке "Закрыть окно"»
