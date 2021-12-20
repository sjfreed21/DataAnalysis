import urllib
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.plots import SkewT
from metpy.units import units
from scipy import interpolate
import numpy as np
import matplotlib.cm as cm

#%% Section 1: Temperature and Dew Point
def read_sounding(url):
    pressure=[]
    altitude=[]
    temp    =[]
    tdew    =[]
    lines   =urllib.request.urlopen(url).readlines()
    for line in lines[10:76]: # 100
        entries = line.decode("utf-8").split()
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
            tdew.append(float(entries[3]))
    return(pressure,altitude,temp,tdew)

for i in [78807, 72403, 71909]:
    p,h,t,td = read_sounding('http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM=' + str(i))
    plt.figure(1)
    plt.plot(t,h,'o--', label=i)
    plt.xlabel("temperature [C]")
    plt.ylabel("altitude [m]")
    plt.legend()
    plt.figure(2)
    plt.plot(td,h,'o--', label=i)
    plt.xlabel("dew temperature [C]")
    plt.ylabel("altitude [m]")
    plt.legend()
    
    
#%% Section 2: Skew-T Data in 3 locations
for i in [78807, 72403, 71909]:
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)
    p,h,t,td = read_sounding('http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM=' + str(i))
    p = p * units.hPa
    t = t * units.degC
    td = td * units.degC

    prof = mpcalc.parcel_profile(p, t[0], td[0]).to('degC')

    skew.plot(p, t, 'r')
    skew.plot(p, td, 'g')
    skew.plot(p, prof, 'k')  # Plot parcel profile

    skew.ax.set_xlim(-60, 30)

    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    skew.shade_cape(p,t,prof)
    skew.shade_cin(p,t,prof)
    plt.title('Location: ' + str(i))
    plt.show()
    
#%% Section 3: Sounding Data in 2D

def read_mult_lines(lines, start, end):
    p, a, t, rh = [], [], [], []
    for l in lines[start + 6: end]:
        e = e = l.split()
        if len(e) == 11:
            p.append(float(e[0]))
            a.append(float(e[1]))
            t.append(float(e[2]))
            rh.append(float(e[4]))
    return(p, a, t, rh)

out = '/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 2/dat/'
T_2D = np.empty([149,365])
RH_2D = np.empty([149,365])
H_n = np.arange(100,15000,100)
mon = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = 0
for i in mon:
    f = open(out + 'sonde_' + i + '.txt', 'r')
    l = f.readlines()
    num = 0
    start, end = [], []
    for j in l:
        e = j.split()
        num += 1
        if 'at' in e:
            loc = e.index('at')
            if(e[loc+1][-1]) == 'Z':
                t = e[loc+1][0:2]
                d = e[loc+2][0:2]
                start.append(num)
    N_s = len(start)
    end = np.array(start.copy()) + 74
    for i in range(1, N_s-1):
        if end[i] > start[i+1]: end[i] = start[i+1]
            
    for i in range(N_s):
        p, a, t, rh = read_mult_lines(l, start[i], end[i])
        
        f = interpolate.interp1d(np.array(a), np.array(t), fill_value = "extrapolate")
        T_n = f(H_n)
        T_2D[:, days] = T_n
        
        f = interpolate.interp1d(np.array(a), np.array(rh), fill_value = "extrapolate")
        RH_n = f(H_n)
        RH_2D[:, days] = RH_n
        
        days += 1
        if days > 364: break
    if days > 364: break

x = np.arange(0, 365, 1)
y = H_n / 1000.0

T_2D[T_2D > 20] = 20
T_2D[T_2D < -80] = -80

RH_2D[RH_2D > 100] = 100
RH_2D[RH_2D < 0] = 0

fig, ax = plt.subplots()
img = ax.imshow(T_2D, extent=(x.min(), x.max(), y.min(), y.max()), interpolation='nearest',
                cmap = cm.gist_rainbow, aspect = 20, origin = 'lower')
ax.set_title("Temperature in 2D")
ax.set_xlabel("Sample Number")
ax.set_ylabel("Altitude (km)")
cbar = fig.colorbar(img, ax = ax, label = "Temperature (C)", spacing = 'proportional')

fig, ax = plt.subplots()
img = ax.imshow(RH_2D, extent=(x.min(), x.max(), y.min(), y.max()), interpolation='nearest',
                cmap = cm.gist_rainbow, aspect = 20, origin = 'lower')
ax.set_title("Relative Humidity in 2D")
ax.set_xlabel("Sample Number")
ax.set_ylabel("Altitude (km)")
cbar = fig.colorbar(img, ax = ax, label = "%RH", spacing = 'proportional')