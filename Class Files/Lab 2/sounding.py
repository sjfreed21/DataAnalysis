# read sounding
import urllib
import matplotlib.pyplot as plt

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

def location(url):
    lines  = urllib.request.urlopen(url).readlines()
    lon=lines[81] # longitude 132
    lat=lines[80] # latitude  131
    lon=float(lon.decode("utf-8").split(":")[1])
    lat=float(lat.decode("utf-8").split(":")[1])
    return(lat,lon)   

if __name__ == '__main__':
    # url     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=np&TYPE=TEXT%3ALIST&YEAR=2018&MONTH=09&FROM=0800&TO=0800&STNM=01004'
    url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=np&'\
        +'TYPE=TEXT%3ALIST&YEAR=2019&MONTH=02&FROM=0100&TO=2812&STNM=78016'    
    # lat,lon = location(url)
    p,h,t,td   = read_sounding(url)
    plt.figure(1)
    plt.plot(t,h,'o--')
    plt.xlabel("temperature [C]")
    plt.ylabel("altitude [m]")
    
    # stnm = ['78807','72403','71909'] # 
    # for i in stnm:
    #     url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM='+i
    #     p,h,t,td   = read_sounding(url)
    #     plt.figure(1)
    #     plt.plot(t,h,'o--', label=i)
    #     plt.xlabel("temperature [C]")
    #     plt.ylabel("altitude [m]")
    #     plt.legend()
    #     plt.figure(2)
    #     plt.plot(td,h,'o--', label=i)
    #     plt.xlabel("dew temperature [C]")
    #     plt.ylabel("altitude [m]")
    #     plt.legend()
 
#   re-grid temperature profile vertically
    import numpy as np
    from scipy import interpolate
    H_new=np.arange(100,20000,100)
    f = interpolate.interp1d(np.array(h), np.array(t),fill_value="extrapolate")
    T_new=f(H_new)
    plt.plot(T_new, H_new,'*r')

    
    '''
    Skew_ T plot with download sounding data
    Changing units to the required  is critical.
    '''   
    '''
    import metpy.calc as mpcalc
    from metpy.plots import SkewT
    from metpy.units import units
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)

    t=t* units.degC
    td=td* units.degC
    p=p* units.hPa
    

    # Calculate parcel profile
    prof = mpcalc.parcel_profile(p, t[0], td[0]).to('degC')
    #u = np.linspace(-10, 10, len(p)) * units.knots
    #v = np.linspace(-20, 20, len(p)) * units.knots

    skew.plot(p, t, 'r')
    skew.plot(p, td, 'g')
    skew.plot(p, prof, 'k')  # Plot parcel profile
    #skew.plot_barbs(p[::2], u[::2], v[::2])

    skew.ax.set_xlim(-50, 35)
    skew.ax.set_ylim(1000, 100)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    skew.shade_cape(p, t,prof)
    skew.shade_cin(p, t,prof)
    plt.show()   
    #plt.title('lat='+str(lat)+' lon='+str(lon))
    '''
    
    '''
    # save data to the local disk
    outdir='/Users/zhwa2432/Documents/CUB/ATOC4815_programing/dat/'

    mon=['01','02','03','04','05','06','07','08','09','10','11','12']
    days=['31','28','31','30','31','30','31','31','30','31','30','31']
    for i in range(12):
        print(i)
        url     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=np&'\
        +'TYPE=TEXT%3ALIST&YEAR=2019&MONTH='+mon[i]+'&FROM=0100&TO='+days[i]+'12&STNM=78016'   #=01004'  
        urllib.request.urlretrieve(url, outdir + 'Sonde_'+mon[i]+'_2.txt')
        '''
    '''  
    url     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=np&'\
        +'TYPE=TEXT%3ALIST&YEAR=2019&MONTH=05&FROM=0100&TO=3100&STNM=01004'    

    urllib.request.urlretrieve(url, outdir + 'Sonde_02.txt')
    '''    
