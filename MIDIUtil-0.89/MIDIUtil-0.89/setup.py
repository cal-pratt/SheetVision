from distutils.core import setup

setup(name='MIDIUtil',
      version='0.89',
      description='MIDIUtil, a MIDI Interface for Python',
      author='Mark Conway Wirt',
      author_email='emergentmusics) at (gmail . com',
      license='Copyright (C) 2009, Mark Conway Wirt. See License.txt for details.',
      url='www.emergentmusics.org',
      packages=["midiutil"],
      package_dir = {'midiutil': 'src/midiutil'},
      package_data={'midiutil' : ['../../documentation/*']},
      scripts=['examples/single-note-example.py'],
      platforms='Platform Independent',
      long_description='''
This package provides a simple interface to allow Python programs to
write multi-track MIDI files.'''
     )
