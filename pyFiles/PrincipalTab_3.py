import ipywidgets as widgets
from traitlets import link
from pyFiles.PrincipalTab_2 import time_text

######################################################
#### Principal Tab 3: Funwave output txt ####
######################################################

# this tab lets the user choose the variables that will appear in the output text
label_output = widgets.HTML("""Check all the variables desired in the output
                text file:""",layout = widgets.Layout(width = '90%',height = '20px'))

space_box = widgets.Box(layout=widgets.Layout(height ='25px', width='90%')) # box created to have space ammong widgets

## column 1 of output tab:
# depth_out widget container 
DEPTH_OUT = widgets.Checkbox(description='Depth', value=False)

# u widget 
U = widgets.Checkbox(description='U',value=False)

# v widget 
V = widgets.Checkbox(description='V',value=False)

# eta widget 
ETA = widgets.Checkbox(description='ETA',value=False)

# ETAmean widget 
ETAmean = widgets.Checkbox(description='ETAmean',value=False)

# Hmax widget  
Hmax = widgets.Checkbox(description='Hmax',value=False)

# Hmin widget  
Hmin = widgets.Checkbox(description='Hmin',value=False)

# mfmax widget  
MFmax = widgets.Checkbox(description='MFmax',value=False)

# umax widget  
Umax = widgets.Checkbox(description='Umax',value=False)

# VORmax widget 
VORmax = widgets.Checkbox(description='VORmax',value=False)

# Umean widget 
Umean = widgets.Checkbox(description='Umean',value=False)

# Vmean widget 
Vmean = widgets.Checkbox(description='Vmean',value=False)

container_col1 = widgets.VBox(children=[DEPTH_OUT,ETA,ETAmean,U,V,Umax,Umean,Vmean,Hmax,Hmin,MFmax,VORmax]) 

## column 2 of output tab:

# Gx widget 
Gx = widgets.Checkbox(description='Gx',value=False)

# Gy widget 
Gy = widgets.Checkbox(description='Gy',value=False)

# Fx widget 
Fx = widgets.Checkbox(description='Fx',value=False)

# Fy widget 
Fy = widgets.Checkbox(description='Fy',value=False)

# MASK widget 
MASK = widgets.Checkbox(description='MASK',value=True)

# MASK9 widget 
MASK9 = widgets.Checkbox(description='MASK9',value=False)

# SourceX widget
SourceX = widgets.Checkbox(description='SourceX',value=False)

# SourceY widget 
SourceY = widgets.Checkbox(description='SourceY',value=False)

# P widget 
P = widgets.Checkbox(description='P',value=False)

# Q widget 
Q = widgets.Checkbox(description='Q',value=False)

# AGE widget 
AGE = widgets.Checkbox(description='AGE',value=False)

# WaveHeight 
WaveHeight = widgets.Checkbox(description='Wave H',value=False)

container_col2 = widgets.VBox(children=[MASK9,SourceX,SourceY,P,Q,Fx,Fy,Gx,Gy,AGE,WaveHeight])   
                                        

## column 3 of output tab:
col_3_note = widgets.HTML("""<b>NOTE:</b> Input <b>Starting Time</b> and <b>T_INT</b> values if <b>output means</b> (e.g. Umean) 
                            and/or <b>Wave H</b> are picked.""")
                                                  
# Steady time widget container (label & bounded float text)
label_steady_time = widgets.Label('Starting Time (STEADY_TIME):',layout = widgets.Layout(width = "90%"))
steady_time = widgets.BoundedFloatText(value = 1,layout = widgets.Layout(width = "70%",height = '70px'))
container_steadyTime = widgets.VBox(children=[label_steady_time,steady_time]) 

link((time_text,'value'), (steady_time, 'max'))

# T_INTV_mean widget container (label & bounded float text)
label_TIntvMean = widgets.Label('Time Interval (T_INTV_mean):',layout = label_steady_time.layout)
T_INTV_MEAN = widgets.BoundedFloatText(value = 1,layout = steady_time.layout)
container_TIntvMean = widgets.VBox(children=[label_TIntvMean,T_INTV_MEAN])

container_col3 = widgets.VBox([col_3_note,space_box, container_steadyTime,container_TIntvMean],
                             layout = widgets.Layout(width = "30%", align_items = 'stretch'))

# create box with all columns
container_totcol = widgets.HBox([container_col1,container_col2,container_col3],
                                layout = widgets.Layout(height = '400px'))

output_tabs = widgets.VBox([label_output,space_box,container_totcol],
                           layout = widgets.Layout(width = "95%", align_items = 'stretch',height = '465px'))
