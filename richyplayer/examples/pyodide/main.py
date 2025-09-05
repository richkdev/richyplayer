# ive fcked up this file too much to the point it only works on pyodide and desktop and not pygbag

import os
import sys
import pygame
import asyncio

import richyplayer

if richyplayer.IS_PYODIDE:
    baseURL: str

def newPath(relPath: str):
    relPath = relPath.replace(("/" if len(relPath.split("/"))>1 else "\\"), os.sep)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        basePath = sys._MEIPASS # type: ignore -> pyinstaller temp folder
    elif richyplayer.IS_PYODIDE:
        basePath = baseURL # type: ignore -> baseURL is set by pyodide
    else:
        basePath = os.path.abspath('.')
    return os.path.join(basePath, relPath)

VIDEO = "video.mp4" if richyplayer.IS_PYODIDE else "richyplayer\\examples\\pyodide\\assets\\video.mp4"
AUDIO = "override.mp3" if richyplayer.IS_PYODIDE else "richyplayer\\examples\\pyodide\\assets\\override.mp3"

async def main():
    player = richyplayer.VideoPlayer()
    await player.open(
        path=VIDEO if richyplayer.IS_PYODIDE else newPath(VIDEO),
        tmp_dir=newPath("/tmp/" if richyplayer.IS_WEB else "tmp/"),
        has_audio=True,
        override_audio_source=AUDIO if richyplayer.IS_PYODIDE else newPath(AUDIO),
    )

    audio_played = False

    screen = pygame.display.set_mode((player.width, player.height))
    clock = pygame.Clock()

    frame_no = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        frame_no += 1

        if not audio_played:
            audio_played = not audio_played
            if player.has_audio and not player.busy_audio():
                player.play_audio()

        player.set_frame(frame_no)
        screen.blit(player.get_frame(), (0, 0))

        pygame.display.flip()
        clock.tick(player.FPS)

        if richyplayer.IS_PYODIDE:
            await asyncio.sleep(1/player.FPS)
        else:
            await asyncio.sleep(0)

    player.close()
    pygame.quit()

if __name__ ==  "__main__":
    if richyplayer.IS_PYODIDE: # required if you want to not get `RuntimeError` on pyodide
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    else:
        asyncio.run(main())
