import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
import os


# import pertinent variables from principal tab
from pyFiles.PRINCIPAL_TAB import title_text

# import pertinent variables from principal tab 2
from pyFiles.PrincipalTab_2 import processors_text, time_text,plotInt_text,show_initial, dif, fric, Dir, wave_maker,csp_text,CDsponge_text,LSW_text, RSW_text,BSW_text,TSW_text,R_sponge_text,A_sponge_text,input_verification

# import wavemaker variables from principal tab 2 (continued)
from pyFiles.PrincipalTab_2 import xc, yc, wid, amp, dep, LagTime, Xwavemaker, xc_wk, yc_wk, tPeriod, ampWK, depWK, thetaWK, TimeRamp, ywidth_wk, deltaWK, FreqPeak, FreqMin, FreqMax, HMO, GammaTMA, ThetaPeak, NFreq, NTheta 

# import pertinent variables from principal tab 3
from pyFiles.PrincipalTab_3 import DEPTH_OUT,U,V,ETA,Hmax,Hmin,MFmax,Umax,VORmax,Umean,Vmean,ETAmean,MASK,MASK9,SourceX, SourceY,P,Q,Fx,Fy,Gx,Gy,AGE,WaveHeight,steady_time,T_INTV_MEAN

 

def boolean_function(variable):    
# This function changes the checkbox variables True & False to T & F
# since that is the format of FUNWAVE's input file. 
    if show_initial.value == True:
        turn_on_IC = 'T'
    else:
        turn_on_IC = 'F'
        
    if dif.value == True:
        dif_text = 'T'
    else:
        dif_text = 'F'   
    
    if fric.value == True:
        fric_text = 'T'
    else:
        fric_text = 'F'
        
    if Dir.value == True:
        dir_text = 'T'
    else:
        dir_text = 'F'
        
    if DEPTH_OUT.value == True:
        depth_out = 'T'
    else:
        depth_out = 'F'    
        
    if U.value == True:
        u = 'T'
    else:
        u = 'F'
    
    if V.value == True:
        v = 'T'
    else:
        v = 'F' 
        
    if ETA.value == True:
        eta = 'T'
    else:
        eta = 'F' 
    
    if Hmax.value == True:
        hmax = 'T'
    else:
        hmax = 'F'
    
    if Hmin.value == True:
        hmin = 'T'
    else:
        hmin = 'F'
        
    if MFmax.value == True:
        mfmax = 'T'
    else:
        mfmax = 'F'    
        
    if Umax.value == True:
        umax = 'T'
    else:
        umax = 'F'
    
    if VORmax.value == True:
        vormax = 'T'
    else:
        vormax = 'F'
        
    if Umean.value == True:
        umean = 'T'
    else: 
        umean = 'F'
        
    if Vmean.value == True:
        vmean = 'T'
    else:
        vmean = 'F'
        
    if ETAmean.value == True:
        etamean = 'T'
    else:
        etamean = 'F'
        
    if MASK.value == True:
        mask = 'T'
    else:
        mask = 'F'
    
    if MASK9.value == True:
        mask9 = 'T'
    else:
        mask9 = 'F'
    
    if SourceX.value == True:
        sourcex = 'T'
    else:
        sourcex = 'F'
        
    if SourceY.value == True:
        sourcey = 'T'
    else:
        sourcey = 'F'    
    
    if P.value == True:
        p = 'T'
    else:
        p = 'F'
        
    if Q.value == True:
        q = 'T'
    else:
        q = 'F'  
        
    if Fx.value == True:
        fx = 'T'
    else:
        fx = 'F'
        
    if Fy.value == True:
        fy = 'T'
    else:
        fy = 'F'
        
    if Gx.value == True:
        gx = 'T'
    else:
        gx = 'F'
        
    if Gy.value == True:
        gy = 'T'
    else:
        gy = 'F'    
    
    if AGE.value == True:
        age = 'T'
    else:
        age = 'F'
    
    if WaveHeight.value == True:
        waveheight = 'T'
    else:
        waveheight = 'F'
    
    # this part changes "TMA-1D/IRR_WAVE" wavemaker option to TMA-1D (which is the one that FUNWAVE accepts) 
    if wave_maker.value == 'TMA_1D/IRR_WAVE':
        waveMaker = 'TMA_1D'
    else:
        waveMaker = wave_maker.value
    
    # call generate input.txt function:
    generate_input_file(turn_on_IC,dif_text,fric_text,dir_text,depth_out,
                       u,v,eta,hmax,hmin,mfmax,umax,vormax,umean,vmean,etamean,mask,
                       mask9,sourcex,sourcey,p,q,fx,fy,gx,gy,age,waveheight,steady_time,T_INTV_MEAN,waveMaker) 

def wave_param_generate_input(wave_maker_parameters):
# this function creates the wave maker parameter list that will be added to the input txt
    
    if wave_maker.value == 'INI_REC':
        
        parameter = """Xc = %4.2f
Yc = %4.2f
AMP = %4.2f
!WID = %4.2f""" % (xc.value,yc.value,amp.value,wid.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'JON_1D':
        
        parameter = """Xc_WK = %4.2f
Yc_WK = %4.2f
DEP_WK = %4.2f
Time_ramp = %4.2f
FreqPeak = %4.2f
FreqMin = %4.2f
FreqMax = %4.2f
Hmo = %4.2f
GammaTMA = %4.2f
Nfreq = %d
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value))
        wave_maker_parameters.value = parameter
    
    elif wave_maker.value == 'JON_2D':
        parameter = """Xc_WK = %4.2f
Yc_WK = %4.2f
DEP_WK = %4.2f
Time_ramp = %4.2f
!Delta_WK = %4.2f
FreqPeak = %4.2f
FreqMin = %4.2f
FreqMax = %4.2f
Hmo = %4.2f
GammaTMA = %4.2f
Nfreq = %d
Ntheta = %d
ThetaPeak = %4.2f
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value),int(NTheta.value),
               ThetaPeak.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'INI_GAUS':
        
        parameter = """AMP = %4.2f
Xc = %4.2f
Yc = %4.2f
!WID = %4.2f
        """ % (amp.value,xc.value,yc.value,wid.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'INI_SOL':
        
        parameter = """AMP = %4.2f
XWAVEMAKER = %4.2f
DEP = %4.2f
LAGTIME = %4.2f
        """ % (amp.value,Xwavemaker.value,float(dep.value)*-1,LagTime.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'WK_REG':
        
        parameter = """Xc_WK = %4.2f
Yc_WK = %4.2f
DEP_WK = %4.2f
AMP_WK = %4.2f
Tperiod = %4.2f
Time_ramp = %4.2f
Theta_WK = %4.2f
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,ampWK.value,tPeriod.value,TimeRamp.value,thetaWK.value)
        wave_maker_parameters.value = parameter        
    
    elif wave_maker.value == 'TMA_1D/IRR_WAVE':
        parameter = """Xc_WK = %4.2f
Yc_WK = %4.2f
DEP_WK = %4.2f
Time_ramp = %4.2f
FreqPeak = %4.2f
FreqMin = %4.2f
FreqMax = %4.2f
Hmo = %4.2f
GammaTMA = %4.2f
Nfreq = %d
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value))
        wave_maker_parameters.value = parameter
           
    else: 
        warning = "Select Wave Maker!!"
        raise Exception(warning)
    
    return(wave_maker_parameters.value)    
    
    
def generate_input_file(turn_on_IC,dif_text,fric_text,dir_text,depth_out,
                       u,v,eta,hmax,hmin,mfmax,umax,vormax,umean,vmean,etamean,mask,
                       mask9,sourcex,sourcey,p,q,fx,fy,gx,gy,age,waveheight,steady_time,T_INTV_MEAN,waveMaker):
# this function generates FUNWAVE's input.txt
        
        # Step 1 - take bathy points and dx data saved in data.txt 
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
        
        data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
        fin= open(data_text,'r')  
        val = fin.read()            
        val=val.split()
        points = val[2]
        dx = float(val[5])
        
        # Step 2 - create output folder and input file
        output_text=os.path.join(pwd,folder_name,'output','') # create output path 
        input_path = os.path.join(pwd,folder_name,'input.txt') # create path to save input.txt in project folder
        
        wave_maker_param = widgets.HTML(layout = widgets.Layout(width = "20%"))
        wave_maker_parameters = wave_param_generate_input(wave_maker_param) # call function that shows the wavemaker parameters
        
        fin = open(input_path,'w') # create input file
        
        inputFile ="""!INPUT FILE FOR FUNWAVE_TVD
! NOTE: all input parameter are capital sensitive
! --------------------TITLE-------------------------------------
! title only for log file
TITLE = %s 
! -------------------PARALLEL INFO-----------------------------
! 
!    PX,PY - processor numbers in X and Y
!    NOTE: make sure consistency with mpirun -np n (px*py)
!    
PX = %s
PY = 1
! --------------------DEPTH-------------------------------------
! Depth types, DEPTH_TYPE=DATA: from depth file
!              DEPTH_TYPE=FLAT: idealized flat, need depth_flat
!              DEPTH_TYPE=SLOPE: idealized slope, 
!                                 need slope,SLP starting point, Xslp
!                                 and depth_flat
DEPTH_TYPE = DATA
! Depth file
! depth format NOD: depth at node (M1xN1), ELE: depth at ele (MxN) 
! where (M1,N1)=(M+1,N+1)  
DEPTH_FILE = depth.txt
DepthFormat = ELE
! -------------------PRINT---------------------------------
! PRINT*,
! result folder
RESULT_FOLDER = %s
! ------------------DIMENSION-----------------------------
! global grid dimension
Mglob = %s
Nglob = 3
! ----------------- TIME----------------------------------
! time: total computational time/ plot time / screen interval 
! all in seconds
TOTAL_TIME = %4.2f
PLOT_INTV = %4.2f
PLOT_INTV_STATION = 0.5
SCREEN_INTV = 10.0
! -----------------GRID----------------------------------
! cartesian grid sizes
DX = %4.2f
DY = %4.2f
! --------------- INITIAL UVZ ---------------------------
! INI_UVZ - initial UVZ e.g., initial deformation
!         must provide three (3) files 
INI_UVZ = %s
! if true, input eta u and v file names
ETA_FILE = ini_z.txt
U_FILE = ini_u.txt
V_FILE = ini_v.txt
! ----------------WAVEMAKER------------------------------
!  wave maker 
! LEF_SOL- left boundary solitary, need AMP,DEP, LAGTIME 
! INI_SOL- initial solitary wave, WKN B solution,  
! need AMP, DEP, XWAVEMAKER  
! INI_REC - rectangular hump, need to specify Xc,Yc and WID 
! WK_REG - Wei and Kirby 1999 internal wave maker, Xc_WK,Tperiod 
!          AMP_WK,DEP_WK,Theta_WK, Time_ramp (factor of period) 
! WK_IRR - Wei and Kirby 1999 TMA spectrum wavemaker, Xc_WK, 
!          DEP_WK,Time_ramp, Delta_WK, FreqPeak, FreqMin,FreqMax, 
!          Hmo,GammaTMA,ThetaPeak 
! WK_TIME_SERIES - fft time series to get each wave component 
!                 and then use Wei and Kirby 1999  
!          need input WaveCompFile (including 3 columns: per,amp,pha) 
!          NumWaveComp,PeakPeriod,DEP_WK,Xc_WK,Ywidth_WK
WAVEMAKER = %s
!
%s
!
! ---------------- PERIODIC BOUNDARY CONDITION ---------
! South-North periodic boundary condition
!
PERIODIC = F
! ---------------- SPONGE LAYER ------------------------
! DHI type sponge layer
! need to specify widths of four boundaries and parameters
! set width=0.0 if no sponge
! R_sponge: decay rate
! A_sponge: maximum decay rate
! e.g., sharp: R=0.85
!       mild:  R=0.90, A=5.0
!       very mild, R=0.95, A=5.0
DIFFUSION_SPONGE = %s
FRICTION_SPONGE = %s
DIRECT_SPONGE = %s
Csp = %4.2f
CDsponge = %4.2f
Sponge_west_width =  %4.2f
Sponge_east_width =  %4.2f
Sponge_south_width = %4.2f
Sponge_north_width = %4.2f
R_sponge = %4.2f
A_sponge = %4.2f
! ----------------PHYSICS------------------------------
! parameters to control type of equations
! dispersion: all dispersive terms
! gamma1=1.0,gamma2=1.0: default: Fully nonlinear equations
!----------------Friction-----------------------------
Cd = 0.0
! ----------------NUMERICS----------------------------
! time scheme: runge_kutta for all types of equations
!              predictor-corrector for NSWE
! space scheme: second-order
!               fourth-order
! construction: HLLC
! cfl condition: CFL
! froude number cap: FroudeCap
! CFL
CFL = 0.5
! Froude Number Cap (to avoid jumping drop, set 1.5)
FroudeCap = 3.0
! --------------WET-DRY-------------------------------
! MinDepth for wetting-drying
MinDepth=0.01
!---------------breaking-----------------------------
!  there are two options for breaking algorithm 
!  1: shock-capturing breaking, need SWE_ETA_DEP
!  2: eddy-viscosity breaking, when VISCOSITY_BREAKING = T
!     the shock-capturing breaking is invalid
!     Cbrk1 and Cbrk2 are parameters defined in Kennedy et al 2000
!     suggested in this model Cbrk1=0.65, Cbrk2=0.15
!     WAVEMAKER_Cbrk is to avoid breaking inside wavemaker 
VISCOSITY_BREAKING = T
Cbrk1 = 0.65
Cbrk2 = 0.35
! ----------------- MIXING ---------------------------
! if use smagorinsky mixing, have to set -DMIXING in Makefile
! and set averaging time interval, T_INTV_mean, default: 20s
STEADY_TIME = %4.2f
T_INTV_mean = %4.2f
! -----------------OUTPUT-----------------------------
! stations 
! if NumberStations>0, need input i,j in STATION_FILE
NumberStations = 0
STATIONS_FILE = stations.txt
! output variables, T=.TRUE, F = .FALSE.
DEPTH_OUT = %s
U = %s
V = %s
ETA = %s
Hmax = %s
Hmin = %s
MFmax = %s
Umax = %s
VORmax = %s
Umean = %s
Vmean = %s
ETAmean = %s
MASK = %s
MASK9 = %s
SourceX = %s
SourceY = %s
P = %s
Q = %s
Fx = %s
Fy = %s
Gx = %s
Gy = %s
AGE = %s
WaveHeight = %s""" % (folder_name,int(processors_text.value),
                              str(output_text),points,time_text.value,plotInt_text.value,dx,dx,turn_on_IC,
                             waveMaker,wave_maker_parameters,dif_text, fric_text, dir_text,
                             csp_text.value,CDsponge_text.value,LSW_text.value,
                             RSW_text.value,BSW_text.value,TSW_text.value,
                             R_sponge_text.value,float(A_sponge_text.value),steady_time.value,T_INTV_MEAN.value, 
                              depth_out,u,v,eta,hmax,hmin,mfmax,umax,vormax,umean,vmean,
                              etamean,mask,mask9,sourcex,sourcey,p,q,fx,
                              fy,gx,gy,age,waveheight)
        fin.write(inputFile)
        fin.close()
        
        
def wave_param_show_input(variable):
# this function creates the wave maker parameter list that will be added to the input txt
    wave_maker_parameters = widgets.HTML(layout = widgets.Layout(width = "20%"))
    if wave_maker.value == 'INI_REC':
        
        parameter = """Xc = %4.2f</br>Yc = %4.2f</br>WID = %4.2f</br>
        """ % (xc.value,yc.value,wid.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'JON_1D':
        
        parameter = """Xc_WK = %4.2f</br>Yc_WK = %4.2f</br>DEP_WK = %4.2f</br>
        Time_ramp = %4.2f</br>FreqPeak = %4.2f</br>FreqMin = %4.2f</br>
        FreqMax = %4.2f</br>Hmo = %4.2f</br>GammaTMA = %4.2f</br>Nfreq = %4.2d</br>
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value))
        wave_maker_parameters.value = parameter
    
    elif wave_maker.value == 'JON_2D':
        parameter = """Xc_WK = %4.2f</br>Yc_WK = %4.2f</br>DEP_WK = %4.2f</br>
        Time_ramp = %4.2f</br>Delta_WK = %4.2f</br>FreqPeak = %4.2f</br>FreqMin = %4.2f</br>
        FreqMax = %4.2f</br>Hmo = %4.2f</br>GammaTMA = %4.2f</br>Nfreq = %4.2d</br> Ntheta = %4.2d</br>
        ThetaPeak = %4.2f</br>
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value),int(NTheta.value),
               ThetaPeak.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'INI_GAUS':
        
        parameter = """AMP = %4.2f</br>Xc = %4.2f</br>Yc = %4.2f</br>WID = %4.2f</br>
        """ % (amp.value,xc.value,yc.value,wid.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'INI_SOL':
        
        parameter = """AMP = %4.2f</br>XWAVEMAKER = %4.2f</br>DEP = %4.2f</br>LAGTIME = %4.2f</br>
        """ % (amp.value,Xwavemaker.value,float(dep.value)*-1,LagTime.value)
        wave_maker_parameters.value = parameter
        
    elif wave_maker.value == 'WK_REG':
        
        parameter = """Xc_WK = %4.2f</br>Yc_WK = %4.2f</br>DEP_WK = %4.2f</br>AMP_WK = %4.2f</br>Tperiod = %4.2f</br>
        Time_ramp = %4.2f</br>Theta_WK = %4.2f</br>
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,ampWK.value,tPeriod.value,TimeRamp.value,thetaWK.value)
        wave_maker_parameters.value = parameter        
    
    elif wave_maker.value == 'TMA_1D/IRR_WAVE':
        parameter = """Xc_WK = %4.2f</br>Yc_WK = %4.2f</br>DEP_WK = %4.2f</br>
        Time_ramp = %4.2f</br>Delta_WK = %4.2f</br>FreqPeak = %4.2f</br>FreqMin = %4.2f</br>
        FreqMax = %4.2f</br>Hmo = %4.2f</br>GammaTMA = %4.2f</br>Nfreq = %4.2d</br>
        """ % (xc_wk.value,yc_wk.value,float(depWK.value)*-1,TimeRamp.value,
               FreqPeak.value,FreqMin.value,FreqMax.value,HMO.value,GammaTMA.value,int(NFreq.value))
        wave_maker_parameters.value = parameter
           
    else: 
        warning = "Select Wave Maker!!"
        raise Exception(warning)
    
    return(wave_maker_parameters.value)        
 
    
def update_input_function(variable):
# this function updates the input txt preview that is shown in the gui
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    output_text=os.path.join(pwd,folder_name,'output','') # create output path 
    
### this function lets the user update the input.txt before generating the file

# Step 1: change the checkbox variables True & False to T & F
    if show_initial.value == True:
        turn_on_IC = 'T'
    else:
        turn_on_IC = 'F'
        
    if dif.value == True:
        dif_text = 'T'
    else:
        dif_text = 'F'   
    
    if fric.value == True:
        fric_text = 'T'
    else:
        fric_text = 'F'
        
    if Dir.value == True:
        dir_text = 'T'
    else:
        dir_text = 'F'
        
    if DEPTH_OUT.value == True:
        depth_out = 'T'
    else:
        depth_out = 'F'    
        
    if U.value == True:
        u = 'T'
    else:
        u = 'F'
    
    if V.value == True:
        v = 'T'
    else:
        v = 'F' 
        
    if ETA.value == True:
        eta = 'T'
    else:
        eta = 'F' 
    
    if Hmax.value == True:
        hmax = 'T'
    else:
        hmax = 'F'
    
    if Hmin.value == True:
        hmin = 'T'
    else:
        hmin = 'F'
        
    if MFmax.value == True:
        mfmax = 'T'
    else:
        mfmax = 'F'    
        
    if Umax.value == True:
        umax = 'T'
    else:
        umax = 'F'
    
    if VORmax.value == True:
        vormax = 'T'
    else:
        vormax = 'F'
        
    if Umean.value == True:
        umean = 'T'
    else: 
        umean = 'F'
        
    if Vmean.value == True:
        vmean = 'T'
    else:
        vmean = 'F'
        
    if ETAmean.value == True:
        etamean = 'T'
    else:
        etamean = 'F'
        
    if MASK.value == True:
        mask = 'T'
    else:
        mask = 'F'
    
    if MASK9.value == True:
        mask9 = 'T'
    else:
        mask9 = 'F'
    
    if SourceX.value == True:
        sourcex = 'T'
    else:
        sourcex = 'F'
        
    if SourceY.value == True:
        sourcey = 'T'
    else:
        sourcey = 'F'    
    
    if P.value == True:
        p = 'T'
    else:
        p = 'F'
        
    if Q.value == True:
        q = 'T'
    else:
        q = 'F'  
        
    if Fx.value == True:
        fx = 'T'
    else:
        fx = 'F'
        
    if Fy.value == True:
        fy = 'T'
    else:
        fy = 'F'
        
    if Gx.value == True:
        gx = 'T'
    else:
        gx = 'F'
        
    if Gy.value == True:
        gy = 'T'
    else:
        gy = 'F'    
    
    if AGE.value == True:
        age = 'T'
    else:
        age = 'F'
    
    if WaveHeight.value == True:
        waveheight = 'T'
    else:
        waveheight = 'F'
        
    # this part changes "TMA-1D/IRR_WAVE" wavemaker option to TMA-1D (which is the one that FUNWAVE accepts)
    if wave_maker.value == 'TMA_1D/IRR_WAVE':
        waveMaker = 'TMA_1D'
    else:
        waveMaker = wave_maker.value

#Step 2: upload data.txt to obtain point and dx values
    data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
    fin= open(data_text,'r')   
    val = fin.read()            
    val=val.split()
    points = val[2]
    dx = float(val[5])
    
#Step  3: update FUNWAVE's input.txt before generating it   

    wave_maker_parameters = wave_param_show_input(variable) # wavemaker parameter list that will be added to the input
    
    inputFile ="""!INPUT FILE FOR FUNWAVE_TVD </br>
! NOTE: all input parameter are capital sensitive </br>
! --------------------TITLE-------------------------------------</br>
! title only for log file</br>
TITLE = %s</br>
!</br>
! -------------------PARALLEL INFO-----------------------------</br>
! </br>
!    PX,PY - processor numbers in X and Y</br>
!    NOTE: make sure consistency with mpirun -np n (px*py)</br>
!    </br>
PX = %s</br>
PY = 1</br>
! --------------------DEPTH-------------------------------------</br>
! Depth types, DEPTH_TYPE=DATA: from depth file</br>
!              DEPTH_TYPE=FLAT: idealized flat, need depth_flat</br>
!              DEPTH_TYPE=SLOPE: idealized slope, </br>
!                                 need slope,SLP starting point, Xslp</br>
!                                 and depth_flat</br>
DEPTH_TYPE = DATA</br>
! Depth file</br>
! depth format NOD: depth at node (M1xN1), ELE: depth at ele (MxN) </br>
! where (M1,N1)=(M+1,N+1) </br> 
DEPTH_FILE = depth.txt</br>
DepthFormat = ELE</br>
!</br>
! -------------------PRINT---------------------------------</br>
! PRINT*,</br>
! result folder</br>
RESULT_FOLDER = %s</br>
! ------------------DIMENSION-----------------------------</br>
! global grid dimension</br>
Mglob = %s</br>
Nglob = 3</br>
! ----------------- TIME----------------------------------</br>
! time: total computational time/ plot time / screen interval </br>
! all in seconds</br>
TOTAL_TIME = %4.2f</br>
PLOT_INTV = %4.2f</br>
PLOT_INTV_STATION = 0.5</br>
SCREEN_INTV = 10.0</br>
! -----------------GRID----------------------------------</br>
! if use spherical grid, in decimal degrees</br>
! cartesian grid sizes</br>
DX = %4.2f</br>
DY = %4.2f</br>
! --------------- INITIAL UVZ ---------------------------</br>
! INI_UVZ - initial UVZ e.g., initial deformation</br>
!         must provide three (3) files </br>
INI_UVZ = %s</br>
! if true, input eta u and v file names</br>
ETA_FILE = ini_z.txt</br>
U_FILE = ini_u.txt</br>
V_FILE = ini_v.txt</br>
! ----------------WAVEMAKER------------------------------</br>
!  wave maker </br>
! LEF_SOL- left boundary solitary, need AMP,DEP, LAGTIME </br>
! INI_SOL- initial solitary wave, WKN B solution,  </br>
! need AMP, DEP, XWAVEMAKER  </br>
! INI_REC - rectangular hump, need to specify Xc,Yc and WID </br>
! WK_REG - Wei and Kirby 1999 internal wave maker, Xc_WK,Tperiod </br>
!          AMP_WK,DEP_WK,Theta_WK, Time_ramp (factor of period) </br>
! WK_IRR - Wei and Kirby 1999 TMA spectrum wavemaker, Xc_WK, </br>
!          DEP_WK,Time_ramp, Delta_WK, FreqPeak, FreqMin,FreqMax, </br>
!          Hmo,GammaTMA,ThetaPeak </br>
! WK_TIME_SERIES - fft time series to get each wave component </br>
!                 and then use Wei and Kirby 1999  </br>
!          need input WaveCompFile (including 3 columns: per,amp,pha) </br>
!          NumWaveComp,PeakPeriod,DEP_WK,Xc_WK,Ywidth_WK</br>
WAVEMAKER = %s</br>
!</br>
%s
!</br>
! ---------------- PERIODIC BOUNDARY CONDITION ---------</br>
! South-North periodic boundary condition</br>
!</br>
PERIODIC = F</br>
! ---------------- SPONGE LAYER ------------------------</br>
! DHI type sponge layer</br>
! need to specify widths of four boundaries and parameters</br>
! set width=0.0 if no sponge</br>
! R_sponge: decay rate</br>
! A_sponge: maximum decay rate</br>
! e.g., sharp: R=0.85</br>
!       mild:  R=0.90, A=5.0</br>
!       very mild, R=0.95, A=5.0</br>
DIFFUSION_SPONGE = %s</br>
FRICTION_SPONGE = %s</br>
DIRECT_SPONGE = %s</br>
Csp = %4.2f</br>
CDsponge = %4.2f</br>
Sponge_west_width =  %4.2f</br>
Sponge_east_width =  %4.2f</br>
Sponge_south_width = %4.2f</br>
Sponge_north_width = %4.2f</br>
R_sponge = %4.2f</br>
A_sponge = %4.2f</br>
! ----------------PHYSICS------------------------------</br>
! parameters to control type of equations</br>
! dispersion: all dispersive terms</br>
! gamma1=1.0,gamma2=1.0: Fully nonlinear equations</br>
!
! ----------------NUMERICS----------------------------</br>
! time scheme: runge_kutta for all types of equations</br>
!              predictor-corrector for NSWE</br>
! space scheme: second-order</br>
!               fourth-order</br>
! construction: HLLC</br>
! cfl condition: CFL</br>
! froude number cap: FroudeCap</br>
! CFL</br>
CFL = 0.5</br>
! Froude Number Cap (to avoid jumping drop, set 1.5)</br>
FroudeCap = 3.0</br>
! --------------WET-DRY-------------------------------</br>
! MinDepth for wetting-drying</br>
MinDepth=0.01</br>
! </br>
!---------------breaking-----------------------------</br>
!  there are two options for breaking algorithm </br>
!  1: shock-capturing breaking, need SWE_ETA_DEP</br>
!  2: eddy-viscosity breaking, when VISCOSITY_BREAKING = T</br>
!     the shock-capturing breaking is invalid</br>
!     Cbrk1 and Cbrk2 are parameters defined in Kennedy et al 2000</br>
!     suggested in this model Cbrk1=0.65, Cbrk2=0.15</br>
!     WAVEMAKER_Cbrk is to avoid breaking inside wavemaker </br>
VISCOSITY_BREAKING = T</br>
Cbrk1 = 0.65</br>
Cbrk2 = 0.35</br>
! ----------------- MIXING ---------------------------</br>
! if use smagorinsky mixing, have to set -DMIXING in Makefile</br>
! and set averaging time interval, T_INTV_mean, default: 20s</br>
STEADY_TIME = %4.2f</br>
T_INTV_mean = %4.2f</br>
! -----------------OUTPUT-----------------------------</br>
! stations </br>
! if NumberStations>0, need input i,j in STATION_FILE</br>
NumberStations = 0</br>
STATIONS_FILE = stations.txt</br>
! output variables, T=.TRUE, F = .FALSE.</br>
DEPTH_OUT = %s</br>
U = %s</br>
V = %s</br>
ETA = %s</br>
Hmax = %s</br>
Hmin = %s</br>
MFmax = %s</br>
Umax = %s</br>
VORmax = %s</br>
Umean = %s</br>
Vmean = %s</br>
ETAmean = %s</br>
MASK = %s</br>
MASK9 = %s</br>
SourceX = %s</br>
SourceY = %s</br>
P = %s</br>
Q = %s</br>
Fx = %s</br>
Fy = %s</br>
Gx = %s</br>
Gy = %s</br>
AGE = %s</br>
WaveHeight = %s""" % (folder_name,int(processors_text.value),
                              str(output_text),points,time_text.value,plotInt_text.value,dx,dx,turn_on_IC,
                              waveMaker,wave_maker_parameters,dif_text, fric_text, dir_text,
                             csp_text.value,CDsponge_text.value,LSW_text.value,
                             RSW_text.value,BSW_text.value,TSW_text.value,
                             R_sponge_text.value,float(A_sponge_text.value),steady_time.value,T_INTV_MEAN.value, 
                              depth_out,u,v,eta,hmax,hmin,mfmax,umax,vormax,umean,vmean,
                              etamean,mask,mask9,sourcex,sourcey,p,q,fx,
                              fy,gx,gy,age,waveheight)

    input_verification.value = inputFile

    
    
###--------------------------------------------       
# activate functions

from pyFiles.PrincipalTab_2 import update_input_button,inputFile_button
# ^ import pertinent variables of PrincipalTab_2

update_input_button.on_click(update_input_function)  # activate update input values button
inputFile_button.on_click(boolean_function)        # activate generate input file button
