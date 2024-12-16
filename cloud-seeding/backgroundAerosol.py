import matplotlib.pyplot as plt
import numpy as np

# https://digitalcommons.chapman.edu/cgi/viewcontent.cgi?article=1339&context=scs_articles

dat=[0.05018928375492713, 0.0029739776951672736, 0.05616824249778104, 0.004460966542750966, 0.061691315697138024, 0.008921933085501876, 0.06904049073511313, 0.010408921933085458, 0.07726515972435936, 0.013382899628252787, 0.08646961867834096, 0.017843866171003753, 0.0967705882062704, 0.017843866171003753, 0.10431095917317436, 0.014869888475836424, 0.12120012144147815, 0.013382899628252787, 0.13563847304788731, 0.010408921933085458, 0.15179683940866254, 0.0074349442379182396, 0.17971423755954494, 0.005947955390334603, 0.2250827221443728, 0.005947955390334603, 0.26647834009971144, 0.005947955390334603, 0.3038703954531077, 0.0074349442379182396, 0.34006992693995547, 0.008921933085501876, 0.38778830257756397, 0.011895910780669205, 0.4339848228027595, 0.013382899628252787, 0.47665893609452425, 0.017843866171003753, 0.54354338650227, 0.022304832713754663, 0.6315494074157563, 0.02676579925650563, 0.6936502218805416, 0.029739776951672847, 0.805960292151645, 0.03717472118959103, 0.9541867931608273, 0.04907063197026024, 1.0285370944818935, 0.05947955390334575, 1.129674061003534, 0.07286245353159854, 1.264250091946579, 0.09070631970260229, 1.3885649269779694, 0.11152416356877326, 1.5251037502117932, 0.1368029739776952, 1.6133898021176223, 0.15167286245353162, 1.772035855117121, 0.16802973977695168, 1.9462817154906868, 0.17992565055762083, 2.1376613261603614, 0.18438661710037174, 2.304228045445928, 0.18289962825278816, 2.4837736550889264, 0.17249070631970265, 2.6773094711291554, 0.16505576208178446, 2.885925611422609, 0.14869888475836435, 3.052987674112459, 0.13828996282527883, 3.2297207181608516, 0.12639405204460968, 3.481380781263065, 0.11003717472118962, 3.7526502139942024, 0.09368029739776951, 3.969885711271743, 0.083271375464684, 4.199696657521706, 0.06988847583643121, 4.526937313315595, 0.05650557620817842, 4.972075082248464, 0.04312267657992569, 5.564389408316466, 0.03122676579925654, 6.345180660189953, 0.017843866171003753, 7.101070574229735, 0.011895910780669205, 8.097487858578704, 0.0074349442379182396, 9.76824852857884, 0.004460966542750966, 10.931922336467807, 0.0014869888475836368]



from scipy.optimize import curve_fit

# Define the nonlinear function
def lognormal_func(x, a,b,c,d,e,f,g,h,i):
    dNdlogD= \
            a/(np.sqrt(2.0*np.pi)*b)* \
            np.exp(-(np.log(x/c)**2.0)/(2*b**2))
    dNdlogD=dNdlogD+ \
            d/(np.sqrt(2.0*np.pi)*e)* \
            np.exp(-(np.log(x/f)**2.0)/(2*e**2))
    dNdlogD=dNdlogD+ \
            g/(np.sqrt(2.0*np.pi)*h)* \
            np.exp(-(np.log(x/i)**2.0)/(2*h**2))
    return dNdlogD



if __name__=="__main__":
    r=np.array(dat[::2])
    D=r*2
    dVdlnr=np.array(dat[1::2])
    dNdlnD=dVdlnr/(4./3.*np.pi*r**3)*1e12/1500/1e6 

    plt.ion()
    plt.plot(D,dNdlnD)


    d=np.logspace(-2,1,100)
    dm=[0.26,0.1, 2.5]
    lnsig=[0.2,0.6,0.3]
    N=[1000*0.6*np.sqrt(2.0*np.pi)*lnsig[0], 10*0.4*np.sqrt(2.0*np.pi)*lnsig[1], 10.]    

    popt, pcov = curve_fit(lognormal_func, D,dNdlnD, \
            p0=[N[0], lnsig[0], dm[0], N[1], lnsig[1],dm[1], N[2], lnsig[2],dm[2]], \
            bounds=([1.0, 0.1, 0.1, 1.0, 0.1,0.1, 1.0,0.1,2.5],\
            [1e9, 0.99,0.5 , 1e9, 0.99,9,1e2,0.4,3]), \
            method='trf') 

    dNdlogD=np.zeros(len(d))
    N=[popt[0],popt[3], popt[6]]
    lnsig=[popt[1],popt[4], popt[7]]
    dm=[popt[2],popt[5], popt[8]]
    for i in range(len(dm)):
        dNdlogD=dNdlogD+ \
                N[i]/(np.sqrt(2.0*np.pi)*lnsig[i])* \
                np.exp(-(np.log(d/dm[i])**2.0)/(2*lnsig[i]**2))
    ax=plt.subplot(111)
    plt.plot(d,dNdlogD)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('D ($\\mu$m)')
    plt.ylabel('$\\frac{dN}{d\\log D}$ (cm$^{-3}$)')
    plt.title('Farahat et al (2016)')

    plt.text(0.3,0.2, \
	'N=[' + str(round(N[0],2)) + ', ' + str(round(N[1],2)) + ', ' + str(round(N[2],2)) + ']\n' + \
	'$\ln\sigma$=[' + str(round(lnsig[0],2)) + ', ' + str(round(lnsig[1],2)) + ', ' + str(round(lnsig[2],2)) +']\n' + \
	'$D_m$=[' + str(round(dm[0],3)) + ', ' + str(round(dm[1],3)) + ', ' + str(round(dm[2],3)) +']', \
	transform=ax.transAxes)
    plt.savefig('images/background_aerosol.png')