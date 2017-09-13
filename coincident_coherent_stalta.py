# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:29:21 2017
@author: linville
"""
#%% function block
def closest_node(node,nodes,n):
    if len(nodes) == 1:
        return np.array([0])
    else:
        nodes = np.asarray(nodes)
        dist_2 = np.sum((nodes-node)**2,axis=1)
        return np.argsort(dist_2,axis=0)[:n]
        
def node_dist(node1,node2):
    return pydist.vincenty(node1,node2).meters/1000.0"""

#%% data block
###nodes are your latitude longitude pairs for each station
nodes = [] #lat/lon pairs for each station
stations = [] #station identifier
tr =[] #this is an obspy stream, loaded with your trace data for all stations for some time period

#%% trigger block
#Once you have a bunch of traces in a stream, you can make detections using obspy's sta/lta implementation
#### The parameters in line 34 matter!!!!!! Optimize them for your data.
st = tr.copy()
st.filter('bandpass', freqmin=1, freqmax=10)
trig = coincidence_trigger("recstalta", 3.5, 1, st, 5, sta=0.5, lta=10)

#%% filter block
#This is the only value I'm adding- It just says, don't return me EVERY detection the trigger routine gives me back.
#only give me detections (associated into triggers) that happen on X number of adjacent stations. If your data is seismic,
#and your array is very small (nodal guys), make numsta very big. By very big, I mean a number nearly equivalent to your station count.

numsta = 3
for i in range(len(trig)):
    det = trig[i]['stations']
    a,b,=[],[]
    for each in det:
        ix =np.where(np.array(station) == each)[0][0]
        a.append(closest_node(nodes[ix],nodes,2)[1])
        b.append(ix)
    c.append(len(np.intersect1d(a,b)))
times=[]
for i in np.where(np.array(c) >=numsta)[0]:
    times.append(trig[i]['time'])
