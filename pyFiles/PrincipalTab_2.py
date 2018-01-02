import ipywidgets as widgets
from traitlets import link
from pyFiles.PrincipalTab_1 import THL
import numpy as np


#####################################################
#### Tabs for Principal Tab 2: Funwave Input txt ####
#####################################################


################################
#### Tab #2a: Input Intro ####
################################

space_box1 = widgets.Box(layout=widgets.Layout(height ='25px', width='90%')) # box created to have space among widgets 
space_box2 = widgets.Box(layout=widgets.Layout(width='10%')) # box created to have space among widgets

# label with input.txt intro
label_input_INTRO = widgets.HTML("""This section sets up and creates <b>FUNWAVE's
</b> driver file <b>(input.txt)</b> according to the user's specifications.<br> It consists of the following six steps:<br><br>
<ol>
<li><b>Project Intro:</b> In this tab the user submits the <b>Number of Processors</b>, the simulation's <b>Total Time</b>, and the <b>Plot Interval.</b><br></li>

<li><b>Initial Conditions:</b> In this tab the user determines if the project has 
initial conditions and specifies their file names.<br>
<b>NOTE:</b> These files must be uploaded in the project folder, similar as the  user-defined bathymetry file.<br></li>

<li><b>Wave Maker:</b> The user chooses the wave maker and inputs its respective 
parameters.<br></li>

<li><b>Sponge Layer:</b> The user selects the sponge layers and inputs their respective values.<br></li>

<li><b>Output Options:</b> The user picks all the desired output variables from the simulation.<br></li>

<li><b>Generate Input:</b> Finally the  user verifies and generates the project driver <b>input.txt</b> file.</li>
</ol>""")


# Number of processors widget container (label & textbox)
label_processors = widgets.Label('Number of Processors:')
processors_text = widgets.BoundedFloatText(max = '32', min = '4',layout = widgets.Layout(width = "50%"))
container_processors = widgets.VBox(children=[label_processors,processors_text],
                                    layout = widgets.Layout(width = "30%"))

# Total project time widget container (label & textbox)
label_time = widgets.Label('Total Time (sec):')
time_text = widgets.BoundedFloatText(min = 10, value = 60, max=43200, layout=processors_text.layout) # total time max = 12hr
container_time = widgets.VBox(children=[label_time,time_text],
                              layout = widgets.Layout(width = "30%")) 

# Total project time widget container (label & textbox)
label_plotInt = widgets.Label('Plot Interval (sec):')
plotInt_text = widgets.BoundedFloatText(max=3600,min=1,value=5,layout=processors_text.layout) # plot time max = 1 hr
container_pltint = widgets.VBox(children=[label_plotInt,plotInt_text],
                                layout = widgets.Layout(width = "30%")) 

container_proc_time = widgets.HBox([space_box2,container_processors,container_time,container_pltint],
                                  layout = widgets.Layout(height = '75px'))

# tab 2a container box
page_inputIntro = widgets.VBox(children=[label_input_INTRO,space_box1,space_box1,
                              container_proc_time],layout = widgets.Layout(width = "90%",height = '487px',
                                                              align_items = 'stretch' ))

#####################################
#### Tab #2b: Initial Conditions ####
#####################################

label_iniCond = widgets.HTML("""Click the checkbox if you want to initialize the simulation with
none-zero elevation and velocity values.""")

show_initial = widgets.Checkbox(description='Activate initial conditions') # turn on inicial condition checkbox

label_iniCond1 = widgets.HTML("""The Initial surface (Z) file dictates if there is
        a perturbation on the originally flat water surface. The initial U velocity file specifies 
        the velocities in the x direction. They must be uploaded in 
        the project title folder before running the simulation. Once you have identified their names
        (e.g. Ini_Z.txt), press "Generate Initial Condition Files" to format the uploaded files to the
        FUNWAVE format.""",
        layout = widgets.Layout(width = '90%',
                    size = '20'))

space_box = widgets.Box(layout=widgets.Layout(height ='20px', width='90%')) 
# this ^ box is created to have space among widgets 

    # initial elevation widget container (label and textbox)
label_iniElev = widgets.Label('Initial Elevation Text File:',
                layout =  widgets.Layout(width = '18%'))
iniElev_text = widgets.Text(layout=widgets.Layout(width = "50%",height = '50px'))
container_iniElev = widgets.HBox(children=[label_iniElev,iniElev_text])

    # initial u vel widget container (label and textbox)
label_Uvel = widgets.Label('Initial U Velocity Text File:', 
             layout = widgets.Layout(width = '18%'))
Uvel_text = widgets.Text(layout = iniElev_text.layout)
container_Uvel = widgets.HBox(children=[label_Uvel,Uvel_text])

# initial v vel is not used in 1D gui, but it will be used in 2D GUI. When needed, add it to init container!!
    # initial v vel widget container (label and textbox)
label_Vvel = widgets.Label('Initial V Velocity Text File:', 
             layout = widgets.Layout(width = '18%'))
Vvel_text = widgets.Text(layout = iniElev_text.layout)
container_Vvel = widgets.HBox(children=[label_Vvel,Vvel_text])

label_iniCond2=widgets.HTML("""<b>NOTE:</b> The data format must be the same as depth file (1 row).""",
                           layout = widgets.Layout(width = "60%",height = '40px'))

# button to format the files to FUNWAVE format
ini_button = widgets.Button(description = 'Generate Initial Condition Files',     
                            layout = widgets.Layout(width = "30%",height = '40px'))   

# box containing the Note and the button
note_button_container = widgets.HBox([label_iniCond2,ini_button],layout = widgets.Layout(width = "90%"))

# initial condition box that appears if the show_initial checkbox is turned on
# the function that shows/hides this continer is at wavemaker_Function.py
init = widgets.VBox(children=[label_iniCond1,space_box,container_iniElev,
                                container_Uvel,space_box, note_button_container])  

# tab 2b container box
page_iniCond = widgets.VBox([label_iniCond,space_box,show_initial, init],
                            layout = widgets.Layout(width = "90%",height = '487px',align_items = 'stretch' ))
  

############################
#### Tab #2c: Wavemaker ####
############################

# wavemaker dropdown widget
label_wave = widgets.Label("""Specification of Wave maker:""",layout = widgets.Layout(height = '35px'))
wave_options = ('Select Wave Maker','INI_SOL','INI_REC','WK_REG',
                'JON_1D','TMA_1D/IRR_WAVE')  # add WK_IRR and JON_2D for 2D cases
wave_maker = widgets.Dropdown(options=wave_options)
wave_container = widgets.VBox([label_wave,wave_maker],layout = widgets.Layout(height = '100px'))

label_waveMaker = widgets.HTML("""Click <a href="http://udel.edu/~fyshi/FUNWAVE/definition.html" target="_blank">here</a> for
                               the parameter's definitions.""",
                                layout = widgets.Layout(height = '35px'))

wave_note = widgets.HTML("""<font color="red"><b>NOTE:</b> This is an internal wave maker. Hence, it should NOT be 
located at the boundary (x=0).</font>""")

#  wavemaker variables
EqualEnergy_label = widgets.HTML('EqualEnergy',layout = widgets.Layout(width = "20%"))
EqualEnergy = widgets.Checkbox(value=True) 
container_EqualEnergy = widgets.HBox(children=[EqualEnergy_label,EqualEnergy],
                            layout = widgets.Layout(height = '45px'))

xc_label = widgets.HTML('Xc',layout = widgets.Layout(width = "20%"))
xc = widgets.BoundedFloatText(min = 5.0, layout = widgets.Layout(width = "30%"))
container_xc = widgets.HBox(children=[xc_label,xc],
                            layout = widgets.Layout(height = '45px'))

yc_label = widgets.Label('Yc',layout = widgets.Layout(width = "20%")) 
yc = widgets.BoundedFloatText(value=0.0,layout = widgets.Layout(width = "30%")) 
container_yc = widgets.HBox(children=[yc_label,yc],
                            layout = widgets.Layout(height = '45px')) 

wid_label = widgets.Label('WID',layout = widgets.Layout(width = "20%"))
wid = widgets.BoundedFloatText(value = 0.0,layout = widgets.Layout(width = "30%")) 
container_wid = widgets.HBox(children=[wid_label,wid],
                             layout = widgets.Layout(height = '45px'))

amp_label = widgets.Label('AMP',layout = widgets.Layout(width = "20%"))
amp = widgets.BoundedFloatText(max = 1000,layout = widgets.Layout(width = "30%"))
container_amp = widgets.HBox(children=[amp_label,amp],
                             layout = widgets.Layout(height = '45px'))

dep_label = widgets.Label('DEP',layout = widgets.Layout(width = "20%"))
dep = widgets.HTML(value = '0',layout = widgets.Layout(width = "30%"))
container_dep = widgets.HBox(children=[dep_label,dep],
                             layout = widgets.Layout(height = '45px'))

LagTime_label = widgets.Label('LagTime',layout = widgets.Layout(width = "20%"))
LagTime = widgets.BoundedFloatText(max = 3600,layout = widgets.Layout(width = "30%"))
container_LagTime = widgets.HBox(children=[LagTime_label,LagTime],
                                 layout = widgets.Layout(height = '45px'))

Xwavemaker_label = widgets.Label('X_wavemaker',layout = widgets.Layout(width = "20%"))
Xwavemaker = widgets.BoundedFloatText(min = 5.0,layout = widgets.Layout(width = "30%"))
container_Xwavemaker = widgets.HBox(children=[Xwavemaker_label,Xwavemaker],
                                 layout = widgets.Layout(height = '45px'))

xc_wk_label = widgets.Label('Xc_WK',layout = widgets.Layout(width = "20%"))
xc_wk = widgets.BoundedFloatText(min = 5.0,layout = widgets.Layout(width = "30%"))
container_xc_wk = widgets.HBox(children=[xc_wk_label,xc_wk],
                               layout = widgets.Layout(height = '45px'))

yc_wk_label = widgets.Label('Yc_WK',layout = widgets.Layout(width = "20%"))
yc_wk = widgets.BoundedFloatText(value=0.0,layout = widgets.Layout(width = "30%"))
container_yc_wk = widgets.HBox(children=[yc_wk_label,yc_wk],
                               layout = widgets.Layout(height = '45px'))

tPeriod_label = widgets.Label('Tperiod',layout = widgets.Layout(width = "20%"))
tPeriod = widgets.BoundedFloatText(max = 3600,layout = widgets.Layout(width = "30%"))
container_tPeriod = widgets.HBox(children=[tPeriod_label,tPeriod],
                               layout = widgets.Layout(height = '45px'))

ampWK_label = widgets.Label('AMP_WK',layout = widgets.Layout(width = "20%"))
ampWK = widgets.BoundedFloatText(max = 1000,layout = widgets.Layout(width = "30%"))
container_ampWK = widgets.HBox(children=[ampWK_label,ampWK],
                             layout = widgets.Layout(height = '45px'))

depWK_label = widgets.Label('DEP_WK',layout = widgets.Layout(width = "20%"))
depWK = widgets.HTML(value = '0', layout = widgets.Layout(width = "30%"))
container_depWK = widgets.HBox(children=[depWK_label,depWK],
                             layout = widgets.Layout(height = '45px'))

thetaWK_label = widgets.Label('Theta_WK',layout = widgets.Layout(width = "20%"))
thetaWK = widgets.BoundedFloatText(max = 360,layout = widgets.Layout(width = "30%"))
container_thetaWK = widgets.HBox(children=[thetaWK_label,thetaWK],
                             layout = widgets.Layout(height = '45px'))

TimeRamp_label = widgets.Label('Time_ramp',layout = widgets.Layout(width = "20%"))
TimeRamp = widgets.BoundedFloatText(max = 3600,layout = widgets.Layout(width = "30%"))
container_TimeRamp = widgets.HBox(children=[TimeRamp_label,TimeRamp],
                             layout = widgets.Layout(height = '45px'))

ywidth_wk_label = widgets.Label('Ywidth_WK',layout = widgets.Layout(width = "20%"))
ywidth_wk = widgets.BoundedFloatText(value=0.0,layout=widgets.Layout(width = "30%"))
container_ywidth_wk = widgets.HBox(children=[ywidth_wk_label,ywidth_wk],
                               layout = widgets.Layout(height = '45px'))

deltaWK_label = widgets.Label('DELTA_WK',layout = widgets.Layout(width = "20%"))
deltaWK = widgets.BoundedFloatText(min=0,max=5,step=0.1,value = 0.3,
                                   layout = widgets.Layout(width = "30%")) #  usually, delta =  0.3 to 0.6
container_deltaWK = widgets.HBox(children=[deltaWK_label,deltaWK],
                             layout = widgets.Layout(height = '45px'))

FreqPeak_label = widgets.Label('FreqPeak',layout = widgets.Layout(width = "20%"))
FreqPeak = widgets.BoundedFloatText(min=0,max=1,step=0.01,layout = widgets.Layout(width = "30%"))
container_FreqPeak = widgets.HBox(children=[FreqPeak_label,FreqPeak],
                             layout = widgets.Layout(height = '45px'))

FreqMin_label = widgets.Label('FreqMin',layout = widgets.Layout(width = "20%"))
FreqMin = widgets.BoundedFloatText(min=0,max=1,step=0.01,layout = widgets.Layout(width = "30%"))
container_FreqMin = widgets.HBox(children=[FreqMin_label,FreqMin],
                             layout = widgets.Layout(height = '45px'))

FreqMax_label = widgets.Label('FreqMax',layout = widgets.Layout(width = "20%"))
FreqMax = widgets.BoundedFloatText(min=0,max=1,step=0.01,layout = widgets.Layout(width = "30%"))
container_FreqMax = widgets.HBox(children=[FreqMax_label,FreqMax],
                             layout = widgets.Layout(height = '45px'))

HMO_label = widgets.Label('Hmo',layout = widgets.Layout(width = "20%"))
HMO = widgets.BoundedFloatText(max = 1000,layout = widgets.Layout(width = "30%"))
container_HMO = widgets.HBox(children=[HMO_label,HMO],
                             layout = widgets.Layout(height = '45px'))

GammaTMA_label = widgets.Label('GammaTMA',layout = widgets.Layout(width = "20%"))
GammaTMA = widgets.BoundedFloatText(value = 3.3,layout = widgets.Layout(width = "30%"))
container_GammaTMA = widgets.HBox(children=[GammaTMA_label,GammaTMA],
                                 layout = widgets.Layout(height = '45px'))

ThetaPeak_label = widgets.Label('ThetaPeak',layout = widgets.Layout(width = "20%"))
ThetaPeak = widgets.BoundedFloatText(value = 0.0,max = 360,layout = widgets.Layout(width = "30%"))
container_ThetaPeak = widgets.HBox(children=[ThetaPeak_label,ThetaPeak],
                                 layout = widgets.Layout(height = '45px'))

NFreq_label = widgets.Label('NFreq',layout = widgets.Layout(width = "20%"))
NFreq = widgets.BoundedIntText(value = 45,step = 1,layout = widgets.Layout(width = "30%"))
container_NFreq = widgets.HBox(children=[NFreq_label,NFreq],
                                 layout = widgets.Layout(height = '45px'))

NTheta_label = widgets.Label('NTheta',layout = widgets.Layout(width = "20%"))
NTheta = widgets.BoundedIntText(value = 24,step = 1,layout = widgets.Layout(width = "30%"))
container_NTheta = widgets.HBox(children=[NTheta_label,NTheta],
                                 layout = widgets.Layout(height = '45px'))

SigmaTheta_label = widgets.Label('Sigma_Theta',layout = widgets.Layout(width = "20%"))
Sigma_Theta = widgets.BoundedFloatText(value = 24,layout = widgets.Layout(width = "30%"))
container_SigmaTheta = widgets.HBox(children=[SigmaTheta_label,Sigma_Theta],
                                 layout = widgets.Layout(height = '45px'))

### containers for each wavemaker's respective variables:
# the function that shows/hides this continers is at wavemaker_Function.py

container_IniRec = widgets.VBox(children=[container_xc,container_amp,container_wid],
                         layout = widgets.Layout(align_items = 'stretch' ))  # add container_yc for 2d gui

container_Gauss = widgets.VBox(children=[container_xc,container_amp],
                         layout = widgets.Layout(align_items = 'stretch' ))  # add container_yc,container_wid for 2d gui

container_IniSol = widgets.VBox(children=[container_Xwavemaker,container_dep,container_amp,container_LagTime],
                         layout = widgets.Layout(align_items = 'stretch' ))

container_WkReg = widgets.VBox(children=[container_xc_wk,container_depWK,container_tPeriod,container_ampWK,
                         container_thetaWK,container_deltaWK,container_TimeRamp],
                         layout = widgets.Layout(align_items = 'stretch' ))  # add container_yc_wk for 2d gui

container_JON2D_col1 = widgets.VBox(children=[container_xc_wk,container_depWK,container_yc_wk,
                         container_TimeRamp,container_GammaTMA,container_deltaWK],
                         layout = widgets.Layout(align_items = 'stretch' ))  # add this WM option to 2d gui

container_JON2D_col2 = widgets.VBox(children=[container_FreqPeak,container_FreqMin,container_FreqMax,container_HMO,
                         container_ThetaPeak,container_NFreq,container_NTheta,container_EqualEnergy],
                         layout = widgets.Layout(width = '50%'))  # add this WM option to 2d gui

container_JON2D = widgets.HBox([container_JON2D_col1,container_JON2D_col2],
                              layout = widgets.Layout(width = '90%'))   # add this WM option to 2d gui

container_JON1D_col1 = widgets.VBox(children=[container_xc_wk,container_depWK,container_TimeRamp,
                         container_GammaTMA,container_NFreq],
                         layout = widgets.Layout(width = '50%'))
container_JON1D_col2 = widgets.VBox(children=[container_FreqPeak,container_FreqMin,container_FreqMax,
                         container_deltaWK,container_HMO,container_EqualEnergy],
                         layout = widgets.Layout(width = '50%'))
container_JON1D = widgets.HBox([container_JON1D_col1,container_JON1D_col2],
                              layout = widgets.Layout(width = '90%'))

container_WkIrr_col1 = widgets.VBox(children=[container_xc_wk,container_yc_wk,container_depWK,container_TimeRamp,
                         container_FreqPeak,container_SigmaTheta,container_deltaWK],
                         layout = widgets.Layout(width = '50%'))
container_WkIrr_col2 = widgets.VBox(children=[container_FreqMin,container_FreqMax,container_HMO,
                         container_GammaTMA,container_ThetaPeak,container_NFreq,container_NTheta,container_EqualEnergy],
                         layout = widgets.Layout(width = '50%'))
container_WKIRR = widgets.HBox([container_WkIrr_col1,container_WkIrr_col2],
                              layout = widgets.Layout(width = '90%'))   # add this WM option to 2d gui

container_TMA_1D_col1 = widgets.VBox(children=[container_xc_wk,container_depWK,
                         container_TimeRamp,container_GammaTMA,container_NFreq],
                         layout = widgets.Layout(width = '50%'))
container_TMA_1D_col2 = widgets.VBox(children=[container_FreqPeak,container_FreqMin,
                         container_FreqMax,container_deltaWK,container_HMO,container_EqualEnergy],
                         layout = widgets.Layout(width = '50%'))
container_TMA_1D = widgets.HBox([container_TMA_1D_col1,container_TMA_1D_col2],
                               layout = widgets.Layout(width = '90%'))

# tab 2c container box
page_waveMaker = widgets.VBox(children=[wave_container,label_waveMaker,wave_note,container_IniRec,
                             container_Gauss,container_IniSol,
                             container_WkReg,container_JON1D,container_JON2D,
                             container_WKIRR,container_TMA_1D],
                             layout = widgets.Layout(height = '487px',width = '90%'))

###############################
#### Tab #2d: Sponge layer ####
###############################

# sponge layer tab intro label
sponge_label = widgets.HTML("""FUNWAVE possess a DHI type sponge layer. 
                        The user needs to specify the widths of two boundaries 
                        and parameters.""",layout = widgets.Layout(width = '90%',height = '55px')) 

## column 1 of sponge layer tab:

# diffusion sponge widget container (label and checkbox) 
dif = widgets.Checkbox(description='Diffusion Sponge',value=False,layout=widgets.Layout(height = '45px'))

# friction sponge widget container (label and checkbox) 
fric = widgets.Checkbox(description='Friction Sponge',value=False,layout=dif.layout)

# direct sponge widget container (label and checkbox) 
Dir = widgets.Checkbox(description='Direct Sponge',value=False,layout=dif.layout)

container_SpongeLayer_column1 = widgets.VBox(children=[dif,fric,Dir],
                                layout = widgets.Layout(width = '42%',align_items = 'flex-start'))

## column 2 of sponge layer tab:
# diffusion coefficient widget container (label and textbox)
label_CDsponge = widgets.Label('Friction Coefficient', layout=widgets.Layout(width = "70%"))
CDsponge_text = widgets.BoundedFloatText(layout = widgets.Layout(width = "55%"))
container_CDsponge = widgets.VBox(children=[label_CDsponge,CDsponge_text],
                                 layout=widgets.Layout(height = '90px'))

# friction coefficient widget container (label and textbox)
label_csp = widgets.Label('Diffusion Coefficient', layout = label_CDsponge.layout)
csp_text = widgets.BoundedFloatText(layout = widgets.Layout(width = "55%"))
container_csp = widgets.VBox(children=[label_csp,csp_text],
                            layout=widgets.Layout(height = '90px'))

# decay rate widget container (label and textbox)
label_R_sponge = widgets.Label('Decay Rate', layout = label_CDsponge.layout)
R_sponge_text = widgets.BoundedFloatText(layout=widgets.Layout(width = '55%'),value ='0.85', max = '0.95',
                                    min='0.85',step = '0.01')
container_R_sponge = widgets.VBox(children=[label_R_sponge,R_sponge_text],
                                 layout=widgets.Layout(height = '90px'))

# max decay rate widget container (label and textbox)
label_A_sponge = widgets.Label('Max Decay Rate', layout = label_CDsponge.layout)
A_sponge_text = widgets.BoundedFloatText(layout = widgets.Layout(width = "55%"),value ='5',min='5',step = '0.1')
container_A_sponge = widgets.VBox(children=[label_A_sponge,A_sponge_text],
                                 layout=widgets.Layout(height = '90px'))

container_SpongeLayer_column2 = widgets.VBox(children=[container_csp,container_CDsponge,
                                container_R_sponge,container_A_sponge],
                                layout = widgets.Layout(width = '30%'))

## Column 3 of sponge layer tab:
# sponge layer note label
sponge_note = widgets.HTML("""<b>NOTE: </b>Set width = 0.0 if no sponge.""",
                            layout=sponge_label.layout)

# Left sponge width (LSW) widget container (label and textbox)
label_LSW = widgets.Label('West Width', layout=widgets.Layout(width = "39%"))
LSW_text = widgets.BoundedFloatText(layout = widgets.Layout(width = "50%"),min =0.0,step = 0.01)
widgets.jsdlink((THL,'value'),(LSW_text,'max')) # link THL vaue to LSW_text max
container_LSW = widgets.HBox(children=[label_LSW,LSW_text],
                             layout=widgets.Layout(width = '100%',height = '65px'))

# Right sponge width (RSW) widget container (label and textbox)
label_RSW = widgets.Label('East Width', layout = label_LSW.layout)
RSW_text = widgets.BoundedFloatText(layout = LSW_text.layout,min =0.0,step = 0.01)
widgets.jsdlink((THL,'value'),(RSW_text,'max')) # link THL vaue to RSW_text max
container_RSW = widgets.HBox(children=[label_RSW,RSW_text],layout=container_LSW.layout)

# Sponge widths Top and bottom  will be used in the 2DGUI. If wanted, add them to container_SpongeLayer_column3
# Top sponge width (TSW) widget container (label and textbox)
label_TSW = widgets.Label('North Width', layout = label_LSW.layout)
TSW_text = widgets.BoundedFloatText(layout = LSW_text.layout,value = 0, min =0.0,step = 0.01)
container_TSW = widgets.HBox(children=[label_TSW,TSW_text],layout=container_LSW.layout)

# Bottom sponge width (BSW) widget container (label and textbox)
label_BSW = widgets.Label('South Width', layout = label_LSW.layout)
BSW_text = widgets.BoundedFloatText(layout = LSW_text.layout,value = 0, min =0.0,step = 0.01)
container_BSW = widgets.HBox(children=[label_BSW,BSW_text],layout=container_LSW.layout)

container_SpongeLayer_column3 = widgets.VBox(children=[sponge_note,container_LSW,container_RSW],layout = widgets.Layout(width = '30%'))

# create box with all columns
container_totalColumns = widgets.HBox(children=[container_SpongeLayer_column1,
                                                container_SpongeLayer_column2,
                                                container_SpongeLayer_column3],
                                      layout = widgets.Layout(height = '550px',width = '90%',
                                                              align_items = 'stretch' ))

# tab 2d container box
page_spongeLayer = widgets.VBox([sponge_label,container_totalColumns],
                                layout = widgets.Layout(width = "90%",height = '487px'))

#######################################################################
#### NOTE: Tab #2e: Output Options is located in PrincipalTab_3.py ####
#######################################################################


#######################################
#### Tab #2f: Input File Generator ####
#######################################

inputFile_label = widgets.HTML("""Press button to review/update <b>input.txt values</b>
 before generating the file.""",layout = widgets.Layout(width = "50%",height = '25px'))

update_input_button = widgets.Button(description = 'Review Input Values',layout = widgets.Layout(width = "50%",
                                  height = '40px'))

inputUpdate_box = widgets.HBox([inputFile_label,update_input_button],
                               layout = widgets.Layout(width = "90%",height = '55px'))

# print input.txt for verification 
input_verification = widgets.HTML() 

input_note = widgets.HTML("""<font color="red"><b>NOTE:</b> CCE users can verify their <b>input.txt</b> by opening it in your Project folder located at the Jupyter Notebook directory.</font>""")

inputFile_box = widgets.Box([input_verification],layout = widgets.Layout(height = '285px',width = '90%',
                                                                        border='solid 2px grey'))
# generate input file button
inputFile_label2 = widgets.HTML("""If you are satisfied with your input values, press the <b>Generate Input File</b> button.""",
                                layout = widgets.Layout(width = "50%",height = '25px'))
inputFile_button = widgets.Button(description = 'Generate Input File',layout = widgets.Layout(width = "50%",
                                  height = '40px'))

inputGen_box = widgets.HBox([inputFile_label2,inputFile_button],
                               layout = widgets.Layout(width = "90%",height = '55px'))

page_GenInput = widgets.VBox([inputUpdate_box,space_box1,inputFile_box,input_note,space_box1,inputGen_box],
                                 layout = page_inputIntro.layout)
