LDK: A seismic array detection algorithm
===============================================
</p>

<p align="center">
<b><a href="#overview">Overview</a></b>
|
<b><a href="#set-up">Set-Up</a></b>
|
<b><a href="#tutorial">Tutorial</a></b>
|
<b><a href="#credits">Credits</a></b>
|
<b><a href="#license">License</a></b>
</p>

![ScreenShot](https://github.com/quapity/stalta_neighbors/raw/master/STALTA_neighbors-03.png)


Overview
-----

Amplitude picker where coherence matters only from neighbors in the node graph.  


Set-Up
------------

### Notes
* tested on Python 2.7
* recommend to run in seperate env if other seimic processing relies on older obspy (<0.9.x)
    With Conda you can use environments with diff packages,versions etc.
    Docs on managing environments here: http://conda.pydata.org/docs/using/envs.html 

### Dependencies
* Relies on Numpy,Scipy,Pandas,and Geopy. Most can be installed with pip or ship with Anaconda
    - http://pandas.pydata.org
    - http://scipy.org
    - https://github.com/geopy/geopy
* Requires Obspy for seismic routines and data fetch 
    - https://github.com/obspy/obspy/wiki
* ANF catalog import stolen from old version of detex, a python code for subspace detection. Check it out at:
    - https://github.com/dchambers/detex.git 
    - or to install the latest: git+git://github.com/d-chambers/detex


Quick Feature Summary
-----
* Uses coherent energy in broadband, low amplitude ranges to identify seismic events across an array
* Input is local seismic data OR date range and station list for  obspy fetched waveform data
* Output is a picktable (as a dataframe), and templates for each detection -organized in day directories
* Current support for ANF catalog 


Tutorial
----------

### General Usage

* LDK.detection_function.detect('YYYY','MM','DD','HH','MM','SS',duration=7200,ndays=1,wb=1)
    - The first 6 args are start date/time. These pipe to obspy UTCDatetime
    - duration: number of seconds (2 hours is the smallest allowable increment)
    - ndays:    number of days to process from start date/time
    - wb:       the station list to use. Referenced from lists in the last half of Util.py

### Basic Tutorial

Credits
------------


License
-------------

