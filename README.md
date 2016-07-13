## Sheet Vision

Sheet Vision is a python program which reads sheet music and turns it into midi files.

------------------
## Installing a virtual environment for windows

#### Install [python 3.5.2](https://www.python.org/downloads/windows/)
 - choose Python 3.5.2 Windows executable installer for your system
 - open installer and choose "custom install" and then hit "next"
  - check 'install for all users' 
  - check 'add python to environment variables'
  - change install location to "C:\Python35" 
  - install
            
#### Open powershell in administrator mode:
```
mkdir <project dir>
cd <project dir>
Set-ExecutionPolicy RemoteSigned
(type 'Y' when prompted)
```
#### Verify python install:
```
python --version
```
#### install ez_setup:
```
wget https://bootstrap.pypa.io/ez_setup.py -OutFile ez_setup.py
python ez_setup.py
```
#### Install pip:
```
wget https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
python get-pip.py
```
#### Verify pip
```
pip --version
```
#### Install virtualenv
```
pip install virtualenv
python -m virtualenv venv
```
#### Use the newly created virtual environment
```
.\venv\Scripts\activate
```
If you see a (venv) before the prompt, youre good to go!!

------------------
## Install project dependancies for windows

#### Download wheels from http://www.lfd.uci.edu/~gohlke/pythonlibs/
- (for x64)
  - numpy-1.11.1+mkl-cp35-cp35m-win_amd64.whl
  - matplotlib-1.5.2-cp35-cp35m-win_amd64.whl
  - opencv_python-3.1.0-cp35-cp35m-win_amd64.whl
- (for x86) 
  - numpy-1.11.1+mkl-cp35-cp35m-win32.whl
  - matplotlib-1.5.2-cp35-cp35m-win32.whl
  - opencv_python-3.1.0-cp35-cp35m-win32.whl

#### Open powershell in administrator mode and use virtual environment:
```
pip install .\numpy...
pip install .\matplotlib...
pip install .\opencv_python...
```
#### Verify opencv
```
python
    >>> import cv2
    >>> print(cv2.__version__)
    >>> exit()
```
If you see the version, everything went okay!
