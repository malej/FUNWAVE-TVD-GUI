import ipywidgets as widgets
from IPython.display import display, clear_output
import os
import shutil
import numpy as np

##### This py file contains all the functions that show/hide
##### some widgets on the GUI

## Show GUI function
# this function shows the entire GUI once the "generate project" button is pressed
# this function works with the generate bathy widgets on PRINCIPAL_TAB
# import pertinent variables from principal tab
from pyFiles.PRINCIPAL_TAB import GUI_CONT, title_text,space_box2,container_title
def project_clicked(variable):
    clear_output(wait=True)
    display(space_box2,container_title)
    
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    if folder_name == '': # verify that the user gave a project folder name
        pass
        warning = "Please specify the Project Title."
        raise Exception(warning)
    else:        
        # else, create project folder        
        project_text = os.path.join(pwd,folder_name) # create project folder path 
        output_plot_folder = os.path.join(pwd,folder_name,'output_plots') # create path to output plots (inside project folder)
        
        check_dir = os.path.exists(project_text) # check if project folder exist

        if check_dir == True:         # if project folder exist, print warning
            pass
            warning = "Project title '%s' already exists, please use a different title." %(s)
            raise Exception(warning)
            
        else:                         # else, create project folder
            os.mkdir(project_text)
            os.mkdir(output_plot_folder)
            # Step 2 - Show GUI
            clear_output(wait=True)
            display(GUI_CONT)
            
## generate bathy widgets function
# this function works with the generate bathy widgets on PrincipalTab_1
from pyFiles.PrincipalTab_1 import Box_upload,Box_SlopeBathy,Box_FlatBathy,MWL,space_box
def toggle_choose_bathy(change):
    if change['new'] == 'Upload File':
        #show
        Box_upload.layout.display=''
        #hide
        Box_SlopeBathy.layout.display='none'
        Box_FlatBathy.layout.display='none'       
        
    elif change['new'] == 'Slope':
        #show
        Box_SlopeBathy.layout.display=''
        MWL.layout.width = '100%'
        #hide
        Box_upload.layout.display='none'
        Box_FlatBathy.layout.display='none'
        
    elif change['new'] == 'Flat':
        #show
        Box_FlatBathy.layout.display=''
        MWL.description='Depth'
        MWL.layout.width = '50%'
        space_box.layout.height = '15px'
        #hide
        Box_upload.layout.display='none' 
        Box_SlopeBathy.layout.display='none'
        
    else: 
        Box_upload.layout.display='none'
        Box_SlopeBathy.layout.display='none'
        Box_FlatBathy.layout.display='none'

## generate initial condition widgets function
# this function works with the widgets on PrincipalTab_2b
from pyFiles.PrincipalTab_2 import init
def toggle_initial(change):
    if change['new']:
        #show
        init.layout.display=''
    else:
        # hide
        init.layout.display='none'

# This function generates new initial conditions files by changing the uploaded
# files to FUNWAVE's format
# this function works with the widgets on PrincipalTab_2b
from pyFiles.PrincipalTab_2 import iniElev_text,Uvel_text,Vvel_text
def update_initial_conditions(variable):
    
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

    filenameZ = iniElev_text.value
    file_pathZ = os.path.join(pwd,folder_name,filenameZ) 

    filenameU = Uvel_text.value
    file_pathU= os.path.join(pwd,folder_name,filenameU) 

    filenameV = Vvel_text.value
    file_pathV = os.path.join(pwd,folder_name,filenameU) 

    if filenameZ == '':
        pass
    else:

        IniZ = np.loadtxt(file_pathZ)
        M = 3 # number of rows (need three rows for Funwave to run a 1D case (really a 2D case))
        N = IniZ.shape[0] # number of points (columns)

        IniZ_FunwaveFormat = np.zeros([M,N])

        for i in range(M):
            IniZ_FunwaveFormat[i,:] = IniZ[:]

        ZFF_path = os.path.join(pwd,folder_name,'ini_z.txt') # path to FUNWAVE format ini_z file
        np.savetxt(ZFF_path,IniZ_FunwaveFormat)

    if filenameU == '':
        pass
    else:
        IniU = np.loadtxt(file_pathU)
        M = 3 # number of rows (need three rows for Funwave to run a 1D case (really a 2D case))
        N = IniU.shape[0] # number of points (columns)

        IniU_FunwaveFormat = np.zeros([M,N])

        for i in range(M):
            IniU_FunwaveFormat[i,:] = IniU[:]

        UFF_path = os.path.join(pwd,folder_name,'ini_u.txt') # path to FUNWAVE format ini_u file
        np.savetxt(UFF_path,IniU_FunwaveFormat)

    if filenameV == '':
        IniV = np.loadtxt(file_pathU) # must have the same ammount of pinnts as IniU
        M = 3 # number of rows (need three rows for Funwave to run a 1D case (really a 2D case))
        N = IniV.shape[0] # number of points (columns)

        IniV_FunwaveFormat = np.zeros([M,N])

        VFF_path = os.path.join(pwd,folder_name,'ini_v.txt') # path to FUNWAVE format ini_v file
        np.savetxt(VFF_path,IniV_FunwaveFormat)      # V velocities = 0 in 1D cases               

## generate WAVEMAKER variables widgets function
# this function works with the widgets on PrincipalTab_2c
from pyFiles.PrincipalTab_1 import THL
from pyFiles.PrincipalTab_2 import container_IniRec,container_Gauss,container_IniSol,container_WkReg
from pyFiles.PrincipalTab_2 import container_JON1D,container_JON2D,container_WKIRR,container_TMA_1D, GammaTMA
from pyFiles.PrincipalTab_2 import xc, xc_wk, dep, depWK, Xwavemaker # import Xoordinates and depth of Wavemaker 

                                
def toggle_waveMaker(change):
    if change['new'] == 'INI_REC':
        #show
        container_IniRec.layout.display=''
        #hide
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
        
        # reset xcoordinate of wavemaker 
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc.value = 5 
        xc.max = THL.value - 5
        
    elif change['new'] == 'INI_GAUS':
        #show
        container_Gauss.layout.display=''
        #hide
        container_IniRec.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
        
        # reset xcoordinate of wavemaker 
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc.value = 5 
        xc.max = THL.value - 5
        
        
    elif change['new'] == 'INI_SOL':
        #show
        container_IniSol.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
        
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        Xwavemaker.value = 5  
        Xwavemaker.max = THL.value - 5
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(Xwavemaker.value/dx) # index = Xcoordinate/dx
            dep.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
        
    elif change['new'] == 'WK_REG':
        #show
        container_WkReg.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
    
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc_wk.value = 5 
        xc_wk.max = THL.value - 5
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(xc_wk.value/dx) # index = Xcoordinate/dx
            depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
        
        
    elif change['new'] == 'JON_1D':
        #show
        container_JON1D.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
    
        # gamma value for Jonwsap = 3.3
        GammaTMA.step = 0.01
        GammaTMA.min = 3.3
        GammaTMA.value = 3.3
        
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc_wk.value = 5 
        xc_wk.max = THL.value - 5
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(xc_wk.value/dx) # index = Xcoordinate/dx
            depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
    
    elif change['new'] == 'JON_2D':
        #show
        container_JON2D.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'
        
        # gamma value for Jonwsap = 3.3
        GammaTMA.step = 0.01
        GammaTMA.min = 3.3
        GammaTMA.value = 3.3
        
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc_wk.value = 5 
        xc_wk.max = THL.value - 5 
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(xc_wk.value/dx) # index = Xcoordinate/dx
            depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
    
    elif change['new'] == 'WK_IRR':
        #show
        container_WKIRR.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_TMA_1D.layout.display='none'
        
        # gamma value for TMA = 5.0
        GammaTMA.value = 5.0
        GammaTMA.step = 0.01
        GammaTMA.min = 5.0
        
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc_wk.value = 5 
        xc_wk.max = THL.value - 5
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(xc_wk.value/dx) # index = Xcoordinate/dx
            depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
        
    elif change['new'] == 'TMA_1D/IRR_WAVE':
        #show
        container_TMA_1D.layout.display=''
        #hide
        container_IniRec.layout.display='none' 
        container_Gauss.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        
        # gamma value for TMA = 5.0
        GammaTMA.value = 5.0
        GammaTMA.step = 0.01
        GammaTMA.min = 5.0
        
        # reset xcoordinate and wavemaker depth values
        # there is a 5m separation from the boundary becasue these are internal wavemakers, hence they cant be at the boundary
        xc_wk.value = 5 
        xc_wk.max = THL.value - 5
        
        # search initial depth value at xcoordinate
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
            data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder

            fin= open(data_text,'r')  
            val = fin.read()            
            val=val.split()
            points = val[2]
            dx = float(val[5])

            index = int(xc_wk.value/dx) # index = Xcoordinate/dx
            depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater

        else:
            pass
        
    else: 
        container_Gauss.layout.display='none'
        container_IniRec.layout.display='none'
        container_IniSol.layout.display='none'
        container_WkReg.layout.display='none'
        container_JON1D.layout.display='none'
        container_JON2D.layout.display='none'
        container_WKIRR.layout.display='none'
        container_TMA_1D.layout.display='none'

## update wavemaker depth functions

# find depth value of coordinate xc    
def change_dep(change):    
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
    check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

    if check_dir_dep == True:         # if file exist...
        depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
        data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
        
        fin= open(data_text,'r')  
        val = fin.read()            
        val=val.split()
        points = val[2]
        dx = float(val[5])

        index = int(change['new']/dx) # index = Xcoordinate/dx
        dep.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
        
    else:
        pass
    

# find depth_wk value of coordinate xc_wk    
def change_dep_wk(change): 
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
    check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

    if check_dir_dep == True:         # if file exist...
        depth = np.loadtxt(Depthtext)[0]  # import depth.txt to be used in change_dep and change_dep_wk functions 
        data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
        check_dir = os.path.exists(data_text) # check if data.txt exist

        
        fin= open(data_text,'r')  
        val = fin.read()            
        val=val.split()
        points = val[2]
        dx = float(val[5])

        index = int(change['new']/dx) # index = Xcoordinate/dx
        depWK.value = '%4.2f' % (depth[index]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
        
    else:
        pass
    
## generate sponge layer variables widgets function
# this function works with the widgets on PrincipalTab_2d
from pyFiles.PrincipalTab_2 import container_csp,container_CDsponge,container_R_sponge,container_A_sponge 
def toggle_DifSponge(change):  # show/hide diffusion sponge variables
    if change['new']:
        #show
        container_csp.layout.display=''
        
    else:
        # hide
        container_csp.layout.display='none'
        
           
def toggle_FricSponge(change): # show/hide friction sponge variables
    if change['new']:
        #show
        container_CDsponge.layout.display=''
        
    else:
        # hide
        container_CDsponge.layout.display='none'
        
        
def toggle_DirSponge(change): # show/hide direct sponge variables
    if change['new']:
        #show
        container_R_sponge.layout.display=''
        container_A_sponge.layout.display=''
        
    else:
        # hide
        container_R_sponge.layout.display='none'
        container_A_sponge.layout.display='none'
            
    
        
###--------------------------------------------       
# activate functions

## PRINCIPAL_TAB functions
from pyFiles.PRINCIPAL_TAB import project_button # import pertinent variables of PRINCIPAL_TAB
project_button.on_click(project_clicked) # activate GUI

## PrincipalTab_1 functions
from pyFiles.PrincipalTab_1 import bathy_list # import pertinent variables of PrincipalTab_1

bathy_list.observe(toggle_choose_bathy, 'value')   # activate bathy type variables
toggle_choose_bathy({'new': bathy_list.value})

## PrincipalTab_2 functions
from pyFiles.PrincipalTab_2 import show_initial,ini_button,wave_maker,Dir,fric,dif,update_input_button,inputFile_button
# ^ import pertinent variables of PrincipalTab_2

show_initial.observe(toggle_initial, 'value')   # activate initial conditions input variables
toggle_initial({'new': show_initial.value})

ini_button.on_click(update_initial_conditions)  # activate generate inintial condition files button

wave_maker.observe(toggle_waveMaker, 'value')   # activate wavemaker variables
toggle_waveMaker({'new': wave_maker.value})

dif.observe(toggle_DifSponge, 'value')   # activate diffusion sponge variables
toggle_DifSponge({'new': dif.value})

fric.observe(toggle_FricSponge, 'value')   # activate friction sponge variables
toggle_FricSponge({'new': fric.value})

Dir.observe(toggle_DirSponge, 'value')   # activate direct sponge variables
toggle_DirSponge({'new': Dir.value})

xc_wk.observe(change_dep_wk, 'value')   # activate "find depth_wk of coodinate xc_wk" function  
change_dep_wk({'new': xc_wk.value})

Xwavemaker.observe(change_dep, 'value')   # activate "find depth of coodinate xwavemaker" function
change_dep({'new': Xwavemaker.value})