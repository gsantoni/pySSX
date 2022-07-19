# -*- coding: utf-8 -*-
#
#
#
#    Copyright (C) 2022 European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Gianluca Santoni (gianluca.santoni@esrf.fr)
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  .
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#  .
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

__authors__ = ["Gianluca Santoni"]
__license__ = "MIT"
__date__ = "19/07/2022"
__copyright__ = "2022, ESRF, Grenoble"
__contact__ = "gianluca.santoni@esrf.fr"

from asyncio.windows_events import NULL
import os
import json
import h5py

class Crystfel_launcher():
    def __init__(self, imgdir, prefix, **kwargs):
        self.datadir = imgdir
        self.imgname = prefix
        #need to add here crystfel path, to check with EGI how to better do it
        #also needs all crystfel inputs to define where the experiment was. Need a repo for geometry files and masks.
        
        self.index_method = kwargs.get('indexing_method', 'xgandalf')
        #peakfinding will be chagned to h5 once the peakfinder function is working
        self.peakfinding_method = kwargs.get('peakfinder', 'peakfinder8')
        self.peaks_radius = kwargs.get('peak_radius', '3,4,5')
        self.min_snr = kwargs.get('min_snr', '4.0')  # grid of 3, 4, 5
        self.threshold = kwargs.get('threshold', '10')  # grid of 5, 10, 20
        self.local_bg_radius = kwargs.get('local_bg_radius', '10')  # grid of 7, 10, 15, 20
        self.min_res = kwargs.get('min_res', '70')
        #MISSING: geometry and camera length and beam center: must be read from h5 metadata and not in the geometry file.

    def getHeaderInfo(self):
        return(NULL)

    def prepareLaunchCommand(self):
        launch_script = ('indexamajig'
                        ' -i files.lst' 
                        ' --peaks='+self.peakfinding_method+
                        ' --threshold='+ self.threshold+
                        ' --int-radius='+self.peaks_radius+
                        ' --indexing='+ self.index_method)
        print(launch_script)

def main():
    A = Crystfel_launcher("a", "b")
    A.prepareLaunchCommand()

if __name__== '__main__':
    main()