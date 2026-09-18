import subprocess
from tkinter import filedialog, messagebox
from os.path import dirname,abspath
import os

def get_destination(direct:bool =False)-> str:
    if direct:
        title= "Select {AppName} folder... "
        folder_path = filedialog.askdirectory(title=title)
    else:
        folder_path = os.path.join(os.environ["LOCALAPPDATA"], "AppName")
    return folder_path
def get_path()-> str:
    path=dirname(abspath(__file__))+ "\\assets"
    return  path 

cmd = ["robocopy", get_path(),get_destination(), '/s']
subprocess.run(cmd, stdout=subprocess.DEVNULL)
messagebox.showwarning("Restart {AppName}","You will need to restart {AppName} by saving and closing. Only AFTER will the additional features be implemented.")