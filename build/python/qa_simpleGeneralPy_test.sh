#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/src/gnuradio/gnuradio/gr-simple/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/src/gnuradio/gnuradio/gr-simple/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/usr/src/gnuradio/gnuradio/gr-simple/build/swig:$PYTHONPATH
/usr/bin/python2 /usr/src/gnuradio/gnuradio/gr-simple/python/qa_simpleGeneralPy.py 