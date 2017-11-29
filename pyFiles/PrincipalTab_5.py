import ipywidgets as widgets
from traitlets import link


########################################
#### Principal Tab 5: Post-process  ####
########################################

from pyFiles.PrincipalTab_1 import THL as Lt
from pyFiles.PrincipalTab_2 import time_text, plotInt_text
from pyFiles.PrincipalTab_3 import steady_time, T_INTV_MEAN



# output options dropdown widget
label_intro = widgets.HTML("""Specify the type of Output you want to post-process:""",
                           layout = widgets.Layout(height = '25px'))
out_options = ['Specify Output']  
out_list = widgets.Dropdown(options = out_options)
out_list_container = widgets.VBox([label_intro,out_list],layout = widgets.Layout(height = '60px'))

space_box1 = widgets.Box(layout=widgets.Layout(width='50%',height = '20px')) # box created to have space among widgets
space_box2 = widgets.Box(layout=widgets.Layout(width='50%',height = '40px')) # box created to have space among widgets
space_box3 = widgets.Box(layout=widgets.Layout(width='5%',height = '10px')) # box created to have space among widgets

### Surface Option ###
## generate surface plot column (column 1)
PLOT_label = widgets.HTML('<b>Generate Surface Image:</b>',     
                            layout = widgets.Layout(height = '65px'))

plot_time_label = widgets.HTML("Plot Surface at time:",
                              layout = widgets.Layout(width = '40%'))
plot_time = widgets.BoundedIntText(min = 0,layout = widgets.Layout(width = '40%'))
sec_label = widgets.HTML('sec',layout = widgets.Layout(width = '15%')) # time limit unit label (seconds)
time_cont = widgets.HBox([plot_time_label,plot_time,sec_label]) # plot time limit container

# x and y axis limits for plot column
PltAxis_Label = widgets.Label('Plot Axis limits:',layout = widgets.Layout(width = '45%'))

Xmin_plt = widgets.BoundedFloatText(description = 'X Min',min = 0,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  x axis min for plot
Xmax_plt = widgets.BoundedFloatText(description = 'X Max',step = 0.1,layout = widgets.Layout(width = "50%")) #  x axis max for plot
widgets.jsdlink((Xmin_plt,'value'),(Xmax_plt,'min')) # link Xmin value to Xmax min 
Xplt_Cont = widgets.HBox(children = [Xmin_plt, Xmax_plt],
                             layout = widgets.Layout(height = '45px',width = '90%')) # x axis lim container for video
 
Ymin_plt = widgets.BoundedFloatText(description = 'Y Min',max = 20,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  y axis min for video
Ymax_plt = widgets.BoundedFloatText(description = 'Y Max',max = 20,value = 5,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  y axis max for video
widgets.jsdlink((Ymin_plt,'value'),(Ymax_plt,'min')) # link Ymin value to Ymax min
Yplt_Cont = widgets.HBox(children = [Ymin_plt, Ymax_plt],
                        layout = widgets.Layout(height = '45px',width = '90%')) # y axis lim container for video

# plot and save figure buttons 
plot_results_button = widgets.Button(description="Generate Plot",
                              layout = widgets.Layout(height = '45px',width = '90%'))
save_plot_results_button = widgets.Button(description="Save Plot",
                              layout = widgets.Layout(height = '45px',width = '90%'))

surf_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                         layout = widgets.Layout(width = '50%'))

## generate surface video column (column 2)
VIDEO_label = widgets.HTML('<b>Generate Model Video:</b>',     
                            layout = widgets.Layout(height = '34px'))

VIDEO_TIME_LABEL = widgets.HTML('Video time:',layout = widgets.Layout(width = '20%'))

TimeBegin_label = widgets.HTML('Starts:',layout = widgets.Layout(width = '10%'))
TimeBegin_text = widgets.BoundedIntText(layout = widgets.Layout(min = 0,width = "20%")) # time beginning limit for video

TimeLimit_label = widgets.HTML('Ends:',layout = widgets.Layout(width = '10%'))
TimeLimit_text = widgets.BoundedIntText(layout = widgets.Layout(min = 0,width = "20%")) # time end limit for video
widgets.jsdlink((TimeBegin_text,'value'),(TimeLimit_text,'min')) # link Xmin value to Xmax min

TimeLimit_cont = widgets.HBox(children = [TimeBegin_label,TimeBegin_text,sec_label,space_box3,
                                          TimeLimit_label, TimeLimit_text,sec_label]) # video time limit container       

# x and y axis limits for video column
VidAxis_Label = widgets.HTML('Video Axis limits:',layout = widgets.Layout(width = '45%'))

Xmin_vid = widgets.BoundedFloatText(description = 'X Min',min = 0,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  x axis min for plot
Xmax_vid = widgets.BoundedFloatText(description = 'X Max',step = 0.1,layout = widgets.Layout(width = "50%")) #  x axis max for plot
widgets.jsdlink((Xmin_vid,'value'),(Xmax_vid,'min')) # link Xmin value to Xmax min
Xvid_Cont = widgets.HBox(children = [Xmin_vid, Xmax_vid],
                             layout = widgets.Layout(height = '45px',width = '90%')) # x axis lim container for video
 
Ymin_vid = widgets.BoundedFloatText(description = 'Y Min',max = 20,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  y axis min for video
Ymax_vid = widgets.BoundedFloatText(description = 'Y Max',max = 20,value = 5,step = 0.1,
                                  layout = widgets.Layout(width = "50%")) #  y axis max for video
widgets.jsdlink((Ymin_vid,'value'),(Ymax_vid,'min')) # link Ymin value to Ymax min
Yvid_Cont = widgets.HBox(children = [Ymin_vid, Ymax_vid],
                        layout = widgets.Layout(height = '45px',width = '90%')) # y axis lim container for video

# Frame per second widget
FrameSec_label = widgets.HTML("Frames per second:",layout = widgets.Layout(width = '40%'))
FrameSec = widgets.BoundedIntText(min = 1,value = 2, layout = widgets.Layout(width = '50%'))
FrameSec_cont = widgets.HBox([FrameSec_label,FrameSec])
    
# generate video button
Video_button = widgets.Button(description="Generate Model Video",
                              layout = widgets.Layout(height = '45px',width = '90%'))

# create video progress bar
load_label = widgets.Label('Video Progress:',layout = widgets.Layout(width = '30%'))
video_load = widgets.FloatProgress(value=0.0,min=0.0,max=10.0,step=0.1,
                                 layout = widgets.Layout(height = '45px',width = '90%'))
video_load_cont = widgets.VBox([load_label,video_load])


surf_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

surf_cols = widgets.HBox([surf_col1,space_box3,surf_col2],layout=widgets.Layout(width = '100%'))  # surface columns container box

### Surf mean Option ###
# generate Surf mean plot column (column 1)
Surfmean_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                              plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%')) 

# generate Surf mean video column (column 2)
Surfmean_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Surfmean_cols = widgets.HBox([Surfmean_col1,space_box3,Surfmean_col2]) # Surfmean columns container box


### U vel Option ###
# generate U plot column (column 1)
u_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                       plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate U video column (column 2)
u_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

u_cols = widgets.HBox([u_col1,space_box3,u_col2])  # u columns container box


### Umean Option ###
# generate Umean plot column (column 1)
umean_col1 = widgets.VBox([PLOT_label,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                           plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%')) 

# generate Umean video column (column 2)
#umean_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
#                                  VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
#                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
#                    layout=widgets.Layout(width = '50%'))

umean_cols = widgets.HBox([umean_col1]) #,space_box3,vmean_col2])  # umean columns container box

### V vel Option ###
# generate V plot column (column 1)
v_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                       plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate V video column (column 2)
v_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

v_cols = widgets.HBox([v_col1,space_box3,v_col2])  # v columns container box

### Vmean Option ###
# generate Vmean plot column (column 1)
vmean_col1 = widgets.VBox([PLOT_label,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                           plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%')) 

# generate Vmean video column (column 2)
#vmean_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
#                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
#                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
#                    layout=widgets.Layout(width = '50%'))

vmean_cols = widgets.HBox([vmean_col1]) #,space_box3,vmean_col2])  # vmean columns container box

### Hmin Option ###
# generate Hmin plot column (column 1)
Hmin_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate Hsig video column (column 2)
Hmin_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Hmin_cols = widgets.HBox([Hmin_col1,space_box3,Hmin_col2])  # Hmin columns container box

### Hmax Option ###
# generate Hmax plot column (column 1)
Hmax_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate Hsig video column (column 2)
Hmax_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Hmax_cols = widgets.HBox([Hmax_col1,space_box3,Hmax_col2])  # Hmax columns container box

### Hsig Option ###
# generate Hsig plot column (column 1)
Hsig_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate Hsig video column (column 2)
Hsig_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Hsig_cols = widgets.HBox([Hsig_col1,space_box3,Hsig_col2])  # Hsig columns container box

### Hrms Option ###
# generate Hrms plot column (column 1)
Hrms_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate Hrms video column (column 2)
Hrms_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Hrms_cols = widgets.HBox([Hrms_col1,space_box3,Hrms_col2])  # Hrms columns container box


### Havg Option ###
# generate Havg plot column (column 1)
Havg_col1 = widgets.VBox([PLOT_label,time_cont,space_box1,PltAxis_Label,Xplt_Cont,Yplt_Cont,space_box1,
                          plot_results_button,space_box2,save_plot_results_button],
                                layout = widgets.Layout(width = '50%'))

# generate Hrms video column (column 2)
Havg_col2 = widgets.VBox(children=[VIDEO_label,VIDEO_TIME_LABEL,TimeLimit_cont,space_box1,
                                   VidAxis_Label,Xvid_Cont,Yvid_Cont,space_box1,
                                  FrameSec_cont,space_box1,Video_button,space_box3,video_load_cont],
                    layout=widgets.Layout(width = '50%'))

Havg_cols = widgets.HBox([Hrms_col1,space_box3,Hrms_col2])  # Havg columns container box




# create video tab
video_tabs = widgets.VBox([out_list_container,space_box2,surf_cols,Surfmean_cols,u_cols,umean_cols,v_cols,vmean_cols,Hmin_cols,
                           Hmax_cols,Hsig_cols,Hrms_cols,Havg_cols],
                          layout = widgets.Layout(height = '550px', width = '90%'))

