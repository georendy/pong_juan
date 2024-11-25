import pygame

""" SCENE """
LEBAR_SCENE = 500
TINGGI_SCENE = 500
BG = pygame.image.load("galaxy.jpg")
SCENE = pygame.display.set_mode((LEBAR_SCENE, TINGGI_SCENE))
FPS = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__ (self, file_name, x, y, speed, lebar, tinggi):
        super().__init__()
        self.gambar = pygame.transform.scale(image.load(file_name), (lebar, tinggi))
        self.kecepatan = speed
        self.kotak = self.gambar.get_rect() ## membuat kotak dari ukuran gambar
        self.kotak.x = x
        self.kotak.y = y
    # def tampil(self):

""" GAME LOOP """
run_game = True
while run_game:
    SCENE.blit(BG, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
            break

    pygame.display.update()
    FPS.tick(60)




