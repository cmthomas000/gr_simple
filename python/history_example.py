#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr

class history_example(gr.basic_block):
    """
    docstring for block history_example
    """
    def __init__(self, history):
        gr.basic_block.__init__(self,
            name="history_example",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.set_history(history+1) # setting history to 1, means 0 history



    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        print "................................."
        print "output items size: ",noutput_items
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items
        print "input items size: ",ninput_items_required[0]
        # if(noutput_items <= 1):
        #     noutput_items = 0;
        #     ninput_items_required[0] = 0;


    def general_work(self, input_items, output_items):
        in0 = input_items[0];
        print "input: ",input_items[0]
        print "check: ",len(in0)," ",len(output_items[0])
        out = numpy.zeros(len(output_items[0]))

        # if(len(in0)==1):
        #     print "meow"
        #     output_items[0] = []
        #     self.consume_each(len(in0))
        #     return len(in0)

        # elif(len(in0==0)) :
        #     return 0
        # else:
        for idx in range(0,len(out)):
            if(idx+1 >= len(in0)):
                out[idx] = in0[idx]
            else:
                out[idx] = in0[idx] + in0[idx+1]


        print "output: ",out
        output_items[0][:] = out
        # consume(0, len(input_items[0]))
        print "consuming: ", len(output_items[0])
        self.consume_each(len(output_items[0])) # +1 for history
        return len(output_items[0])
