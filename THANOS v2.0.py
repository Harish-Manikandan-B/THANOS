import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font as tkFont
from cryptography.fernet import Fernet

##########################
##Create the root window##
##########################

window = Tk() 
window.title('THANOS')
window.geometry("500x500") 
window.config(background = "DODGER BLUE")

#######################
##ENCRYPTION FUNCTION##
#######################
    
def delete(fpath,fname):


    key=Fernet.generate_key()
    print(key)

    file=open('thanos_key.key','wb')
    file.write(key)
    file.close()

        #####KEY CREATION OVER###
    
    file = open('thanos_key.key','rb')
    key=file.read()
    file.close()

    os.chdir(fpath)

    input_file = fname
    output_file = input_file

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

    os.remove(fname)


def destroy_key():
    file = open('thanos_key.key','rb')
    key=file.read()
    file.close()

    os.chdir(fpath)

    input_file = "thanos_key.key"
    output_file = input_file

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    os.remove(thanos_key.key)

#####################################
##GUI TO SELECT A FILE FOR DELETION##
#####################################
        
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*"))) 

    path=filename
    print(path)
    head_tail= os.path.split(path)
    location=head_tail[0]  #stores the location or path of the file
    file_name=head_tail[1] #stores the file name seperated from the path
    print(location)
    print(file_name)

    for i in range(5):
        
        delete(location,file_name)
        
    destroy_key()
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename)

def directory():
    window.withdraw()
    folder_selected = filedialog.askdirectory()


label_file_explorer = Label(window,width = 100, height = 4, fg = "blue")  
																						    						  						
button_explore = Button(window,text = "BROWSE FILES",width = 12, height = 3,command = browseFiles) 
button_explore.place(x=50,y=120)
button_explore.width=100

button_explore = Button(window,text = "BROWSE DIRECTORY",width = 12, height = 3,command = directory) 
button_explore.place(x=170,y=120)
button_explore.width=100

button_exit = Button(window, text = "Exit",width = 12, height = 3,command = exit)
button_exit.place(x=290,y=120)
button_exit.width= 200

# Grid method is chosen for placing 
# the widgets at respective positions 
# in a table like structure by 
# specifying rows and columns 

text= Text(window)
text.place(x=0,y=240)
text.insert(INSERT,"This THANOS Version 2.0")
text.insert(INSERT,"select the files to be deleted and it will be deleted permenantly from your system")
text.insert(INSERT,"NOTE: The files are encrypted and cannot be retrieved from your system")
# Let the window wait for any events 
window.mainloop()
#os.system("pause")


####################################
	 AUTHOR - HARISH
####################################
