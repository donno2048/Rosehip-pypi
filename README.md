Reliable Operating System by Elisha Hollander Implemented Python
# Rosehip
```diff
- this only works on windows
```
the source is [here](https://github.com/donno2048/Rosehip) there is also a [version for linux](https://github.com/donno2048/Rosehip-L), more specifically for ubuntu debian and mint.
## How to install it:

open cmd, then:

###### (you can open cmd using `win`+`R` then type `cmd`)
##### if you have python in your PATH:

```
> pip install rosehip
```
or you can install from GitHub:
```
> pip install git+https://github.com/donno2048/Rosehip-pypi
```
##### else:

```
> curl.exe -o python3.exe https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe --ssl-no-revoke -k
> python3.exe /quiet PrependPath=1
> del python3.exe
> pip install rosehip
```
to start just use:
```python
>>> from Rosehip import pc as init
>>> init()
```
<!--the Rosehip was miss written as rosehip!!!!!!!!!!!!!!!-->

in the python command line
###### (you can open it using `win`+`R` then type `python`)

If you're using a laptop replace 'pc' with 'laptop' or just run:

`rosehip`

## What can you do with it:

* press `HOME` button to open the menu bar or `FN`+`LEFT_ARROW` if you don't have any
* press `INSERT` button to open the painter
  * scroll up and down to change the size of the brush
  * scroll up and down while holding `ALT` button to change the color of the brush
  * scroll up and down while holding `CTRL` button to change the shape of the brush


## To do:
- [x] ~~[animations](https://en.wikipedia.org/wiki/Stop_motion)~~
- [x] ~~[pong](https://en.wikipedia.org/wiki/Pong)~~
- [x] ~~[python idle](https://www.python.org/)~~
- [x] ~~[html idle](https://en.wikipedia.org/wiki/HTML)~~
- [x] ~~[bat idle](https://en.wikipedia.org/wiki/Batch_file)~~
- [x] ~~[c# idle](https://docs.microsoft.com/en-us/dotnet/csharp/)~~
- [x] ~~[javascript idle](https://www.javascript.com/)~~
- [x] ~~[visual basic idle](https://docs.microsoft.com/en-us/dotnet/visual-basic/)~~
- [x] ~~[powershell idle](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)~~
- [x] ~~[chrome](https://en.wikipedia.org/wiki/Google_Chrome)~~
- [x] ~~[text based web-browser](https://en.wikipedia.org/wiki/Text-based_web_browser)~~
- [x] ~~[ogg music player](https://en.wikipedia.org/wiki/Ogg)~~
- [x] ~~[calculator](https://en.wikipedia.org/wiki/Calculator)~~
- [x] ~~[clock](https://en.wikipedia.org/wiki/Clock)~~
- [x] ~~[background color picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[background image picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[camera](https://en.wikipedia.org/wiki/Camera)~~
- [x] ~~[mp4 viewer](https://en.wikipedia.org/wiki/MPEG-4_Part_14)~~
- [x] ~~[maze](https://en.wikipedia.org/wiki/Maze)~~
- [ ] [CLI](https://en.wikipedia.org/wiki/Command-line_interface)

## For developers:

if you want to use it as an .iso you can run [another code I wrote](https://github.com/donno2048/CITUR) but it's currently having some issues, as specified is the [README](https://github.com/donno2048/CITUR/blob/master/README.md)...

or you can either use the [.iso builder](https://github.com/donno2048/CITUR-L) for the [linux version of Rosehip](https://github.com/donno2048/Rosehip-L)

## For extreme developers:

if you want to create .exe version yourself you need to install [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) version 6.1 using `pip install cx_Freeze==6.1` then change __every__ `os.path.realpath(__file__)` to `sys.executable` you might need to use `import sys` then in the directory of _os.py_ run:
```python3
from cx_Freeze import Executable,setup
setup(name='Rosehip',options={'build_exe':{'packages':'requests,pygame,pygame_gui,pyttsx3,pywintypes,comtypes,keyboard,wheel,Js2Py,selenium,chromedriver_autoinstaller,html2text,cv2'.split(','),'include_files':['image.jpg',('musics','musics'),('images','images'),('apps','apps')]}},executables=[Executable('os.py',base='Win32GUI')])
```
