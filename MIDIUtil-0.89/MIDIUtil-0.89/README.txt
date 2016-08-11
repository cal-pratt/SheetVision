========
MIDIUtil
========

------------
Introduction
------------

MIDIUtil is a pure Python library that allows one to write muti-track
Musical Instrument Digital Interface (MIDI) files from within Python
programs. It is object-oriented and allows one to create and write these
files with a minimum of fuss.

MIDIUtil isn't a full implementation of the MIDI specification. The actual
specification is a large, sprawling document which has organically grown
over the course of decades. I have selectively implemented some of the
more useful and common aspects of the specification. The choices have
been somewhat idiosyncratic; I largely implemented what I needed. When
I decided that it could be of use to other people I fleshed it out a bit,
but there are still things missing. Regardless, the code is fairly easy to
understand and well structured. Additions can be made to the library by
anyone with a good working knowledge of the MIDI file format and a good,
working knowledge of Python. Documentation for extending the library
is provided.

This software was originally developed with Python 2.5.2 and it makes use
of some features that were introduced in 2.5. I have used it extensively
in Python 2.6.

Included in this version is an intitial port to Python 3 (but which should
work in 2.6.X also). The file is called MidiFile3.py. To use it, use
the following import line in your code:

        from midiutil.MidiFile3 import MIDIFile

(This assumes that the code has been installed into your system path or that
the midiutil directory is copied into your script's working directory.)

This software is distributed under an Open Source license and you are
free to use it as you see fit, provided that attribution is maintained.
See License.txt in the source distribution for details.

------------
Installation
------------

To use the library one can either install it on one's system or
copy the midiutil directory of the source distribution to your
project's directory (or to any directory pointed to  by the PYTHONPATH
environment variable). For the Windows platforms an executable installer
is provided. Alternately the source distribution can be downloaded,
un-zipped (or un-tarred), and installed in the standard way:

    python setup.py install

On non-Windows platforms (Linux, MacOS, etc.) the software should be
installed in this way. MIDIUtil is pure Python and should work on any
platform to which Python has been ported.

If you do not wish to install in on your system, just copy the
src/midiutil directory to your project's directory or elsewhere on
your PYTHONPATH. If you're using this software in your own projects
you may want to consider distributing the library bundled with yours;
the library is small and self-contained, and such bundling makes things
more convenient for your users. The best way of doing this is probably
to copy the midiutil directory directly to your package directory and
then refer to it with a fully qualified name. This will prevent it from
conflicting with any version of the software that may be installed on
the target system.

-----------
Quick Start
-----------

Using the software is easy:

    o The package must be imported into your namespace
    o A MIDIFile object is created
    o Events (notes, tempo-changes, etc.) are added to the object
    o The MIDI file is written to disk.

Detailed documentation is provided; what follows is a simple example
to get you going quickly. In this example we'll create a one track MIDI
File, assign a name and tempo to the track, add a one beat middle-C to
the track, and write it to disk.

        #Import the library
        from midiutil.MidiFile import MIDIFile

        # Create the MIDIFile Object with 1 track
        MyMIDI = MIDIFile(1)

        # Tracks are numbered from zero. Times are measured in beats.
        track = 0
        time = 0

        # Add track name and tempo.
        MyMIDI.addTrackName(track,time,"Sample Track")
        MyMIDI.addTempo(track,time,120)

        # Add a note. addNote expects the following information:
        track = 0
        channel = 0
        pitch = 60
        time = 0
        duration = 1
        volume = 100

        # Now add the note.
        MyMIDI.addNote(track,channel,pitch,time,duration,volume)

        # And write it to disk.
        binfile = open("output.mid", 'wb')
        MyMIDI.writeFile(binfile)
        binfile.close()

There are several additional event types that can be added and there are
various options available for creating the MIDIFile object, but the above
is sufficient to begin using the library and creating note sequences.

The above code is found in machine-readable form in the examples directory.
A detailed class reference and documentation describing how to extend
the library is provided in the documentation directory.

Have fun!

---------
Thank You
---------

I'd like to mention the following people who have given feedback, but
fixes,  and suggestions on the library:

    Bram de Jong
    Mike Reeves-McMillan
    Egg Syntax
    Nils Gey
    Francis G.
