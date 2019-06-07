#!/usr/bin/env python

# Benerman's Resolve Script

# import DaVinciResolveScript
from resolve_class_build import R
import sys
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

root = tk.Tk()
root.withdraw()


### Create and Name Project
def create_project():
    global project_name
    project_name = simpledialog.askstring("Input", "Please name the Project?",
                                    parent=root)
    if project_name is not None:
	    print(f"Project name is: {project_name}")
    else:
        print("Error: Project name not set.\n\nScript is now exiting")
        sys.exit()

    if R.SetProjectName(project_name):
        print(f'Project {project_name} created successfully')
    else:
        print('Error: Failed to create project\nProject already potentially exists or dialog box is preventing script from continuing')
        create_project()

create_project()

##	Set Project Settings
#	Choose between 4k and 2k
#	Choose between 23.976p, 29.97p, 60p

### Create Folder Structure
##	'Master'(Root)
##	'Video', 'Audio', 'Stills', 'Exports', 'Projects'
##	'Video' > 'Raw', 'Converted'
##	'Audio' > 'Raw', 'Tracks', 'Foley'
##	'Stills' > 'Raw', 'Proofs'


### Import Media(Different Types)
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

# Ask the user to select a one or more file names.
# answer = tk.filedialog.askopenfilenames(parent=root,
#                                      initialdir=os.getcwd(),
#                                      title="Please select one or more files:",
#                                      filetypes=my_filetypes)



	

mediaPath = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
if mediaPath:
	print(f'Media will be imported from: {mediaPath}')
else:
	print('Error: No file path selected for file import')

### Create Timelines
#	'All Clips' and 'Final'

##	Add All Clips to 'All Clips Timeline'


