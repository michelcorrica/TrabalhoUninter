import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.jpg')
        self.rect = self.surf.get_rect(left=0,top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50,'Corrica',(15,240,150),((WIN_WIDTH/2),70))
            self.menu_text(50, 'Game', (15, 240,150), ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(25,MENU_OPTION[i],(255,255,255),((WIN_WIDTH / 2), 200+30*i))

            pygame.display.flip()

            #check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
                text_font: Font = pygame.font.SysFont(name="Courier New", size=text_size, bold=True)
                text_surf: Surface = text_font.render(text, True, text_color)
                text_rect: Rect = text_surf.get_rect(center=text_center_pos)
                self.window.blit(source=text_surf, dest=text_rect)