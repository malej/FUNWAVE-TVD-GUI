# This python file arranges the complete SegmentLeveeGUI tab structure

#%matplotlib inline 
#%matplotlib notebook
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
from IPython.core.display import HTML


# Project title widget container (project label, project textbox, space between project widgets & project button)
label_title = widgets.HTML('Project Title:')
title_text = widgets.Text(layout=widgets.Layout(width = "40%"))
space_box1 = widgets.Box(layout=widgets.Layout(width='10%')) # box created to have space among widgets
project_button = widgets.Button(description = 'Generate Project',     
                            layout = widgets.Layout(width = "30%",height = '40px'))  
container_title = widgets.HBox(children=[label_title,title_text,space_box1,project_button],
                               layout = widgets.Layout(width = '90%'))

space_box2 = widgets.Box(layout=widgets.Layout(height ='20px', width='90%')) # box created to have space among widgets 

##########################################################
#### Tabs for Principal Tab 1: Bathymetry development ####
##########################################################


# import bathy type container box and plot & save buttons
from pyFiles.PrincipalTab_1 import page_BATHY,plot_button,save_button

bathy_tabs = page_BATHY


#####################################################
#### Tabs for Principal Tab 2: Funwave Input txt ####
#####################################################


################################
#### Tab #2a: Input Intro ####
################################

# tab 2a container box
from pyFiles.PrincipalTab_2 import page_inputIntro     


#####################################
#### Tab #2b: Initial Conditions ####
#####################################

# tab 2b container box
from pyFiles.PrincipalTab_2 import page_iniCond 


############################
#### Tab #2c: Wavemaker ####
############################

# tab 2c container box
from pyFiles.PrincipalTab_2 import page_waveMaker,wave_maker 


###############################
#### Tab #2d: Sponge layer ####
###############################

# tab 2d container box
from pyFiles.PrincipalTab_2 import page_spongeLayer 

#############################################
#### Principal Tab 3: Funwave output txt ####    # this tab was merged to principal tab 2 (now Tab #2e)
#############################################

# principal tab 2e
from pyFiles.PrincipalTab_3 import output_tabs

#######################################
#### Tab #2e: Input File Generator ####
#######################################

from pyFiles.PrincipalTab_2 import page_GenInput, inputFile_button

####################################################
### Display tabs of Principal tab 2 & 3 (Merged) ###
####################################################

input_tabs = widgets.Tab(children=[page_inputIntro,page_iniCond,
                                   page_waveMaker,page_spongeLayer,output_tabs,page_GenInput])

input_tabs.set_title(0,'1- Project Intro')
input_tabs.set_title(1,'2- Initial Conditions')
input_tabs.set_title(2,'3- Wave Maker')
input_tabs.set_title(3,'4- Sponge Layer')
input_tabs.set_title(4,'5- Output Options') # previously known as Principal Tab 3
input_tabs.set_title(5,'6- Generate Input') 


#######################################
#### Principal Tab 4: Run Funwave  ####
#######################################

# principal tab 4
from pyFiles.PrincipalTab_4 import RUNfunwave_tabs,RunFunwave_button


###########################################
#### Principal Tab 5: Post Processing  ####
###########################################

# principal tab 5
from pyFiles.PrincipalTab_5 import Video_button,video_tabs


#################################
#### Display Principal Tabs  ####
#################################

principal_tab = widgets.Tab(children=[bathy_tabs,input_tabs,RUNfunwave_tabs,video_tabs])

# Set the Principal Tab's titles:
principal_tab.set_title(0,'Step 1: Bathymetry')
principal_tab.set_title(1,'Step 2: Input File')
principal_tab.set_title(2,'Step 3: Run Model')    
principal_tab.set_title(3,'Step 4: Post Process')


#################################
#### GUI STRUCTURE CONTAINER ####
#################################

GUI_CONT = widgets.VBox([space_box2,container_title,space_box2,principal_tab])