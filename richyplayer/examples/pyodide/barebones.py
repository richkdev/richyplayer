# ive fcked up this file too much to the point it only works on pyodide and desktop and not pygbag

import os
import sys
import cv2
import pygame
import asyncio
import urllib3

IS_WEB = sys.platform in ('emscripten', 'wasi')
IS_PYODIDE = "pyodide" in sys.modules

# print("pyodide?", IS_PYODIDE)
# print(cv2.getBuildInformation())

if IS_PYODIDE:
    baseURL: str

def newPath(relPath: str):
    relPath = relPath.replace(("/" if len(relPath.split("/"))>1 else "\\"), os.sep)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        basePath = sys._MEIPASS # type: ignore -> pyinstaller temp folder
    elif IS_PYODIDE:
        basePath = baseURL # type: ignore -> baseURL is set by pyodide
    else:
        basePath = os.path.abspath('.')
    return os.path.join(basePath, relPath)

RAWR = "video.mp4" if IS_PYODIDE else "richyplayer\\examples\\pyodide\\assets\\video.mp4"  # is this way because of fetch_and_move func in index.html
LMAO = "override.mp3" if IS_PYODIDE else "richyplayer\\examples\\pyodide\\assets\\override.mp3" # is this way because of fetch_and_move func in index.html

poolmgr = urllib3.PoolManager()


if not IS_PYODIDE and not pygame.mixer.get_init():
    pygame.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(64)

if IS_PYODIDE:
    from pyodide.code import run_js # type: ignore

    file_extensions = ["mp3"] # will add more later

    def fetch_file(path: str, poolmgr: urllib3.PoolManager) -> bytes:
        resp = poolmgr.request("GET", path, preload_content=False)
        if resp.status == 200:
            data = resp.read()
            print(f"Data at {path} downloaded successfully.")
        else:
            data = bytes(0)
            print(f"Failed to download data at {path}. Status code: {resp.status}")
        resp.release_conn()
        return data

    def play_web_audio(path: str, poolmgr: urllib3.PoolManager) -> None:
        for ex in file_extensions:
            if "."+ex in path:
                # will fail if there hasnt been any user interaction after loading
                run_js(f"""
                    const audioBlob = new Blob([new Uint8Array({list(fetch_file(path, poolmgr))})], {{ type: 'audio/{ex}' }});
                    const audioUrl = URL.createObjectURL(audioBlob);
                    const audio = new Audio(audioUrl);
                    audio.play();
                """)
                break

async def main():
    audio_played = False
    if IS_PYODIDE:
        url = RAWR
    else:
        url = newPath(RAWR)
        audio = pygame.mixer.Sound(newPath(LMAO))
        channel = pygame.mixer.find_channel()

    print("url to the vid", url)

    video = cv2.VideoCapture()

    video.open(url)

    print("VIDEO OPENED", video.isOpened())

    if video.isOpened():
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        FPS = int(video.get(cv2.CAP_PROP_FPS))
        print("SUCCESS", width, height, FPS)
    else:
        print("FAILED")

    screen = pygame.display.set_mode((width, height))
    clock = pygame.Clock()

    frameNumber = 0

    running = True
    print("VIDEO START")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        video.set(cv2.CAP_PROP_POS_FRAMES, frameNumber)
        status, video_frame = video.read()

        if not audio_played:
            audio_played = not audio_played
            if IS_PYODIDE:
                # can play multiple sounds!
                play_web_audio(newPath("assets/override.mp3"), poolmgr)
                play_web_audio("https://ebe474db-a244-4ac4-a274-1326c2b72627.mdnplay.dev/shared-assets/audio/t-rex-roar.mp3", poolmgr) # can play multiple at the same time
            else:
                channel.play(audio)

        if video_frame is not None:
            frameNumber += 1

            image = pygame.image.frombuffer(video_frame.tobytes(), video_frame.shape[1::-1], "BGR")
            screen.blit(image, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)

        if IS_PYODIDE:
            await asyncio.sleep(1/FPS)
        else:
            await asyncio.sleep(0)

    print("VIDEO END")
    video.release()
    pygame.quit()

if __name__ ==  "__main__":
    if IS_PYODIDE: # required if you want to not get `RuntimeError` on pyodide
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    else:
        asyncio.run(main())
