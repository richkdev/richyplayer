import os
import sys
import pygame
import asyncio


import richyplayer


def newPath(relPath: str) -> str:
    relPath = relPath.replace(("/" if len(relPath.split("/")) > 1 else "\\"), os.sep)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        basePath = sys._MEIPASS  # type: ignore -> pyinstaller temp folder
    else:
        basePath = os.path.abspath('.')
    return os.path.join(basePath, relPath)


async def main():
    player = richyplayer.VideoPlayer()
    await player.open(
        path="video.mp4",
        tmp_dir=newPath("/tmp/" if richyplayer.IS_WEB else "tmp/"),
        has_audio=False,
        override_audio_source=None,
    )

    screen = pygame.display.set_mode((player.width, player.height))
    clock = pygame.Clock()

    running = True
    frameIndex = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 0))

        # if player.has_audio and not player.busy_audio():
        #     player.play_audio(loops=1)
        player.set_frame(frameIndex)
        screen.blit(player.get_frame(), (0, 0))

        frameIndex += 1

        pygame.display.flip()
        clock.tick(30)
        await asyncio.sleep(0)

    player.close()
    pygame.quit()

asyncio.run(main())
