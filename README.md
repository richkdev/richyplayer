# richyplayer

a video player library for pygame-ce, works on desktop and web

supports python 3.9+

## features

* ability to fetch local & web videos on both desktop & web
* ability to play said videos with its original audio[[1]](#note1), override the audio, or no sound at all
* works on:
  * desktop: windows, linux, raspberry pi os, etc.
  * web: currently only pygbag[[1]](#note1), pyodide 0.27.7[[2]](#note2) & pyscript 2025.7.3[[3]](#note3)

## installation

### desktop

put this in your cli: `pip install git+https://github.com/richkdev/richyplayer.git` then just do `import richyplayer`

### web

put the entire `richyplayer` folder inside the the root folder as your main.py[[3]](#notes)

BEFORE:

```text
my-project
├── img/
│   └── image.png
├── sfx/
│   └── sound.mp3
├── main.py
├── README.md
└── requirements.txt
```

AFTER:

```text
my-project
├── richyplayer/
│   ├── __init__.py
│   ├── richyplayer.py
│   └── ...
├── img/
│   └── image.png
├── sfx/
│   └── sound.mp3
├── main.py
├── README.md
└── requirements.txt
```

## usage

check `richyplayer/examples/` for examples on how to use the `richyplayer`

## notes

1. <span id="note1">some features don't work on some web platforms, known issues include:</span>
   1. original video's audio can't be played on all supported web platforms. the workaround is to play the put the audio in a different file - whether it be local or web - and pass the path to the `override_audio_source` param in `VideoPlayer.open()`.
   2. lots of things in pygame-ce 2.4.2+ cannot be used on web for compatibility with pyodide & pyscript, since pyodide 0.27.7 only has pygame-ce 2.4.1 built-in at the moment[[2]](#note2)
2. <span id="note2">pyodide removed pygame-ce in 0.28.0, so `richyplayer` uses 0.27.7 just to use pygame-ce. you could technically bundle a wheel for pygame-ce 2.4.2+ and use it. check [pyodide docs](https://pyodide.org/en/stable/project/changelog.html#version-0-28-0) for more info</span>
3. <span id="note3">pyscript 2025.7.3 uses bundled pyodide 0.27.6, whereas pygame-ce hasn't been removed. if you manually set the `interpreter` option in pyscript config to be pyodide 0.27.7 when using pyscript 2025.8.1+, it will still use their pyodide version's built-in packages. in our case, pyscript 2025.8.1 which uses pyodide 0.28.1 doesn't have pygame-ce[[2]](#note2)</span>

## references

references when using the `richyplayer`

* pygame-ce
  * <https://pyga.me/docs/> (make sure to check when a specific pygame-ce feature was added/removed/modified)
* opencv-python
  * <https://docs.opencv.org/4.10.0/d6/d00/tutorial_py_root.html>
* urllib3
  * <https://urllib3.readthedocs.io/en/2.2.3/>
* pygbag
  * <https://github.com/pygame-web/pygbag>
  * <https://pygame-web.github.io/>
* pyodide
  * <https://pyodide.org/en/0.27.7/usage/packages-in-pyodide.html>
  * <https://pyodide.org/en/0.27.7/usage/sdl.html>
* pyscript
  * <https://docs.pyscript.net/2025.7.3/>
  * <https://docs.pyscript.net/2025.7.3/user-guide/pygame-ce/>

## license

[MIT](/LICENSE)
