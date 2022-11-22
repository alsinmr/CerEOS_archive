#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:38:34 2022

@author: albertsmith
"""

import numpy as np
import pyDR
import matplotlib.pyplot as plt

pyDR.Defaults['zrange'][1]=-2

files=['cera_CO.txt','cera_Hx1.txt','cera_Hx2.txt','cera_Hx3.txt']  #Data files
#Data has to be broken up by type of spin system
#CO: carbonyl with only a CSA, Hx1: 13C with one bonded 1H, Hx2: 2 bonded 1H, Hx3: 3 bonded 1H


proj=pyDR.Project('linoleic_proj',create=True)

for f in files:proj.append_data(f)

proj[0].detect.r_auto(4)  #Set up 4 detectors for carbonyl

#By default, we optimize detectors to maximize signal to noise (i.e. med_val/stdev)
#However, to obtain identical detectors for the 3 Hxn data sets, we need to
#assume these values are the same for the 3 sets. We do that here
#The consequence is that for Hx1 and Hx3, the detectors may be sub-optimal
#in terms of signal-to-noise (although only a small loss)
for d in proj[1:]:      
    d.sens.info['stdev']=proj[2].sens.info['stdev']      
    d.sens.info['med_val']=proj[2].sens.info['med_val']

proj[1:].detect.r_auto(5).inclS2()  #Set of 5+1 (inclS2) detectors for Hxn data sets

proj.fit()  #Fit all 4 data sets using the optimized detectors



#%% Create a single data object with all processed data for easier plotting
sub=proj['proc']

n=sum([d.R.shape[0] for d in sub])

src=pyDR.Data(sens=proj[3].sens)  #Object for source data
src.R=np.zeros([n,6])
src.Rstd=np.ones([n,6])*.001      #.001 will be a filler value for missing carbonyl data
src.S2=np.zeros(n)
src.S2std=np.ones(n)*0.1          #0.1 filler for CO
src.label=np.zeros(n,dtype='<U3')
src.title='Combined source data'

data=pyDR.Data(sens=proj[-1].sens,src_data=src)  #Object for processed data
data.R=np.zeros([n,6])
data.Rstd=np.ones([n,6])*.001    #0.001 filler for CO
data.Rc=np.zeros([n,6])
data.S2c=np.zeros(n)
data.title='Combined data'
data.label=np.zeros(n,dtype='<U3')

index=[[0],[6,5],[9,8,7,4,3,2,1],[10]]  #Sorting index for the for data sets

for d,i in zip(proj['proc'],index):  
    start=2 if d is proj['proc'][0] else 0
    
    data.R[i,start:]=d.R
    data.Rstd[i,start:]=d.Rstd
    data.Rc[i,start:]=d.Rc
    if d.S2c is not None:data.S2c[i]=d.S2c
    data.label[i]=d.label
    src.R[i,start:]=d.src_data.R
    src.Rstd[i,start:]=d.src_data.Rstd
    src.label[i]=d.label

proj.append_data(data)    #Add combined data to the project

#%% Plot results
proj['Combined data'].plot(style='bar',errorbars=True)
proj.plot_obj.ax_sens.plot(sub[0].sens.z,sub[0].sens.rhoz.T,linestyle=':',color='grey')
ylim=[1,.55,.55,.55,.004,.0005]
for a,yl in zip(proj.plot_obj.ax,ylim):a.set_ylim([0,yl])
proj.plot_obj.show_tc()

#%% Plot fit
proj['Combined data'].plot_fit()

#%% Compare Sensitivities
#This is just a check that all sensitivies are the same for the 3 Hxn data object
#We also see the deviation for the CO data set
ax=plt.figure().add_subplot(111)
clrs=plt.get_cmap('tab10')
for k,d in enumerate(proj['proc']):
    d.sens.plot_rhoz(ax=ax,color=clrs(k))
ax.set_title('Comparison of Sensitivities')


plt.show()  #Show all the figures
    