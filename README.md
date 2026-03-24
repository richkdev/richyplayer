# richyplayer

a video player library for pygame-ce, works on desktop and web

supports python 3.9+

## features

* ability to fetch local & web videos on both desktop & web
* ability to play said videos with its original audio[[1]](#note1), override the audio, or no sound at all
* works on:
  * desktop: windows, linux, raspberry pi os, etc.
  * web: pygbag, pyodide & pyscript[[2]](#note2)

## installation

### desktop

put this in your cli: `pip install git+https://github.com/richkdev/richyplayer.git` then just do `import richyplayer`

### web

put the entire `richyplayer` folder inside the the root folder as your main.py

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

1. <span id="note1">original video's audio can't be played on all supported web platforms. the workaround is to play the put the audio in a different file - whether it be local or web - and pass the path to the `override_audio_source` param in `VideoPlayer.open()`.</span>
2. <span id="note2">on pyodide, pass enableRunUntilComplete: false to loadPyodide so that the old no-op behavior is enabled.</span>

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
  * <https://pyodide.org/en/stable/usage/packages-in-pyodide.html>
  * <https://pyodide.org/en/stable/usage/sdl.html>
* pyscript
  * <https://docs.pyscript.net/>
  * <https://docs.pyscript.net/2026.3.1/user-guide/pygame-ce/>

## license

[MIT](/LICENSE)
