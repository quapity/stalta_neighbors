Amplitude picker, where coherence matters only from neighbors in the node graph
===============================================
</p>

<p align="center">
<b><a href="#overview">Overview</a></b>
|
<b><a href="#set-up">Set-Up</a></b>
|
<b><a href="#credits">Credits</a></b>
</p>

![ScreenShot](https://github.com/quapity/stalta_neighbors/raw/master/STALTA_neighbors-03.png)


Overview
-----

Pick spikes from a time-series, but make sure a temporally coincident amplitude excursion is seen on X number of nearby sensors, otherwise... consider it noise. This lets us associate temporally coincident picks on individual sensors into triggers without an explicit path model, with the hope of keeping the number of false positives from noisy signals to a minimum.  


Dependencies
------------

### Dependencies

* Requires Obspy for STA/LTA implementation 
    - https://github.com/obspy/obspy/wiki
* Requires geopy for geo dist, install with pip or conda

### Things You Might Want To Tweak

* Which picker, and then Tune the picker parameters
* Sensor Array metadata- I nab it from obspy trace headers
* Output is a trigger dict


Credits
------------
To Obspy, as always.



