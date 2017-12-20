import ipywidgets as widgets
from IPython.display import Image
from traitlets import link

##########################################################
#### Tabs for Principal Tab 1: Bathymetry development ####
##########################################################

space_box = widgets.Box(layout=widgets.Layout(height ='25px')) # box created to have space among widgets
space_box2 = widgets.Box(layout=widgets.Layout(width = "5%",height ='60px')) # box created to have space among widgets

# bathymetry dropdown widget
label_intro = widgets.HTML("""Specify the type of One-Dimensional Bathymetry:""",
                           layout = widgets.Layout(height = '25px'))
bathy_options = ('Select Bathy','Upload File','Slope','Flat')  
bathy_list = widgets.Dropdown(options=bathy_options)
bathy_list_container = widgets.VBox([label_intro,bathy_list],layout = widgets.Layout(height = '70px'))

#####################################
### Option #1a: Upload Bathy File ###
#####################################

label_intro1 = widgets.HTML("""<ul> 
<li><b>Substep 1:</b> Upload your file in the <b>Project Title</b> folder through  the <b>Jupyter Notebook home directory</b>. Go inside your Projet's folder and upload the file by pressing the "Upload" button located at the top right corner of the directory.<br></li>
<br>
<b>NOTE: </b>This file must be a text file (ASCII) of 1 column; with depth values [-] for underwater (below mean water level). Also, the values must be in <b>metric</b> units.<br><br>

<li><b>Substep 2:</b> Once the file is uploaded, identify its name (e.g., myBathy.txt), and eitehr its step size (DX) or its Total Horizontal Length (THL) in the widgets/box below. Press "Plot Bathymetry" to visualize the bathymetry.<br><br></li>

<li><b>Substep 3:</b> If you are satisfied with the bathymetry, you must press <b> Assemble Bathymetry File</b> button before continuing to <b>Step #2</b>. This will format the uploaded bathymetry file to the <b>required FUNWAVE format.</b><br><br></li>
</ul>
""",layout=widgets.Layout(width='90%'))


bathy_name = widgets.HTML("File name:",layout=widgets.Layout(width = "8%"))
upload_bathy_name = widgets.Text(layout=widgets.Layout(width = "20%")) # name of uploaded bathy


parameter_options = ('Select Parameter','THL','DX')  
parameter_list = widgets.Dropdown(options = parameter_options,layout=widgets.Layout(width = "20%"))

THL = widgets.BoundedFloatText(description='THL',min = '10',value='200',max='1500000',step='0.01')    # total horizontal length
THL_box = widgets.HBox([THL],layout=widgets.Layout(width = "25%"))

dom = widgets.BoundedFloatText(description='DX',min = '0.0',value='1',max='100',step='0.1')   # Dx spacing
dom_box = widgets.HBox([dom],layout=widgets.Layout(width = "25%"))

file_name_box = widgets.HBox([bathy_name,upload_bathy_name,space_box2,parameter_list,THL_box,dom_box],
                          layout=widgets.Layout(height ='75px',width = "90%"))

Box_upload = widgets.VBox([label_intro1,space_box2,file_name_box],
                          layout=widgets.Layout(height ='500px'))

######################################
### Option #1b: Slope Bathy Gen ######
######################################

## Un-edited Variables (this could be added as a changeable feature in the future)
NumSeg = 2

# label intro
label_intro2 = widgets.HTML("""This option plots and saves a simple one-dimensional <b>slope</b>
bathymetry consisting of 2 segments and 3 vertices. The user can select the <b>total horizontal lenght</b> 
of the bathymetry <b>(THL)</b>, the discretization (horizontal spatial step size)  <b>(DX)</b>,
and the <b>elevation</b> with the  <b>location</b> of the vertices. Once the desired bathymetry is plotted,
press the <b>Assemble Bathymetry File</b>
button and proceed to Step #2.<br>The values are in <b>metric</b> units.""",
                           layout=widgets.Layout(width='90%'))

# domain discretization widgets

domain_box = widgets.HBox([THL,dom],layout=widgets.Layout(align_items='center',width = '90%',height ='40px'))

# label with elevation NOTE
label_NOTE = widgets.HTML("""<b>NOTE:</b> Depth values are [-] for underwater (below mean water level).""")

## vertex elevation and location floatsliders:
# vertex 1 
v1_label = widgets.HTML("<b>Vertex #1<b/>")
MWL = widgets.FloatSlider(description='Elevation ',min=-10, max=15,value = -10,
                    step='0.01',layout = widgets.Layout(width='100%',height = '50px')) #V1 elev = mean water level
label_v1_loc = widgets.HTML("""Located at <b>0.0 meters</b>.""")     # vert1 loc = 0.0m
v1_box = widgets.VBox([v1_label,MWL,label_v1_loc],layout=widgets.Layout(display='flex-grow',
                    align_items='center',
                    width='30%',
                    border='solid 2px grey'))

# vertex 2
v2_label = widgets.HTML("<b>Vertex #2<b/>")
vert2_loc = widgets.FloatSlider(max=THL.value, min=0,value=10,
                    step='0.01',layout=MWL.layout,   
                    description = 'Location')
# link THL value to vertex 2 location
widgets.jsdlink((THL,'value'),(vert2_loc,'max'))

vert2_elev = widgets.FloatSlider(min=MWL.value, max=15,value = MWL.value,
                    step='0.01', layout=MWL.layout,
                    description = 'Elevation ')  

v2_box = widgets.VBox([v2_label,vert2_elev,vert2_loc],layout=v1_box.layout)

# vertex 3
v3_label = widgets.HTML("<b>Vertex #3<b/>")
vert3_elev = widgets.FloatSlider(min=MWL.value, max=15,value = MWL.value,
                    step='0.01', layout=MWL.layout,
                    description = 'Elevation')
label_v3_loc = widgets.HTML("""Located at <b>THL</b> distance.""")  # vert3 loc = THL
v3_box = widgets.VBox([v3_label,vert3_elev,label_v3_loc],layout=v1_box.layout)


VERT_box = widgets.HBox([v1_box,v2_box,v3_box])

# slope container box
Box_SlopeBathy = widgets.VBox(children=[label_intro2,space_box,domain_box,space_box,
                                        label_NOTE,VERT_box,space_box])

######################################
### Option #1c: Flat Bathy Gen ######
######################################

# label intro
label_intro3 = widgets.HTML("""This option plots and saves a simple one-dimensional <b>flat</b>
bathymetry with a constant depth. The user can select the <b>total horizontal lenght</b> 
of the bathymetry <b>(THL)</b>, the <b>spacing</b> between the points <b>(DX)</b>,
and the <b>Depth</b>. Once the desired bathymetry is plotted,
press the <b>Assemble Bathymetry File</b>
button and proceed to Step #2.<br>The values are in <b>metric</b> units.""",
                           layout=widgets.Layout(width='90%'))

# slope container box
Box_FlatBathy = widgets.VBox(children=[label_intro3,space_box,domain_box,space_box,MWL,space_box,
                                        label_NOTE,space_box])


# box that shows the "chosen bathy type" widgets
# the function that shows/hides this container is at wavemaker_Function.py
bathy_option_box = widgets.VBox([Box_upload,Box_SlopeBathy,Box_FlatBathy],layout=widgets.Layout(height ='420px'))

#  Plot and Save buttons widgets
plot_button = widgets.Button(description="Plot Bathymetry", layout=widgets.Layout(width='40%',height='40px'))

# arrow image that points "button use flow"
file = open("media/arrow.png", "rb")
image = file.read()
arrow  = widgets.Image(value=image,format='png',width=90,height=10)

#  Plot and Save button widget
save_button = widgets.Button(description="Assemble Bathymetry File",
                             layout=widgets.Layout(width = '40%',height = '40px'))

# HBox for plot and save buttons
plotSaveHBox = widgets.HBox([plot_button,arrow, save_button],layout=widgets.Layout(width='90%')) 


# Bathymetry tab
page_BATHY = widgets.VBox([bathy_list_container,bathy_option_box,plotSaveHBox],
                          layout=widgets.Layout(height ='550px'))

