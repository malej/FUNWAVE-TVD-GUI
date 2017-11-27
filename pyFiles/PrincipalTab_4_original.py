import ipywidgets as widgets
from traitlets import link


#######################################
#### Principal Tab 4: Run Funwave  ####
#######################################

#intro label
runFUNWAVE_label = widgets.Label('Press Button to Run FUNWAVE Model.',layout = widgets.Layout(height = '90px'))

# run funwave button
RunFunwave_button = widgets.Button(description="Run FUNWAVE Model",                           
                             layout = widgets.Layout(width = '80%',height = '45px'))
# column 1: run funwave buttom
fun_cont = widgets.HBox(children = [RunFunwave_button],
                       layout = widgets.Layout(width = '50%',height = '150px'))                    

# run funwave load progress bar 
Prog_label = widgets.Label('Model Progress:',layout = widgets.Layout(width = '12%'))
RunFunwave_load = widgets.FloatProgress(value=0.0,min=5.0,max=10.0,step=0.1,
                                        layout = widgets.Layout(width = '88%',height = '35px'))
Load_cont = widgets.HBox([Prog_label,RunFunwave_load],layout = widgets.Layout(width = '90%',height = '137px'))

# create run_funwave tab
RUNfunwave_tabs = widgets.VBox(children=[runFUNWAVE_label,fun_cont,Load_cont],
                              layout=widgets.Layout(height ='530px'))