import random

import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_size = mole_image.get_size()

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_position = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_position
                    if mole_x <= mouse_x < mouse_x + mole_size[0] and mole_y <= mouse_y < mole_y + mole_size[1]:
                        mole_position = (
                            random.randrange (0, 640, 32),
                            random.randrange(0, 512, 32),
                        )
                    print(event.pos) #need the player to be able to click anywhere within the square of the mole
            screen.fill((255, 163, 130))

            for x in range (0, 640, 32):
                pygame.draw.line(screen, ((191, 38, 27)), (x, 0), (x, 512))
            for y in range (0, 512, 32):
                pygame.draw.line(screen, ((191, 38, 27)), (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

#I forgot to push
if __name__ == "__main__":
    main()
