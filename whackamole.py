import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if pos[0] in range(x, x + 32) and pos[1] in range(y, y + 32):
                        x = 32 * (random.randrange(0, 640) // 32)
                        y = 32 * (random.randrange(0, 512) // 32)
            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "dark blue", (32 + (32*i), 0), (32 + (32*i), 512))
            for i in range(16):
                pygame.draw.line(screen, "dark blue", (0, 32 + (32 * i)), (640, 32 + (32 * i)))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
