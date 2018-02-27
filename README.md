## Sheet Vision

Sheet Vision is a python program which reads sheet music and turns it into midi files.

![image](https://cloud.githubusercontent.com/assets/7611406/17604255/9819f878-5fef-11e6-8f49-865d07284803.png)

## Developing a Sheet Music Reader
Calvin Gregory, and Calvert Pratt

### I.	Introduction
Applications in the field of Music Optical Character Recognition (OCR), also referred to as Optical Music Recognition, are an application of machine vision which serves to simplify the sight reading learning process and speed up music transcription. The sheet music reader application SheetVision was developed to convert single-tone lines of written music into a computer readable format for audio song playback. It does this through a template image matching algorithm implemented in Python using OpenCV which searches the target image for instances of each music character type such as notes, flats, and sharps. These characters are then identified, sequenced, and exported to a MIDI file for playback. 

### II.	Project Scope
The sheet music reader application was designed to convert images of written sheet music into a computer-readable format. SheetVision takes in an image of written sheet music, classifies all relevant music characters in the image, then generates and exports a MIDI file with all of the classified characters properly sequenced and identified as music notations. The application can handle single tone sequences of notes consisting of whole, half, quarter, and paired eighth (Ti-Ti) notes. It also interprets key signatures (sharp and flat symbols included at the beginning of a line) and rest characters. SheetVision is capable of interpreting most simple to moderate complexity sheet music arrangements written for single-tone instruments such as woodwinds, strings, and vocals. 

### III.	Algorithm
The algorithm used for music character identification uses the following series of steps to categorize each note or symbol in the target image:
 - A.	Image Filtering / Binary Conversion
 - B.	Template Scaling
 - C.	Character Classification
 - D.	Classifier Thresholding
 - E.	Note Identification and Sequencing
 - F.	Export results to MIDI

------------------

#### Libraries sourced from http://www.lfd.uci.edu/~gohlke/pythonlibs/
- (for x64)
  - numpy-1.11.1+mkl-cp35-cp35m-win_amd64.whl
  - matplotlib-1.5.2-cp35-cp35m-win_amd64.whl
  - opencv_python-3.1.0-cp35-cp35m-win_amd64.whl
- (for x86) 
  - numpy-1.11.1+mkl-cp35-cp35m-win32.whl
  - matplotlib-1.5.2-cp35-cp35m-win32.whl
  - opencv_python-3.1.0-cp35-cp35m-win32.whl

Midiutil Python 3 version is included in this repo
