# /// script
# dependencies = [
#   'numpy',
#   'opencv-python',
#   'pygame-ce'
# ]
# ///

import os
import sys
import pygame
import asyncio

import richyplayer


def newPath(relPath: str) -> str:
    relPath = relPath.replace(
        ("/" if len(relPath.split("/")) > 1 else "\\"), os.sep)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        basePath = sys._MEIPASS  # type: ignore -> pyinstaller temp folder
    else:
        basePath = os.path.abspath('.')
    return os.path.join(basePath, relPath)


async def main():
    player = richyplayer.VideoPlayer()
    await player.open(
        path=newPath("assets/quaso.mp4" if richyplayer.IS_WEB else "richyplayer/examples/minimal/assets/quaso.mp4"),
        tmp_dir=newPath("/tmp/" if richyplayer.IS_WEB else "tmp/"),
        has_audio=True,
        override_audio_source=None,
    )

    screen = pygame.display.set_mode((player.width, player.height))
    clock = pygame.Clock()

    running = True
    frame_no = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 0))

        if player.has_audio and not player.busy_audio():
            player.play_audio(loops=0)
        player.set_frame(frame_no)
        screen.blit(player.get_frame(), (0, 0))

        frame_no += 1

        pygame.display.flip()
        clock.tick(player.FPS)
        await asyncio.sleep(0)

    player.close()
    pygame.quit()


asyncio.run(main())
