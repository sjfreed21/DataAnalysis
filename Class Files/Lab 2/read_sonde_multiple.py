#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:56:39 2020
read save sonde text file 
@author: zhwa2432
"""
import matplotlib.pyplot as plt

def read_sounding(url):
    pressure=[]
    altitude=[]
    temp    =[]
    lines  = urllib.request.urlopen(url).readlines()
    for line in lines[10:76]: # 100
        entries = line.decode("utf-8").split()
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
    return(pressure,altitude,temp)

if __name__ == '__main__':
    outdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 2/dat/'
    f=open(outdir + 'sonde_01.txt', 'r')
    lines = f.readlines()
    pressure=[]
    altitude=[]
    temp    =[]
    rh      =[]
    for line in lines[8:76]: # 100
        entries = line.split()
        #print(entries)
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
            rh.append(float(entries[4]))
    
    plt.plot(temp,altitude,'o--')
    plt.xlabel("temperature [C]")
    plt.ylabel("altitude [m]")
    print(len(lines))
    num=0
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
                print(' time:',time,day,num)
                num0=num
    #Check the lines below the            
    for line in lines[num0:num0+6]:
        print(line)
        
    pressure=[]
    altitude=[]
    temp    =[]
    rh      =[]
    for line in lines[num0+6:num0+74]: # 100
        entries = line.split()
        #print(entries)
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
            rh.append(float(entries[4]))
    
    plt.plot(temp,altitude,'o--')
    plt.xlabel("temperature [C]")
    plt.ylabel("altitude [m]")