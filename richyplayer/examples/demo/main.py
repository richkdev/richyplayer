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
    relPath = relPath.replace(("/" if len(relPath.split("/")) > 1 else "\\"), os.sep)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        basePath = sys._MEIPASS  # type: ignore -> pyinstaller temp folder
    else:
        basePath = os.path.abspath('.')
    return os.path.join(basePath, relPath)


async def main():
    player = richyplayer.VideoPlayer()
    await player.open(
        path=newPath("assets/video.mp4") if richyplayer.IS_WEB else newPath("richyplayer/examples/demo/assets/video.mp4"),
        tmp_dir=newPath("/tmp/" if richyplayer.IS_WEB else "tmp/"),
        has_audio=True,
        override_audio_source=newPath("assets/override.mp3") if richyplayer.IS_WEB else newPath("richyplayer/examples/demo/assets/override.mp3"),
    )

    player2 = richyplayer.VideoPlayer()
    await player2.open(
        path="http://test-videos.co.uk/vids/bigbuckbunny/mp4/av1/360/Big_Buck_Bunny_360_10s_1MB.mp4",
        tmp_dir=newPath("/tmp/" if richyplayer.IS_WEB else "tmp/"),
        has_audio=False,
        override_audio_source=None,
    )

    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.Clock()

    running = True
    frameIndex = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 0))

        if player.has_audio and not player.busy_audio():
            player.play_audio(loops=1)
        player.set_frame(frameIndex)
        screen.blit(player.get_frame(), (0, 0))

        if player2.has_audio and not player2.busy_audio():
            player2.play_audio()
        player.set_frame(frameIndex)
        screen.blit(pygame.transform.scale_by(player2.get_frame(), 0.75), (500, 200))

        frameIndex += 1

        pygame.display.flip()
        clock.tick(30)
        await asyncio.sleep(0)

    player.close()
    player2.close()
    pygame.quit()

asyncio.run(main())
