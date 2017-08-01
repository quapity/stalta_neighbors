# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:29:21 2017

@author: linville
"""
tt = UTCDateTime(2010,2,10)
tt2 = UTCDateTime(2010,2,11)
tr = client.get_waveforms(station=station[0],network='TA',channel='BHZ',location='*',starttime=tt,endtime=tt2)
st = tr.copy()
st.filter('bandpass', freqmin=1, freqmax=10)
trig = coincidence_trigger("recstalta", 3.5, 1, st, 5, sta=0.5, lta=10)

for i in range(1,len(station)):
    tr.append(client.get_waveforms(station=station[i],network='TA',channel='BHZ',location='*',starttime=tt,endtime=tt2)[0])


for i in range(len(trig)):
    det = trig[i]['stations']
    a,b,=[],[]
    for each in det:
        ix =np.where(np.array(station) == each)[0][0]
        a.append(closest_node(nodes[ix],nodes,2)[1])
        b.append(ix)
    c.append(len(np.intersect1d(a,b)))
times=[]
for i in np.where(np.array(c) >=3)[0]:
    times.append(trig[i]['time'])