#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:56:39 2020
read save sonde text file 
@author: zhwa2432
"""
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import matplotlib.cm as cm
import matplotlib as mpl

def read_sounding_multiple(lines,S_line,E_line):
    pressure=[]
    altitude=[]
    temp    =[]
    rh      =[]
    #print(I_line)
    for line in lines[S_line+6:E_line]: # 100
        #print(line)
        entries = entries = line.split()
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
            rh.append(float(entries[4]))
    return(pressure,altitude,temp,rh)

if __name__ == '__main__':
    outdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 2/dat/'
    T_2d = np.empty([149,365])
    RH_2d = np.empty([149,365])
    H_new=np.arange(100,15000,100)
    mon=['01','02','03','04','05','06','07','08','09','10','11','12']
    idays=0
    for imon in range(12):
        #f=open(outdir + 'sonde_'+mon[imon]+'_2.txt', 'r')
        f=open(outdir + 'sonde_'+mon[imon]+'.txt', 'r')
        lines = f.readlines()
        num=0
        start_line=[]
        end_line=[]
    # find time  and location of different radiosonde
        for line in lines: #[0:4]: # 100
            entries = line.split()
            num=num+1
            #print(entries)
            if 'at' in entries:
                id=entries.index('at')
                if (entries[id+1][-1]) == 'Z':
                    time=entries[id+1][0:2]
                    day=entries[id+2][0:2]
                    print(' time:',time, entries[id+3], day,num)
                    num0=num
                    start_line.append(num)
        N_sonde=len(start_line)
        end_line = np.array(start_line.copy())  + 74
        for i in range(1,N_sonde-1):
            if end_line[i] >  start_line[i+1]:
                end_line[i]=start_line[i+1]
          
         
    #Get each sonde ddata by using start_line           
        #for I_line in start_line:
        for I in range(N_sonde):
            print('imon:',imon,idays,start_line[I])
            p,h,t,rh   = read_sounding_multiple(lines,start_line[I],end_line[I])
            # interpolate data to H_new and build your 2-D array here
            f = interpolate.interp1d(np.array(h), np.array(t), fill_value = "extrapolate")
            T_new = f(H_new)
            T_2d[:,idays] = T_new
            f = interpolate.interp1d(np.array(h), np.array(rh), fill_value = "extrapolate")
            RH_new = f(H_new)
            RH_2d[:,idays] = RH_new
            idays=idays+1
            if idays >364: break
        if idays >364: break
        
    print(idays) 
    x=np.arange(0,365,1)
    y=H_new/1000.

    
    #plot your 2-D here
    fig, ax = plt.subplots()

    img=ax.imshow(T_2d,extent=(x.min(), x.max(), y.min(), y.max()),
            interpolation='nearest', cmap=cm.gist_rainbow,aspect=20,origin ='lower')
    ax.set_title("Temperature in 2D")
    ax.set_xlabel('Sample Number',size=10)
    ax.set_ylabel('Altitude (km)',size=10)
    cbar=fig.colorbar(img, ax=ax,label='Temperature',spacing='proportional')

    fig, ax = plt.subplots()
    
    img=ax.imshow(RH_2d,extent=(x.min(), x.max(), y.min(), y.max()),
            interpolation='nearest', cmap=cm.gist_rainbow,aspect=20,origin ='lower')
    ax.set_title("Relative Humidity in 2D")
    ax.set_xlabel('Sample Number',size=20)
    ax.set_ylabel('Altitude (km)',size=20)
    cbar=fig.colorbar(img, ax=ax,label='RH',spacing='proportional')

    
    