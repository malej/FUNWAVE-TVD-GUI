import numpy as np
import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display, clear_output, HTML
import os
import io
import base64

# import pertaining variables: 
from pyFiles.PRINCIPAL_TAB import principal_tab,title_text,space_box2,container_title     
# ^ import tab structure & projects name
from pyFiles.PrincipalTab_2 import time_text, plotInt_text     # total time and plot interval in (s)
from pyFiles.PrincipalTab_3 import T_INTV_MEAN, steady_time    # Wave Height time interval & starting time
from pyFiles.PrincipalTab_4 import exec_list # to know which model was ran (exec_list.value)
from pyFiles.PrincipalTab_5 import TimeBegin_text,TimeLimit_text,video_load,plot_time,out_list, Xmax_vid,Xmax_plt,Xmin_vid,Xmin_plt,Ymax_vid,Ymax_plt,Ymin_vid,Ymin_plt,FrameSec    # time values, axis limits and video loadbar widget


def show_vid(folder_path, type_vid): # show video in notebook function
        
    vid_name = '%sMovie.mp4'%(type_vid) # video name depends of the output type
    vid_path = os.path.join(folder_path,vid_name) # path to video
    video = io.open(vid_path, 'r+b').read() # read video file
        
    encoded = base64.b64encode(video) 
       
    vid = HTML(data='''<video width="900" height="400" controls>
         <source src="data:video/mp4;base64,{0}" type="video/mp4" />
         </video>'''.format(encoded.decode('ascii')))              # html video cell
        
    clear_output(wait=True)
    display(space_box2,container_title,space_box2) # display project text box and button
    display(principal_tab,vid) # display GUI & video
        
def generate_vid(folder_path, type_vid):   # run ffpmpeg function
    os.chdir(folder_path) # move to directory where the images are located (output_plots directory)
    
    # set fmpeg command line depending on the video type (eta, wave height, hmax, etc...)
 
    if exec_list.value == "FUNWAVE CCE":
        string1 = "/funwave/ffmpeg.command.dir/ffmpeg -r %d -y -i %s" % (FrameSec.value,type_vid)
    else:
        string1 = "ffmpeg -r %d -y -i %s" % (FrameSec.value,type_vid)

    string2 = "%5d.png -s 815x735 "
    string3 = "%sMovie.mp4" % (type_vid)

    run_ffmpeg = string1+string2+string3
    
    os.system(run_ffmpeg) # create video with ffmpeg terminal command 
    return_to_gui_folder = os.path.join(folder_path,'..','..')
    
    os.chdir(return_to_gui_folder) # return to GUI directory 
    show_vid(folder_path, type_vid) # call show video function
    
def video_function(type_vid,ax,mwl,x,Lt,depth,files_start,files_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid): # generate video function
    
    ## Plot Output
    ax.clear()    
    for num in range(int(files_start[0]),int(files_end[0])+1):
        fnum = '%.5d' % (num)
        
        type_vid_name = type_vid + '_' # output type file name
        output_path = os.path.join(postprocessDir,type_vid_name) # path to output file
        output = np.loadtxt(output_path+fnum) # output file data
        
        mask_path = os.path.join(postprocessDir,'mask_') # path to mask file
        mask = np.loadtxt(mask_path+fnum)
        
        out_masked = np.ma.masked_where(mask==0,output) # do not plot where mask = 0

        ax.clear()
        ax.plot(np.asarray(x),mwl,'--k',linewidth=1) # plot mean water level @ 0m
        ax.plot(np.asarray(x),depth[0,:],'k',np.asarray(x),out_masked[0,:],'c',linewidth=1)
        ax.set_xlabel('X (m)',fontsize = 12, fontweight = 'bold')
        ax.set_ylabel(type_vid+' (m)',fontsize = 12, fontweight = 'bold')
        ax.axis([Xmin_vid.value,Xmax_vid.value,Ymin_vid.value,Ymax_vid.value])

        # Water Fill:
        ax.fill_between(x, depth[0,:], out_masked[0,:],
                             where = out_masked[0,:] > depth[0,:],
                             facecolor = 'cyan', interpolate =True)

        # Bottom Fill:
        ax.fill_between(x, min(depth[0,:])-.05, depth[0,:], 
                                       where= depth[0,:] > (depth[0,:]-.05),facecolor = '0.35',
                                       hatch = 'X')
        # Time Annotations:
        if delta_time == 'PLOT_INT': # if the output time interval increases by plot_int variable
            ax.set_title('Time: %4.2f sec'%((num)*plotInt_text.value-plotInt_text.value),fontsize = 16)
            
        else: # if the output time interval increases by T_int variable
            ax.set_title('Time: %4.2f sec'%((num)*T_INTV_MEAN.value+steady_time.value),fontsize = 16)

        NUM = num-int(files_start[0])+1 # to save files starting from 01 (so that ffmpeg can read them) 
            
        # video load bar progress description:
        video_load.min = 0
        video_load.max = int(files_end[0])
        
        
        if NUM < 10:
            fileIndex = '0'+str(NUM)
            fileName = '{0}000{1:s}'.format(type_vid_name,fileIndex)
            file_path = os.path.join(folder_path,fileName)
            fig.savefig(file_path, ext="png", bbox_inches='tight')


            # video load bar progress description:
            video_load.value = num
            video_load.description = '%d/%d'%(num,int(files_end[0]))
            
        elif NUM < 100:
            fileIndex = str(NUM)
            fileName = '{0}000{1:s}'.format(type_vid_name,fileIndex)
            file_path = os.path.join(folder_path,fileName)
            fig.savefig(file_path, ext="png", bbox_inches='tight')

            # video load bar progress description: 
            video_load.value = num
            video_load.description = '%d/%d'%(num,int(files_end[0]))

        elif NUM < 1000: 
            fileIndex = str(NUM)
            fileName = '{0}00{1:s}'.format(type_vid_name,fileIndex)
            file_path = os.path.join(folder_path,fileName)
            fig.savefig(file_path, ext="png", bbox_inches='tight')

            # video load bar progress description:
            video_load.value = num
            video_load.description = '%d/%d'%(num,int(files_end[0]))

        else: 
            fileIndex = str(NUM)
            fileName = '{0}0{1:s}'.format(type_vid_name,fileIndex)
            file_path = os.path.join(folder_path,fileName)
            fig.savefig(file_path, ext="png", bbox_inches='tight')

            # video load bar progress description:
            video_load.value = num
            video_load.description = '%d/%d'%(num,int(files_end[0]))   
    
    generate_vid(folder_path, type_vid_name)
    
def plot_function(type_out,ax,mwl,x,Lt,depth,files,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt): # plot output function
  
    ## Plot Output
    ax.clear()
    for num in range(len(files)):
        fnum = '%.5d' % files[num]
        
        type_out_name = type_out + '_'
        output_path = os.path.join(postprocessDir,type_out_name) # path to output file
        output = np.loadtxt(output_path+fnum)
        
        mask_path = os.path.join(postprocessDir,'mask_') # path to mask file
        mask = np.loadtxt(mask_path+fnum)
        
        out_masked = np.ma.masked_where(mask==0,output) # do not plot where mask = 0

        ax.clear()
        ax.plot(np.asarray(x),mwl,'--k',linewidth=1) # plot mean water level @ 0m
        ax.plot(np.asarray(x),depth[0,:],'k',np.asarray(x),out_masked[0,:],'c',linewidth=1)
        ax.set_xlabel('X (m)',fontsize = 12, fontweight = 'bold')
        ax.set_ylabel(type_out+' (m)',fontsize = 12, fontweight = 'bold')
        ax.axis([Xmin_plt.value,Xmax_plt.value,Ymin_plt.value,Ymax_plt.value])

        # Water Fill:
        ax.fill_between(x, depth[0,:], out_masked[0,:],
                         where = out_masked[0,:] > depth[0,:],
                         facecolor = 'cyan', interpolate =True)

        # Bottom Fill:
        ax.fill_between(x, min(depth[0,:])-.05, depth[0,:], 
                                   where= depth[0,:] > (depth[0,:]-.05),facecolor = '0.35',
                                   hatch = 'X')
        # Time Annotations:
        ax.set_title('Time: %4.2f sec'%(plot_time.value),fontsize = 16)       
    display(fig) 
   
    
def save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt): # save plot function
    
    ## Plot Output
    ax.clear()
    for num in range(len(files)):
        fnum = '%.5d' % files[num]
        
        type_out_name = type_out + '_'
        output_path = os.path.join(postprocessDir,type_out_name) # path to output file
        output = np.loadtxt(output_path+fnum)
        
        mask_path = os.path.join(postprocessDir,'mask_') # path to mask file
        mask = np.loadtxt(mask_path+fnum)
        
        out_masked = np.ma.masked_where(mask==0,output) # do not plot where mask = 0

        ax.clear()
        ax.plot(np.asarray(x),mwl,'--k',linewidth=1) # plot mean water level @ 0m
        ax.plot(np.asarray(x),depth[0,:],'k',np.asarray(x),out_masked[0,:],'c',linewidth=1)
        ax.set_xlabel('X (m)',fontsize = 12, fontweight = 'bold')
        ax.set_ylabel(type_out+' (m)',fontsize = 12, fontweight = 'bold')
        ax.axis([Xmin_plt.value,Xmax_plt.value,Ymin_plt.value,Ymax_plt.value])

        # Water Fill:
        ax.fill_between(x, depth[0,:], out_masked[0,:],
                         where = out_masked[0,:] > depth[0,:],
                         facecolor = 'cyan', interpolate =True)

        # Bottom Fill:
        ax.fill_between(x, min(depth[0,:])-.05, depth[0,:], 
                                   where= depth[0,:] > (depth[0,:]-.05),facecolor = '0.35',
                                   hatch = 'X')
        # Time Annotations:
        ax.set_title('Time: %4.2f sec'%(plot_time.value),fontsize = 16)       
    
    # save figure
    fileName = '%s_1d_time_%dsec.png'%(type_out,int(files[num]*plotInt_text.value-plotInt_text.value))
    file_path = os.path.join(pwd,folder_name,'output_plots',fileName)
    fig.savefig(file_path, dpi=fig.dpi) # save figure
    
def plot_output_clicked(variable):    # plot results
    clear_output(wait=True)
    display(space_box2,container_title,space_box2) # display project text box and button
    display(principal_tab) # display GUI
    
    fig, ax = plt.subplots(figsize=(15,5), dpi=200)
    plt.close(fig)
    
    # File type 1: their interval is pltIntv_text (e.g. eta, Hmax, Hmin...)
    files1 = [(plot_time.value/plotInt_text.value) + 1] # number of files for eta, hmin & hmax
    
    # File type 2: their interval is T_INTV_MEAN (e.g. eta_mean, Hsig, Hrms, Havg...) 
    files2 = [(plot_time.value/T_INTV_MEAN.value)-(steady_time.value/T_INTV_MEAN.value)] # number of files for etaMean & wave height

    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    postprocessDir=os.path.join(pwd,folder_name,'output') # create output folder path

    Depthtext = os.path.join(pwd,folder_name,'depth.txt')
    depth = (np.loadtxt(Depthtext))*-1 
    pts  = len(depth.T)     # number of points

    data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
    fin= open(data_text,'r')  # upload data.txt; which has the bathy dx data
    val = fin.read()            
    val=val.split()
    dx = float(val[5])

    Lt = np.ceil(dx*(pts)) # compute total horizontal length

    x = np.linspace(0, Lt, pts)
    
    mwl = np.zeros(len(x))
    
    if out_list.value == 'Surface Elevation': #if the chosen output option is ETA
        type_out = 'eta'
        plot_function(type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value == 'Surface Elevation Mean': #if the chosen output option is ETA mean
        type_out = 'etamean'
        plot_function(type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value == 'Average Wave Height (Havg)':# if the chosen output option is Havg
        type_out = 'havg'
        plot_function(type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    elif out_list.value =='Significant Wave Height (Hsig)':#if the chosen output option is Hsig
        type_out = 'hsig'
        plot_function(type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    elif out_list.value =='Root Mean Square Wave Height (Hrms)':# if the chosen output option is Hrms
        type_out = 'hrms'
        plot_function(type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value =='Maximum surface elevation (Hmax)':# if the chosen output option is Hmax
        type_out = 'hmax'
        plot_function(type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value =='Minimum surface elevation (Hmin)': # if the chosen output option is Hmin
        type_out = 'hmin'
        plot_function(type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig,Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    else:
        pass
           

def save_plot_clicked(variable):    # save output plot results
    
    fig, ax = plt.subplots(figsize=(15,5), dpi=200)
    plt.close(fig)
    
    # File type 1: their interval is pltIntv_text (e.g. eta, Hmax, Hmin...)
    files1 = [(plot_time.value/plotInt_text.value) + 1] # number of files for eta, hmin & hmax
    
    # File type 2: their interval is T_INTV_MEAN (e.g. eta_mean, Hsig, Hrms, Havg...) 
    files2 = [(plot_time.value/T_INTV_MEAN.value)-(steady_time.value/T_INTV_MEAN.value)] # number of files for etaMean & wave height

    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    postprocessDir=os.path.join(pwd,folder_name,'output') # create output folder path

    Depthtext = os.path.join(pwd,folder_name,'depth.txt')
    depth = (np.loadtxt(Depthtext))*-1 
    pts  = len(depth.T)     # number of points

    data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
    fin= open(data_text,'r')  # upload data.txt; which has the bathy dx data
    val = fin.read()            
    val=val.split()
    dx = float(val[5])

    Lt = np.ceil(dx*(pts)) # compute total horizontal length

    x = np.linspace(0, Lt, pts)
   
    mwl = np.zeros(len(x))
    
    if out_list.value == 'Surface Elevation': #if the chosen output option is ETA, go to saveETA function
        type_out = 'eta'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value == 'Surface Elevation Mean': #if the chosen output option is ETA mean, go to saveETAmean function
        type_out = 'etamean'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value == 'Average Wave Height (Havg)':# if the chosen output option is Havg, go to saveHsig function
        type_out = 'havg'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    elif out_list.value =='Significant Wave Height (Hsig)':#if the chosen output option is Hsig, go to saveHsig function
        type_out = 'hsig'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    elif out_list.value =='Root Mean Square Wave Height (Hrms)':# if the chosen output option is Hrms, go to saveHsig function
        type_out = 'hrms'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value =='Maximum surface elevation (Hmax)':# if the chosen output option is Hmax, go to saveHsig function
        type_out = 'hmax'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
        
    elif out_list.value =='Minimum surface elevation (Hmin)': # if the chosen output option is Hmin, go to saveHsig function
        type_out = 'hmin'
        save_plot_function(pwd,type_out,ax,mwl,x,Lt,depth,files1,postprocessDir,folder_name,fig, Xmax_plt,Xmin_plt,Ymax_plt,Ymin_plt)
    
    else:
        pass

def runVID_function(variable):   # generate video of plots
    
    fig, ax = plt.subplots(figsize=(15,5), dpi=200)
    plt.close(fig)
    
    # File type 1: their interval is pltIntv_text (e.g. eta, Hmax, Hmin...) 
    files1_start = [(TimeBegin_text.value/plotInt_text.value) + 1]
    # ^ file number for video start time (TimeBegin_text variable in PrincipalTab_5)
    files1_end = [(TimeLimit_text.value/plotInt_text.value) + 1] 
    # ^ file number for video ending time (TimeLimit_text variable in PrincipalTab_5)
    
    # File type 2: their interval is T_INTV_MEAN (e.g. eta_mean, Hsig, Hrms, Havg...) 
    files2_start = [(TimeBegin_text.value/T_INTV_MEAN.value)-(steady_time.value/T_INTV_MEAN.value)] 
    # ^ file number for video start time (TimeBegin_text variable in PrincipalTab_5)
    files2_end = [(TimeLimit_text.value/T_INTV_MEAN.value)-(steady_time.value/T_INTV_MEAN.value)] 
    # ^ file number for video ending time (TimeLimit_text variable in PrincipalTab_5)
    
    
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title given by the user (widget located in PRINCIPAL_TAB)
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'

    postprocessDir=os.path.join(pwd,folder_name,'output') # path to output folder
    folder_path=os.path.join(pwd,folder_name,'output_plots') # path to save plots in project folder

    Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth file
    depth = (np.loadtxt(Depthtext))*-1 
    pts  = len(depth.T)     # number of points

    data_text = os.path.join(pwd,folder_name,'data.txt') # create path to open data.txt in project folder
    fin= open(data_text,'r')  # upload data.txt; which has the bathy dx data
    val = fin.read()            
    val=val.split()
    dx = float(val[5])

    Lt = np.ceil(dx*(pts)) # compute total horizontal length

    x = np.linspace(0, Lt, pts)
    
    mwl = np.zeros(len(x)) # mean water level = 0 
    
    if out_list.value == 'Surface Elevation': #if the chosen output option is ETA, go to video ETA function
        type_vid = "eta"
        delta_time = 'PLOT_INT' # output time interval increases by plot_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files1_start,files1_end,postprocessDir,folder_path,fig,delta_time,Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid)  
               
    elif out_list.value == 'Surface Elevation Mean': #if the chosen output option is ETA mean, go to videoETAmean function
        type_vid = "etamean"
        delta_time = 'T_INT' # output time interval increases by T_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files2_start,files2_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    elif out_list.value == 'Average Wave Height (Havg)':# if the chosen output option is Havg, go to videoHsig function
        type_vid = "havg"
        delta_time = 'T_INT' # output time interval increases by T_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files2,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    elif out_list.value =='Significant Wave Height (Hsig)':#if the chosen output option is Hsig, go to videoHsig function
        type_vid = "hsig"
        delta_time = 'T_INT' # output time interval increases by T_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files2_start,files2_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    elif out_list.value =='Root Mean Square Wave Height (Hrms)':# if the chosen output option is Hrms, go to videoHsig function
        type_vid = "hrms"
        delta_time = 'T_INT' # output time interval increases by T_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files2_start,files2_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    elif out_list.value =='Maximum surface elevation (Hmax)':# if the chosen output option is Hmax, go to videoHsig function
        type_vid = "hmax"
        delta_time = 'PLOT_INT' # output time interval increases by plot_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files1_start,files1_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    elif out_list.value =='Minimum surface elevation (Hmin)': # if the chosen output option is Hmin, go to videoHsig function
        type_vid = "hmin"
        delta_time = 'PLOT_INT' # output time interval increases by plot_int variable
        video_function(type_vid,ax,mwl,x,Lt,depth,files1_start,files1_end,postprocessDir,folder_path,fig,delta_time, Xmax_vid,Xmin_vid,Ymax_vid,Ymin_vid) 
                
    else:
        pass
    
###--------------------------------------------       
# activate functions    
from pyFiles.PrincipalTab_5 import plot_results_button,save_plot_results_button,Video_button
# ^ import pertinent variables of PrincipalTab_5

plot_results_button.on_click(plot_output_clicked)             # activate plot result button
save_plot_results_button.on_click(save_plot_clicked)    # activate save plot button
Video_button.on_click(runVID_function)             # activate run video button 






