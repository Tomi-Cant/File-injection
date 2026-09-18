import subprocess
from tkinter import filedialog, messagebox
from os.path import dirname,abspath

def get_destination()-> str:
    title= "Select {AppName} folder... "
    folder_path = filedialog.askdirectory(title=title)
    return folder_path
def get_path()-> str:
    path=dirname(abspath(__file__))+ "\\assets"
    return  path 

cmd = ["robocopy", get_path(),get_destination(), '/s']
subprocess.run(cmd)
messagebox.showwarning("Restart {AppName}","You will need to restart {AppName} by saving and closing. Only AFTER will the additional features be implemented.")