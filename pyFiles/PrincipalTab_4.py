import ipywidgets as widgets
from traitlets import link


#######################################
#### Principal Tab 4: Run Funwave  ####
#######################################

space_box = widgets.Box(layout=widgets.Layout(height ='25px')) # box created to have space between widgets

# funwave executable options dropdown widgets
label_intro = widgets.HTML("""Specify your FUNWAVE Executable:""",
                           layout = widgets.Layout(height = '25px'))
exec_options = ["Specify Executable", "FUNWAVE HPC Topaz", "FUNWAVE CCE", "Gaby's Mac", "Matt's Mac"]  
exec_list = widgets.Dropdown(options = exec_options,layout = widgets.Layout(height = '40px',width = '90%'))

# column 1: funwave exec list container
exec_list_container = widgets.VBox([label_intro,exec_list],
                                   layout = widgets.Layout(width = '45%'))

# run funwave button label
runFUNWAVE_label = widgets.HTML('Press Button to Run FUNWAVE Model.',
                         layout = widgets.Layout(height = '25px'))

# run funwave button
RunFunwave_button = widgets.Button(description="Run FUNWAVE Model",                           
                             layout = widgets.Layout(height = '40px',width = '90%'))

# column 2: run funwave button container
RunFunwave_button_cont = widgets.VBox(children = [runFUNWAVE_label, RunFunwave_button],
                       layout = widgets.Layout(width = '45%'))    

# Column 1 & column 2 container
fun_cont = widgets.HBox(children = [exec_list_container,RunFunwave_button_cont],
                        layout = widgets.Layout(height = '150px'))

# run funwave load progress bar 
Prog_label = widgets.HTML('Model Progress:',layout = widgets.Layout(width = '10%'))
RunFunwave_load = widgets.FloatProgress(value=0.0,min=5.0,max=10.0,step=0.1,
                                        layout = widgets.Layout(width = '90%',height = '35px'))
Load_cont = widgets.HBox([Prog_label,RunFunwave_load],layout = widgets.Layout(width = '90%',height = '137px'))

# create run_funwave tab
RUNfunwave_tabs = widgets.VBox(children=[space_box,fun_cont,Load_cont],
                              layout=widgets.Layout(height ='550px'))
