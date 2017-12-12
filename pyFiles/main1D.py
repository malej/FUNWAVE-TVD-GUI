##### %matplotlib inline
#%matplotlib notebook
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# import project title and generate project button from PRINCIPAL_TAB 
# once the button is pressed, the entire GUI will appear
# the function that does this is located at wavemaker_Function.py
from pyFiles.PRINCIPAL_TAB import container_title,space_box2, project_button

display(space_box2,container_title,space_box2) # display project text box and button

############################        
#### Activate Functions ####
############################

from pyFiles.wavemaker_Function import project_clicked # import generate project project fucntions

from pyFiles.bathymetry_Functions import compute_high_difference, on_save_clicked, on_plot_clicked
# ^ import generate bathymetry functions


from pyFiles.input_Functions import update_input_function # activate update input values button
from pyFiles.input_Functions import boolean_function # activate generate input file button

# activate the output variables (located in PrincipalTab_3) that will be shown the post-process list:
from pyFiles.output_functions import toggle_output_ETA
from pyFiles.output_functions import toggle_output_Hmax
from pyFiles.output_functions import toggle_output_Hmin
from pyFiles.output_functions import toggle_output_ETAmean
from pyFiles.output_functions import toggle_choose_output


from pyFiles.video_Functions import runVID_function,save_plot_clicked, plot_output_clicked
# ^ activate post processing buttons

from pyFiles.funwave_Functions import runFUN_function # activate run funwave button
