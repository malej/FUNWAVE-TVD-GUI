import io
import base64
import os
import subprocess
import ipywidgets as widgets

# import pertaining variables:
from pyFiles.PRINCIPAL_TAB import title_text
from pyFiles.PrincipalTab_2 import processors_text, time_text #,output_text # output directory & number of processors
from pyFiles.PrincipalTab_4 import RunFunwave_load                          # funwave progress load bar

originalSize = 0.0

def runFunLoad(logFolder):             # loading bar function
    
    filename = os.path.join(logFolder,'LOG.txt')

    total_time = time_text.value      # total time of model (which is given by the user)
    RunFunwave_load.min = 0.0         # min value in progress bar = 0.0
    RunFunwave_load.max = total_time  # max value in progress bar = total time of model

    originalSize = 0.0                # original size of log.txt = 0
    actual_time = 0.0                 # initial actual time of model = 0
    RunFunwave_load.value = 0.0
    RunFunwave_load.description = "%4.2f / %4.2f" % (actual_time,total_time)
    
    while actual_time < total_time:
            fileStats=os.stat(filename)          
            fileSizeInBytes=fileStats.st_size     # check size in bytes of log.txt

            if fileSizeInBytes > originalSize:
                originalSize = fileSizeInBytes         
                lastLines = str(subprocess.check_output(['tail', '-3', filename]))    # take the final line in log.txt
                for line in lastLines.split("\n"):
                    if "TIME/TOTAL" in line:    
                        #test
                        #print('last line in question: ', line)
                        # test end
                        rowDataList = line.strip().split()                      # convert to list
                        time_total_index = rowDataList.index("TIME/TOTAL:")
                        actual_time = float(rowDataList[time_total_index + 1])    # actual_time's index is +1 after TIME/TOTAL's 
                        RunFunwave_load.value = actual_time                       # value of progress bar is actual_time
                        RunFunwave_load.description = "%4.2f / %4.2f" % (actual_time,total_time)


def runFUN_function(variable):
    """ this function runs the funwave model"""
    
    pwd = os.getcwd()  # get current path
    s = title_text.value # project title
    s = s.replace(" ", "_")
    folder_name = s.replace(".", "_") # substitute ' ' space and '.' in project title with '_'
    
    Depthtext = os.path.join(pwd,folder_name,'depth.txt') # path to depth.txt 
    check_dir_dep = os.path.exists(Depthtext) # check if depth.txt exist
    Input_text = os.path.join(pwd,folder_name,'input.txt') # path to input.txt 
    check_dir_input = os.path.exists(Depthtext) # check if input.txt exist
    
    if check_dir_dep == True and check_dir_input == True:         # if files exist...

        ### Uncomment if you want to run it on the hpc:
        #folder_dir = os.path.join(pwd,folder_name)    # directory where input.txt and depth.txt are located (project folder) 
        #EXEC = 'funwave_sgi'   # name of funwave executable
        #FUN = 'FUNWAVE-TVD'    # FUNWAVE program folder
        #BIN = 'bin'
        #HOME = os.environ['HOME']
        #fun_dir = os.path.join(HOME,FUN,BIN,EXEC) # path to FUNWAVE exec 
        #inputDir =  os.path.join(folder_dir,'input.txt')  # directory to input.txt 
        
        #os.chdir(folder_dir)                       # move to folder dir (NOT NEEDED)
        # run funwave terminal command:
        #run_fun = "cd %s && mpirun -n %d %s %s > LOG.txt &"%(folder_dir,processors_text.value,
        #                                                                    fun_dir,
        #                                                                   inputDir)
        
        ### To run in Gaby's Mac laptop
        folder_dir = os.path.join(pwd,folder_name)    # directory where input.txt and depth.txt are located (project folder) 
        EXEC = 'funwave_mac' # name of funwave executable
        FUN = 'FUNWAVE-TVD'    # FUNWAVE program folder
        BIN = 'bin'
        HOME = os.environ['HOME']
        fun_dir = os.path.join(HOME,FUN,BIN,EXEC) # path to FUNWAVE exec 
        inputDir =  os.path.join(folder_dir,'input.txt')  # directory to input.txt 
        
        os.chdir(folder_dir)                       # move to folder dir (NOT NEEDED)
        # run funwave terminal command:
        run_fun = "cd %s && /usr/local/Cellar/mpich/3.2_3/bin/mpirun -n %d %s %s > LOG.txt &"%(folder_dir,
                                                                            processors_text.value,
                                                                            fun_dir,
                                                                           inputDir)
        
        os.system(run_fun) # run funwave
        return_to_GUI_folder = os.path.join(folder_dir,'..')
        os.chdir(return_to_GUI_folder)  # return to GUI dir

        runFunLoad(folder_dir)
    else:
        warning = "You need to have a bathymetry and an input file before starting the simulation."
        raise Exception(warning)

    
    
###--------------------------------------------       
# activate functions
from pyFiles.PrincipalTab_4 import RunFunwave_button
RunFunwave_button.on_click(runFUN_function)        # activate run funwave button 




