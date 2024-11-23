import os
import tempfile
import numpy as np
#import itertools
from subprocess import check_output
import getpass
import createModelProfile

username=getpass.getuser()
outputDir='/tmp'
def batchRuns(radiosonde):
    
    num_runs=len(radiosonde)   
    
    inputFile=os.getcwd()+'/../../bin-microphysics-model/python/cloud_seeding/namelist.default'
    
    dumpFileObj=tempfile.NamedTemporaryFile(delete=False)
    dumpFile=dumpFileObj.name
    
    tmpFileObj=tempfile.NamedTemporaryFile(delete=False)
    tmpFile=tmpFileObj.name
    
    
    if not os.path.exists('/tmp/' + username):
        os.mkdir('/tmp/' + username)
    
    print(tmpFile)
    print(dumpFile)
    
    
    for nn in range(num_runs):
        
        (q_read,theta_read,rh_read,z_read,z_replace,\
                t_replace,p_replace,ps_replace,\
                ts_replace,n_level_replace)=createModelProfile.do_it(radiosonde[nn])

        n=str(nn)

        print('Run number '+ n.zfill(3))

      
        fileName=outputDir + '/' + username + '/output' + n.zfill(3) + '.nc'
        # change the output filename
        changeFile(inputFile,dumpFile,'/tmp/output1.nc',fileName)
        # zinit
        changeFile(dumpFile,tmpFile,'zinit=4863.61,',z_replace)
        # tinit
        changeFile(tmpFile,tmpFile,'tinit=274.869,',t_replace)
        # pinit
        changeFile(tmpFile,tmpFile,'pinit=57645.1,',p_replace)
        # n_levels_s
        changeFile(tmpFile,tmpFile,'n_levels_s = 102,',n_level_replace)
        # psurf
        changeFile(tmpFile,tmpFile,'psurf=72299.70728542529,',ps_replace)
        # tsurf
        changeFile(tmpFile,tmpFile,'tsurf=291.87352,',ts_replace)
        # q_read
        changeFile(tmpFile,tmpFile,'q_read(1,1:102) = 0.008542568137614734, 0.008585769317769295, 0.008670988248240996, 0.008666986513247217, 0.00868057012887731, 0.008684498956399651, 0.008669997995668317, 0.008650880384200237, 0.008588636129229683, 0.008558990710352902, 0.008493222642737991, 0.008274564142674159, 0.00801393627386423, 0.008060996304315983, 0.008111509440182645, 0.007789402583968996, 0.007700385507179348, 0.0077818274243349065, 0.006915608676072064, 0.006450998318672354, 0.006398929708043032, 0.006380854344480615, 0.00641912698106695, 0.006493566732658686, 0.006578048303391324, 0.006571109957937807, 0.006459481148307626, 0.006345674739461716, 0.006295137620999771, 0.006281195252276052, 0.006233371337883053, 0.006085136879424505, 0.005680576360223083, 0.0053088659253673854, 0.0051768811297831716, 0.005093175966237522, 0.005064758115646594, 0.005008367509191132, 0.004897828094258039, 0.004819042349987036, 0.004755224622056359, 0.00492805420219078, 0.005266419425372504, 0.005336784900351915, 0.005240883193000766, 0.005117438488236161, 0.00513173581027026, 0.005123903242088979, 0.0049133807844637025, 0.0046579707849810454, 0.004235257152887583, 0.004040917841479451, 0.003743370948346213, 0.0036150889350725973, 0.0035749305973826065, 0.0035311773345712287, 0.0034943018162004987, 0.00339409856623646, 0.0031430296208006395, 0.0031858981613447804, 0.003142137088674238, 0.0030504317081869784, 0.0029934958648315875, 0.002918277277335792, 0.0028816807201139947, 0.00287103208860784, 0.0028762445213998274, 0.002922058646806271, 0.0029111455957586837, 0.00281323793486062, 0.0028008148532570392, 0.002857966996720944, 0.002857266442843798, 0.0028243296082598015, 0.002794613244107666, 0.0025934979863203177, 0.0018746170355759353, 0.0012081966619634018, 0.0008386262237331591, 0.0007353628659683536, 0.0009260873395041507, 0.0008301410391847841, 0.0005341485506337189, 0.0005107260773265494, 0.0005103161552439593, 0.000507541455517322, 0.0003369209344795178, 0.00026962413280278146, 0.0003882160285195789, 0.00044668141838351917, 0.0003538696116858078, 0.0004788845688857333, 0.0008130887469106482, 0.000825320654246927, 0.0008533255221324388, 0.0008301601217342041, 0.0007604337462385953, 0.0006759856021196309, 0.0005780966772845898, 0.00044881556686319986, 0.00032643522297925396, 0.0002989077821312654,',q_read)
        # theta_read
        changeFile(tmpFile,tmpFile,'theta_read(1:102) = 320.46746903142343, 320.3700956282465, 320.3334573436535, 320.3528332133091, 320.36286689507034, 320.3452903001715, 320.3365578961664, 320.4372149826082, 320.82188109125025, 320.9526612064163, 321.2693285308234, 321.8654794651877, 322.0584459813949, 322.0120534591814, 322.0103744627633, 322.12963366680407, 322.122772741805, 322.1123264123236, 322.38176840194967, 322.5394379245299, 322.53559088136126, 322.57304323155915, 322.6638908809318, 322.70090070345736, 322.69795431065575, 322.72455677406816, 322.9543790134206, 323.18453490440805, 323.2135365964928, 323.2135356265836, 323.2523917238329, 323.3333762654103, 323.54549938094806, 323.73173224363575, 323.83112303086375, 323.89548960701103, 323.92155723871645, 323.97675469515866, 324.06668427119706, 324.15873230829646, 324.269868810768, 324.3051956091525, 324.2793398953218, 324.27853906448087, 324.31441973025915, 324.3428841177718, 324.36995771158473, 324.38751625055517, 324.44520704225795, 324.5573117303632, 324.77488936514027, 324.87922053576824, 325.111220728962, 325.275594789067, 325.33225190128894, 325.4245868766635, 325.6027106228785, 325.91002842011557, 326.34825937172957, 326.5786767341171, 326.7140604187538, 326.8509194980859, 326.95084768670904, 327.04548619973156, 327.1076690134641, 327.15974411649876, 327.1957533914478, 327.2227852628782, 327.3045773996407, 327.5085242900319, 327.7373838542524, 327.91294796910853, 327.97414297645685, 327.9962876517176, 327.9901793843194, 328.0462222970349, 328.7333156758117, 330.06339403546616, 330.96766911385413, 331.69428412190274, 332.1986581456704, 332.7516385970726, 333.37220707840345, 333.78318643312343, 334.00474585782854, 334.1537032187249, 334.42365618555925, 334.63864581081464, 334.78893609701475, 334.9669851699533, 335.295044215489, 335.7354415210285, 335.91691219643667, 335.96241787810817, 336.0871445249675, 336.4018821127998, 336.58462414566804, 336.64050869399057, 336.7473404158334, 336.9191629143819, 337.0724716649622, 337.18030784476053,',theta_read)
        # rh_read
        changeFile(tmpFile,tmpFile,'rh_read(1:102) = 0.44428661, 0.45942795000000003, 0.47949608, 0.4879252866666667, 0.50156867, 0.5160225066666667, 0.5279718800000001, 0.537906705, 0.5363620766666667, 0.5428360733333333, 0.5440848075, 0.5254245133333333, 0.5148413733333332, 0.5340503699999999, 0.5522624466666667, 0.5391955066666667, 0.5481165025, 0.5701671066666667, 0.5105202866666667, 0.4848207, 0.49487414, 0.50402298, 0.5190817649999999, 0.5389680866666666, 0.5595163733333334, 0.573901625, 0.570494845, 0.5684831966666667, 0.5785025533333333, 0.5952256666666667, 0.6044203066666668, 0.6048573025, 0.57465398, 0.5438246766666667, 0.54326597, 0.5489106466666667, 0.55904934, 0.5678248699999999, 0.56902438, 0.5714139433333333, 0.5776113774999999, 0.6154061533333334, 0.67639183, 0.7069220925, 0.7141133866666667, 0.7134253700000001, 0.7369629850000001, 0.7580506633333333, 0.7438423933333332, 0.721281035, 0.6696693400000001, 0.6492496233333334, 0.611665165, 0.6032332766666667, 0.60922615, 0.6208043, 0.6273480833333334, 0.6149439466666666, 0.5736726475, 0.5920592366666667, 0.5956353999999999, 0.590938905, 0.5955053333333333, 0.5941158066666666, 0.6018251324999999, 0.6169907533333333, 0.63427428, 0.6664641833333333, 0.6820864133333333, 0.67001053, 0.6805987950000001, 0.7111227166666667, 0.7272106666666667, 0.7409112, 0.7581208066666666, 0.7228465533333334, 0.5169987225, 0.31853232, 0.21449879999999996, 0.185547755, 0.23366702000000003, 0.20797652, 0.13324805666666667, 0.12844704333333332, 0.13023194, 0.132581785, 0.08944359366666665, 0.07294811866666667, 0.107669055, 0.12670523666666667, 0.10120815533333333, 0.13819555766666666, 0.24043021, 0.25081591333333336, 0.2664606475, 0.2631711766666667, 0.24556588333333335, 0.22414512666666667, 0.19663453666666666, 0.15628355666666666, 0.1167077525, 0.10949289499999999,',rh_read)
        # z_read
        changeFile(tmpFile,tmpFile,'z_read(1:102) = 2900.0, 2950.0, 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0, 3400.0, 3450.0, 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0, 3900.0, 3950.0, 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0, 4400.0, 4450.0, 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0, 5050.0, 5100.0, 5150.0, 5200.0, 5250.0, 5300.0, 5350.0, 5400.0, 5450.0, 5500.0, 5550.0, 5600.0, 5650.0, 5700.0, 5750.0, 5800.0, 5850.0, 5900.0, 5950.0, 6000.0, 6050.0, 6100.0, 6150.0, 6200.0, 6250.0, 6300.0, 6350.0, 6400.0, 6450.0, 6500.0, 6550.0, 6600.0, 6650.0, 6700.0, 6750.0, 6800.0, 6850.0, 6900.0, 6950.0, 7000.0, 7050.0, 7100.0, 7150.0, 7200.0, 7250.0, 7300.0, 7350.0, 7400.0, 7450.0, 7500.0, 7550.0, 7600.0, 7650.0, 7700.0, 7750.0, 7800.0, 7850.0, 7900.0, 7950.0/',z_read)

        # psd
        changeFile(tmpFile,tmpFile,\
                'n_aer1(1:4,1:1)        = 889.7e6, 15.47e6, 270.8e6, 0.e6, d_aer1(1:4,1:1)        = 0.103e-6  , 0.175e-6, 0.045e-6, 1e-7, sig_aer1(1:4,1:1)      = 0.39   , 0.1, 0.25, 0.25,  ',\
                'n_aer1(1:4,1:1)        = 150.02e6, 4421.32e6, 7.51e6, 0.e6, d_aer1(1:4,1:1)        = 0.292e-6  , 0.135e-6, 2.5e-6, 1e-7, sig_aer1(1:4,1:1)      = 0.72   , 0.33, 0.4, 0.25,  ')


        # psd of seed https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2020JD033771
        #changeFile(tmpFile,tmpFile,\
        #        'n_aer1(1:4,2:2)        = 0e6, 0e6, 0e6, 0.e6, d_aer1(1:4,2:2)        = 0.103e-6  , 0.175e-6, 0.045e-6, 1e-7, sig_aer1(1:4,2:2)      = 0.39   , 0.1, 0.25, 0.25,', \
        #        'n_aer1(1:4,2:2)        = 40000e6, 300e6, 0e6, 0.e6, d_aer1(1:4,2:2)        = 0.3e-6  , 1.0e-6, 0.045e-6, 1e-7, sig_aer1(1:4,2:2)      = 0.344   , 0.693, 0.25, 0.25,')


        changeFile(tmpFile,tmpFile,\
                'outputfile = \'' + '/tmp/' + username + '/output.nc\'',\
                'outputfile = \'' + outputDir + '/' + username + \
                 '/output' + n.zfill(3) + '.nc\'')


        # # string to run SCM
        # runStr='cd /Users/mccikpc2/Dropbox/programming/fortran/scm;'
        # runStr=runStr+'./main.exe ' + tmpFile + ' > ' + dumpFile
        
        # os.system(runStr)


        str1='./main.exe ' + tmpFile
        
        result = check_output(str1, shell=True,cwd='../../bin-microphysics-model/').decode()


    
    tmpFileObj.close()
    os.unlink(tmpFileObj.name)
    dumpFileObj.close()
    os.unlink(dumpFileObj.name)

"""
    0. function to change file
"""
def changeFile(inFile,outFile,inString,outString):
    fin = open(inFile,"rt")
    
    lines=[]
    for line in fin:
        lines.append(line)
        
    fin.close()


    fout = open(outFile,"wt")

    for line in lines:
        if isinstance(outString, list):
            line1=line
            for i in range(len(outString)):
                line1=line1.replace(inString[i],outString[i])
            fout.write(line1)
        else:
            fout.write(line.replace(inString,outString))
    

    fout.close()
    
if __name__=="__main__":
    import readSondeData
    # read the dataset
    (data1,dats,tlcl,plcl,cape,cin,pw,time)=readSondeData.do_it()
    # only choose files where cape >= 100
    inds,=np.where(cape >= 100)
    datsnew = [dats[i] for i in inds]

    # run parcel model for all cases
    batchRuns(datsnew)
    
