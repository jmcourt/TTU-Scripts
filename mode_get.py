#! /usr/bin/env python

# A script to extract the datamode, start time and end time of all .FITS files in a folder and save
# this data to a .txt file.

import sys
import os
from astropy.io import fits
from math import log
from numpy import array
import pan_lib as pan

read=0
outname=pan.uniqfname('modes','txt')
tmpname=pan.uniqfname('temp','txt')
info = open(outname, 'w')
files=sorted(os.listdir(os.getcwd()))

#-----Creating Header--------------------------------------------------------------------------------------------------

info.write('{0:26} {1:22} {2:12} {3:12} {4:6} \n \n'.format('File','Datamode','Start','End','Length'))

#-----Extracting Data--------------------------------------------------------------------------------------------------

files=array(files)
for filename in files[files!=tmpname]:
   try:
      cfile=fits.open(filename)[1].header
      read+=1
      try:
         dmode=cfile['DATAMODE']
      except:
         dmode=None
      try:
         stime=float(cfile['TSTART'])
         etime=float(cfile['TSTOP'])
         dtime=etime-stime
      except:
         stime=None
         etime=None
         dtime=None
      info.write('{0:26} {1:22} {2:12} {3:12} {4:6} \n'.format(filename,dmode,str(stime),str(etime),str(dtime)))
   except:
      None
info.close()

if read==0:
   print('No FITS files found!')
   os.remove(outname)
else:
   print('Information saved as '+outname+'!')
exit()


