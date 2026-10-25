import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode(640, 400)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main)