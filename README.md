# richyplayer

a video player library for pygame(-ce), works on desktop and web

currently supports:

* desktop (windows, linux, raspberry pi os, etc)
* web (currently only pygbag, working on pyodide & pyscript compat)

## installation

put this in your cli: `pip install git+https://github.com/richkdev/richyplayer.git` then just do `import richyplayer`

## usage

```python
# /// script
# dependencies = [
#   'numpy',
#   'opencv-python',
#   'pygame-ce'
# ]
# ///

import richyplayer

async def main():
    # code here
    ...

asyncio.run(main())
```

PEP 723 header at the top of the file is for `pygbag`

## license

MIT
