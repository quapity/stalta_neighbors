Amplitude picker, where coherence matters only from neighbors in the node graph
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
</p>

![ScreenShot](https://github.com/quapity/stalta_neighbors/raw/master/STALTA_neighbors-03.png)


Overview
-----

Pick spikes from a time-series, but make sure a temporally coincident amplitude excursion is seen on X number of nearby sensors, otherwise... consider it noise. This lets us associate temporally coincident picks on individual sensors into triggers without an explicit path model, with the hope of keeping the number of false positives from noisy signals to a minimum.  


Set-Up
------------

### Dependencies

* Requires Obspy for seismic routines and data fetch 
    - https://github.com/obspy/obspy/wiki


Tutorial
----------

### General Usage

* LDK.detection_function.detect('YYYY','MM','DD','HH','MM','SS',duration=7200,ndays=1,wb=1)
    - The first 6 args are start date/time. These pipe to obspy UTCDatetime
    - duration: number of seconds (2 hours is the smallest allowable increment)
    - ndays:    number of days to process from start date/time
    - wb:       the station list to use. Referenced from lists in the last half of Util.py
    
* Output: trigger list:

### Things You Might Want To Tweak

* Which picker, and then Tune the picker parameters
* Sensor Array metadata- right now we nab it from obspy trace headers
* Output is a picktable (as a dataframe), and templates for each detection -organized in day directories
* Current support for ANF catalog 


Credits
------------




