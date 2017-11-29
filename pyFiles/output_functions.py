import ipywidgets as widgets
from traitlets import link
from IPython.display import display
import numpy as np
import os

##### This py file contains all the functions related to the widgets
##### located in the output-post-processing tab (PrincipalTab_5)

# import pertinent variables from PRINCIPAL_TAB
from pyFiles.PRINCIPAL_TAB import title_text

# import pertinent variables from principal tab 1
from pyFiles.PrincipalTab_1 import THL

# import pertinent variables from principal tab 2 (input txt : total time & plot interval)
from pyFiles.PrincipalTab_2 import time_text, plotInt_text

# import pertinent variables from principal tab 3 (checklist of Output options tab)
from pyFiles.PrincipalTab_3 import DEPTH_OUT, U, V, ETA, Hmax, Hmin, MFmax, Umax, VORmax, Umean, Vmean, ETAmean, MASK, MASK9, SourceX, SourceY, P, Q, Fx, Fy, Gx, Gy, AGE, WaveHeight, steady_time, T_INTV_MEAN

# import pertinent variables from principal tab 5 (output-post-processing tab)
from pyFiles.PrincipalTab_5 import out_options, out_list, plot_time,TimeBegin_text, TimeLimit_text, vmean_cols, umean_cols, surf_cols, u_cols, v_cols, Surfmean_cols,Hmax_cols,Hmin_cols, Hsig_cols, Hrms_cols, Havg_cols, PLOT_label, plot_time_label, VIDEO_label,Xmax_vid,Xmax_plt,Xmin_vid,Xmin_plt,Ymax_vid,Ymax_plt,Ymin_vid,Ymin_plt


# The next Functions called toggle_output_"variable" adds/removes the output variable to output list
# if that variable was turned on in the Input file's output options (principaltab_3)
def toggle_output_ETA(change):
    if change['new']:    
        # if output variable is turned on, show it in output list
        out_options.append('Surface Elevation')
        out_list.options = out_options
    else:
        if 'Surface Elevation' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('Surface Elevation') 
            out_list.options = out_options
        else:
            pass

def toggle_output_U(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('U Velocity')
        out_list.options = out_options
    else:
        if 'U Velocity' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('U Velocity') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_V(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('V Velocity')
        out_list.options = out_options
    else:
        if 'V Velocity' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('V Velocity') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_Hmax(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Maximum surface elevation (Hmax)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Maximum surface elevation (Hmax)' in out_options: 
            out_options.remove('Maximum surface elevation (Hmax)') 
            out_list.options = out_options
        else:
            pass

def toggle_output_Hmin(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Minimum surface elevation (Hmin)')
        out_list.options = out_options
    else:  # if output variable is turned off, remove it from output list
        if 'Minimum surface elevation (Hmin)' in out_options: 
            out_options.remove('Minimum surface elevation (Hmin)') 
            out_list.options = out_options
        else:
            pass        

def toggle_output_MFmax(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Maximum momentum flux (MFmax)')
        out_list.options = out_options
    else:  # if output variable is turned off, remove it from output list
        if 'Maximum momentum flux (MFmax)' in out_options: 
            out_options.remove('Maximum momentum flux (MFmax)') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_Umax(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('U maximum velocity')
        out_list.options = out_options
    else:
        if 'U maximum velocity' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('U maximum velocity') 
            out_list.options = out_options
        else:
            pass

        
def toggle_output_VORmax(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Maximum vorticity (VORmax)')
        out_list.options = out_options
    else:  # if output variable is turned off, remove it from output list
        if 'Maximum vorticity (VORmax)' in out_options: 
            out_options.remove('Maximum vorticity (VORmax)') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_Umean(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('U Velocity Mean')
        out_list.options = out_options
    else:
        if 'U Velocity Mean' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('U Velocity Mean') 
            out_list.options = out_options
        else:
            pass

def toggle_output_Vmean(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('V Velocity Mean')
        out_list.options = out_options
    else:
        if 'V Velocity Mean' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('V Velocity Mean') 
            out_list.options = out_options
        else:
            pass
 
def toggle_output_ETAmean(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Surface Elevation Mean')
        out_list.options = out_options
    else:
        if 'Surface Elevation Mean' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('Surface Elevation Mean') 
            out_list.options = out_options
        else:
            pass


def toggle_output_MASK9(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('MASK9')
        out_list.options = out_options
    else:
        if 'MASK9' in out_options: # if output variable is turned off, remove it from output list
            out_options.remove('MASK9') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_SourceX(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Output source terms in x direction (SourceX)')
        out_list.options = out_options
    else:  # if output variable is turned off, remove it from output list
        if 'Output source terms in x direction (SourceX)' in out_options: 
            out_options.remove('Output source terms in x direction (SourceX)') 
            out_list.options = out_options
        else:
            pass 
        
def toggle_output_SourceY(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Output source terms in y direction (SourceY)')
        out_list.options = out_options
    else:  # if output variable is turned off, remove it from output list
        if 'Output source terms in y direction (SourceY)' in out_options: 
            out_options.remove('Output source terms in y direction (SourceY)') 
            out_list.options = out_options
        else:
            pass 

def toggle_output_P(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Momentum flux in x direction (P)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Momentum flux in x direction (P)' in out_options: 
            out_options.remove('Momentum flux in x direction (P)') 
            out_list.options = out_options
        else:
            pass 
        
def toggle_output_Q(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Momentum flux in y direction (Q)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Momentum flux in y direction (Q)' in out_options: 
            out_options.remove('Momentum flux in y direction (Q)') 
            out_list.options = out_options
        else:
            pass
        
def toggle_output_Fx(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Numerical flux F in x direction (Fx)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Numerical flux F in x direction (Fx)' in out_options: 
            out_options.remove('Numerical flux F in x direction (Fx)') 
            out_list.options = out_options
        else:
            pass

def toggle_output_Fy(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Numerical flux F in y direction (Fy)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Numerical flux F in y direction (Fy)' in out_options: 
            out_options.remove('Numerical flux F in y direction (Fy)') 
            out_list.options = out_options
        else:
            pass        

def toggle_output_Gx(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Numerical flux G in x direction (Gx)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Numerical flux G in x direction (Gx)' in out_options: 
            out_options.remove('Numerical flux G in x direction (Gx)') 
            out_list.options = out_options
        else:
            pass

def toggle_output_Gy(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Numerical flux G in y direction (Gy)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Numerical flux G in y direction (Gy)' in out_options: 
            out_options.remove('Numerical flux G in y direction (Gy)') 
            out_list.options = out_options
        else:
            pass        

def toggle_output_AGE(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Breaking age (AGE)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Breaking age (AGE)' in out_options: 
            out_options.remove('Breaking age (AGE)') 
            out_list.options = out_options
        else:
            pass  
     

def toggle_output_WaveHeight(change):
    if change['new']:   
        # if output variable is turned on, show it in output list
        out_options.append('Significant Wave Height (Hsig)')
        out_options.append('Root Mean Square Wave Height (Hrms)')
        out_options.append('Average Wave Height (Havg)')
        out_list.options = out_options
    else: # if output variable is turned off, remove it from output list
        if 'Significant Wave Height (Hsig)' in out_options: 
            out_options.remove('Significant Wave Height (Hsig)') 
            out_list.options = out_options
        else:
            pass
        
        if 'Root Mean Square Wave Height (Hrms)' in out_options: 
            out_options.remove('Root Mean Square Wave Height (Hrms)') 
            out_list.options = out_options
        else:
            pass
        
        if 'Average Wave Height (Havg)' in out_options: 
            out_options.remove('Average Wave Height (Havg)') 
            out_list.options = out_options
        else:
            pass


def toggle_choose_output(change):  
# This function shows the post-process window of the type of output that was chosen
    if change['new'] == 'Specify Output': #hide if none are chosen
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        surf_cols.layout.display='none'
        u_cols.layout.display='none' 
        v_cols.layout.display='none'
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'        
        
    elif change['new'] == 'Minimum surface elevation (Hmin)':
        #show
        Hmin_cols.layout.display=''
        PLOT_label.value ='<b>Generate Hmin Image:</b>'
        plot_time_label.value = "Plot Hmin at time:"
        VIDEO_label.value = '<b>Generate Hmin Video:</b>'
        
        #hide
        Hmax_cols.layout.display='none'
        surf_cols.layout.display='none'
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none'
        v_cols.layout.display='none' 
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        
        # link total time & plot interval to image & video output time
        plot_time.min = 0
        plot_time.step = plotInt_text.value
        plot_time.value = 0
        plot_time.max = time_text.value
        
        TimeBegin_text.min = 0
        TimeBegin_text.value = 0
        TimeBegin_text.step = plotInt_text.value
        TimeBegin_text.max = time_text.value - plotInt_text.value
        
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = plotInt_text.value
        TimeLimit_text.max = time_text.value
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass

    elif change['new'] == 'Maximum surface elevation (Hmax)':
        #show
        Hmax_cols.layout.display=''
        PLOT_label.value ='<b>Generate Hmax Image:</b>'
        plot_time_label.value = "Plot Hmax at time:"
        VIDEO_label.value = '<b>Generate Hmax Video:</b>'
        
        #hide
        Hmin_cols.layout.display='none'
        surf_cols.layout.display='none'
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none'
        v_cols.layout.display='none' 
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        
        # link total time & plot interval to image & video output time
        plot_time.min = 0
        plot_time.step = plotInt_text.value
        plot_time.value = 0
        plot_time.max = time_text.value
        
        TimeBegin_text.min = 0
        TimeBegin_text.value = 0
        TimeBegin_text.step = plotInt_text.value
        TimeBegin_text.max = time_text.value - plotInt_text.value
        
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = plotInt_text.value
        TimeLimit_text.max = time_text.value
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
    elif change['new'] == 'Surface Elevation Mean':
        #show
        Surfmean_cols.layout.display=''
        PLOT_label.value ='<b>Generate Surface Mean Image:</b>'
        VIDEO_label.value = '<b>Generate Surface Mean Video:</b>'
        
        #hide
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        surf_cols.layout.display='none'
        u_cols.layout.display='none' 
        v_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'
        
        # change plot time limits for eta mean output processing
        plot_time.value = steady_time.value + T_INTV_MEAN.value
        plot_time.step = T_INTV_MEAN.value   # eta mean plot step = t_intv
        plot_time.max = time_text.value     # eta mean plot max = total time
        plot_time.min = steady_time.value + T_INTV_MEAN.value     # first eta mean plot @ steady + t_intv
        
        TimeBegin_text.max = time_text.value 
        TimeBegin_text.min = steady_time.value + T_INTV_MEAN.value 
        TimeBegin_text.step = T_INTV_MEAN.value   
               
        TimeLimit_text.max = time_text.value
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = T_INTV_MEAN.value        
        
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
    elif change['new'] == 'Significant Wave Height (Hsig)':
        #show
        Hsig_cols.layout.display=''
        PLOT_label.value ='<b>Generate Hsig Image:</b>'
        plot_time_label.value = "Plot Hsig at time:"
        VIDEO_label.value = '<b>Generate Hsig Video:<b>'   
        
        #hide
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none' 
        v_cols.layout.display='none'
        Surfmean_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'
        
        # change plot time limits for eta mean output processing
        plot_time.value = steady_time.value + T_INTV_MEAN.value
        plot_time.step = T_INTV_MEAN.value   # eta mean plot step = t_intv
        plot_time.max = time_text.value     # eta mean plot max = total time
        plot_time.min = steady_time.value + T_INTV_MEAN.value     # first eta mean plot @ steady + t_intv
        
        TimeBegin_text.max = time_text.value 
        TimeBegin_text.min = steady_time.value + T_INTV_MEAN.value 
        TimeBegin_text.step = T_INTV_MEAN.value   
               
        TimeLimit_text.max = time_text.value
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = T_INTV_MEAN.value     
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
    elif change['new'] == 'Root Mean Square Wave Height (Hrms)':
        #show
        Hrms_cols.layout.display=''
        PLOT_label.value ='<b>Generate Hrms Image:</b>'
        plot_time_label.value = "Plot Hrms at time:"
        VIDEO_label.value = '<b>Generate Hrms Video:</b>'       
        
        #hide
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none' 
        v_cols.layout.display='none'
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Havg_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'
        
        # change plot time limits for eta mean output processing
        plot_time.value = steady_time.value + T_INTV_MEAN.value
        plot_time.step = T_INTV_MEAN.value   # eta mean plot step = t_intv
        plot_time.max = time_text.value     # eta mean plot max = total time
        plot_time.min = steady_time.value + T_INTV_MEAN.value     # first eta mean plot @ steady + t_intv
        
        TimeBegin_text.max = time_text.value 
        TimeBegin_text.min = steady_time.value + T_INTV_MEAN.value 
        TimeBegin_text.step = T_INTV_MEAN.value   
               
        TimeLimit_text.max = time_text.value
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = T_INTV_MEAN.value   
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
    elif change['new'] == 'Average Wave Height (Havg)':
        #show
        Havg_cols.layout.display=''
        PLOT_label.value ='<b>Generate Havg Image:</b>'
        plot_time_label.value = "Plot Havg at time:"
        VIDEO_label.value = '<b>Generate Havg Video:</b>'
           
        #hide
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none' 
        v_cols.layout.display='none'
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'
       
        # change plot time limits for eta mean output processing
        plot_time.value = steady_time.value + T_INTV_MEAN.value
        plot_time.step = T_INTV_MEAN.value   # eta mean plot step = t_intv
        plot_time.max = time_text.value     # eta mean plot max = total time
        plot_time.min = steady_time.value + T_INTV_MEAN.value     # first eta mean plot @ steady + t_intv
        
        TimeBegin_text.max = time_text.value 
        TimeBegin_text.min = steady_time.value + T_INTV_MEAN.value 
        TimeBegin_text.step = T_INTV_MEAN.value   
               
        TimeLimit_text.max = time_text.value
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = T_INTV_MEAN.value   
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value
        
        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
    else:
        #show Surface Elevation:
        surf_cols.layout.display=''
        PLOT_label.value ='<b>Generate Surface Image:</b>'
        plot_time_label.value = "Plot Surface at time:"
        VIDEO_label.value = '<b>Generate Surface Video:</b>'
        
        #hide
        vmean_cols.layout.display='none'
        umean_cols.layout.display='none'
        u_cols.layout.display='none'
        v_cols.layout.display='none' 
        Surfmean_cols.layout.display='none'
        Hsig_cols.layout.display='none'
        Hrms_cols.layout.display='none'
        Havg_cols.layout.display='none'
        Hmin_cols.layout.display='none'
        Hmax_cols.layout.display='none'
        
        # link total time & plot interval to image & video output time
        plot_time.min = 0
        plot_time.step = plotInt_text.value
        plot_time.value = 0
        plot_time.max = time_text.value
        
        TimeBegin_text.min = 0
        TimeBegin_text.value = 0
        TimeBegin_text.step = plotInt_text.value
        TimeBegin_text.max = time_text.value - plotInt_text.value
        
        TimeLimit_text.value = time_text.value
        TimeLimit_text.step = plotInt_text.value
        TimeLimit_text.max = time_text.value
        
        # link X axis limits to THL (plot column)
        Xmin_plt.max = THL.value-5 # -5 so that it wont interfere with the max axis
        Xmax_plt.max = THL.value
        Xmin_plt.value = 0
        Xmax_plt.value = THL.value
        
        # link X axis limits to THL (video column)
        Xmin_vid.max = THL.value-5
        Xmax_vid.max = THL.value
        Xmin_vid.value = 0
        Xmax_vid.value = THL.value

        # link Y axis limits to depth (plot & video columns)
        pwd = os.getcwd()  # get current path
        s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
        s = s.replace(" ", "_")
        folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

        Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
        check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist

        if check_dir_dep == True:         # if file exist...
            depth = np.loadtxt(Depthtext)  # import depth.txt to be used in change_dep and change_dep_wk functions 
            Ymin_vid.min = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.min = min(depth[0,:]*-1)  
            
            Ymin_vid.value = min(depth[0,:]*-1) # multiplied by -1 to have [+] for surface and [-] for underwater
            Ymin_plt.value = min(depth[0,:]*-1)
        else:
            pass
        
###--------------------------------------------       
# activate functions               
ETA.observe(toggle_output_ETA, 'value')   # add ETA to output list if turned on
toggle_output_ETA({'new': ETA.value})

Hmax.observe(toggle_output_Hmax, 'value')   # add Hmax to output list if turned on
toggle_output_Hmax({'new': Hmax.value})

Hmin.observe(toggle_output_Hmin, 'value')   # add Hmin to output list if turned on
toggle_output_Hmin({'new': Hmin.value})

ETAmean.observe(toggle_output_ETAmean, 'value')   # add ETAmean to output list if turned on
toggle_output_ETAmean({'new': ETAmean.value})
  

out_list.observe(toggle_choose_output, 'value')   # activate toggle_choose_output function
toggle_choose_output({'new': out_list.value})


###Commented out because they will be used on GUI 2D:

#WaveHeight.observe(toggle_output_WaveHeight, 'value')   # add WaveHeight to output list if turned on
#toggle_output_WaveHeight({'new': WaveHeight.value}) 

#MFmax.observe(toggle_output_MFmax, 'value')   # add MFmax to output list if turned on
#toggle_output_MFmax({'new': MFmax.value})

#Umax.observe(toggle_output_Umax, 'value')   # add Umax to output list if turned on
#toggle_output_Umax({'new': Umax.value})

#VORmax.observe(toggle_output_VORmax, 'value')   # add VORmax to output list if turned on
#toggle_output_VORmax({'new': VORmax.value})

#Umean.observe(toggle_output_Umean, 'value')   # add Umean to output list if turned on
#toggle_output_Umean({'new': Umean.value})

#Vmean.observe(toggle_output_Vmean, 'value')   # add Vmean to output list if turned on
#toggle_output_Vmean({'new': Vmean.value})

#U.observe(toggle_output_U, 'value')   # add U to output list if turned on
#toggle_output_U({'new': U.value})

#V.observe(toggle_output_V, 'value')   # add V to output list if turned on
#toggle_output_V({'new': V.value})

#MASK.observe(toggle_output_MASK, 'value')   # add MASK to output list if turned on
#toggle_output_MASK({'new': MASK.value})

#MASK9.observe(toggle_output_MASK9, 'value')   # add MASK9 to output list if turned on
#toggle_output_MASK9({'new': MASK9.value})

#SourceX.observe(toggle_output_SourceX, 'value')   # add SourceX to output list if turned on
#toggle_output_SourceX({'new': SourceX.value})

#SourceY.observe(toggle_output_SourceY, 'value')   # add SourceY to output list if turned on
#toggle_output_SourceY({'new': SourceY.value})

#Q.observe(toggle_output_Q, 'value')   # add Q to output list if turned on
#toggle_output_Q({'new': Q.value})

#P.observe(toggle_output_P, 'value')   # add P to output list if turned on
#toggle_output_P({'new': P.value})

#Fx.observe(toggle_output_Fx, 'value')   # add Fx to output list if turned on
#toggle_output_Fx({'new': Fx.value})

#Fy.observe(toggle_output_Fy, 'value')   # add Fy to output list if turned on
#toggle_output_Fy({'new': Fy.value})

#Gx.observe(toggle_output_Gx, 'value')   # add Gx to output list if turned on
#toggle_output_Fx({'new': Fx.value})

#Gy.observe(toggle_output_Gy, 'value')   # add Gy to output list if turned on
#toggle_output_Gy({'new': Gy.value})

#AGE.observe(toggle_output_AGE, 'value')   # add AGE to output list if turned on
#toggle_output_AGE({'new': AGE.value})
