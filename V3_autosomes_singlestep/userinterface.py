from fileinput import filename
import tkinter as tk
from tkinter import LEFT, Radiobutton, IntVar, X, Button, Frame, StringVar
from tkinter import W, filedialog, messagebox
import os
#from turtle import done
import random as rd



def GUI_setup( Message = "", type_of_model = "Duos", incomp_rate = "0.001", num_sim = "100,000",rs = "7068971"):
    """setup configurations"""

    # split into vertical frames 
    #   1: text: description of what user is supposed to do
    #   2: options : Select between Duos or Trios 
    #   3: Incompatibility rate
    #   4: Number of Simulations
    #   5: OK button
    #   6: random seed
    

    window = tk.Tk()
    window.attributes('-topmost', True) # always on top
    window.eval('tk::PlaceWindow . center') # center window

    # window title
    window.title("Configure")
    #window.geometry("400x400")

    # define groups vertical layout
    descriptionFrame = Frame(window)
    descriptionFrame.pack(side = "top")
    optionFrame = Frame(window)
    optionFrame.pack(side ="top")
    numMutFrame = Frame(window)
    numMutFrame.pack(side ="top")
    incompatibilityFrame = Frame(window)
    incompatibilityFrame.pack(side = "top")
    numSimFrame = Frame(window)
    numSimFrame.pack(side = "top")
    randomFrame = Frame(window)
    randomFrame.pack(side = "top")
    okFrame = Frame(window)
    okFrame.pack(side = "top")


    # create groups
    # 1:text
    if not Message:
        Message = "\nSetup configurations\nand press OK!\n"
        col = "black"
    else:
        col = "red"
    l1 = tk.Label(descriptionFrame, text=Message,font=("Helvetica", 15, "bold"),fg = col)
    l1.pack()


    # 2:options
    # Tkinter variable to store option
    if type_of_model == "Duos":
        v = IntVar(window, 1)
    else:
        v = IntVar(window, 2)               
    # Dictionary to create multiple buttons
    values = {"Duos    " : "1", "Trios   " : "2"}
    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(optionFrame, text = text, variable = v,
                    value = value, font=("Helvetica", 12, "bold"),
                    indicator = 1,
                    fg = "green",
                    ).pack(side="left" ,fill = X)
    
    # 3:incompatibility rate
    l4 = tk.Label(incompatibilityFrame, text="\nIncompatibility rate\t\n",font=("Helvetica", 12, "bold"), justify = "left")
    l4.pack(side="left")
    incomp = StringVar(window, incomp_rate)
    e4 = tk.Entry(incompatibilityFrame, textvariable = incomp, width = 30,font=("Helvetica", 12, "bold"),justify="left",fg="green")
    e4.pack(side="left")

    # 4:number of simulations
    l5 = tk.Label(numSimFrame, text="\nNumber of simulations\t\n",font=("Helvetica", 12, "bold"), justify = "left")
    l5.pack(side="left")
    numSim = StringVar(window, num_sim)
    e5 = tk.Entry(numSimFrame, textvariable = numSim, width = 30,font=("Helvetica", 12, "bold"),justify="left",fg="green")
    e5.pack(side="left")
    
    # 5: OK button
    if col == "black": # if Message was unset (i.e. first time) col is defined as black, otherwise it is red
        OKbuttonStr = "OK!"
    else:
        OKbuttonStr = "Continue with these settings"
    b1 = Button(okFrame, text = OKbuttonStr, font=("Helvetica", 15, "bold"),bg="blue",fg="white",command=window.destroy).pack()
    
    # 6: random seed
    l6 = tk.Label(randomFrame, text="\nRandom Seed\t\t\n",font=("Helvetica", 12, "bold"), justify = "left")
    l6.pack(side="left")
    rSeed = StringVar(window, rs)
    e6 = tk.Entry(randomFrame, textvariable = rSeed, width = 30,font=("Helvetica", 12, "bold"),justify="left",fg="green")
    e6.pack(side="left")

    # create window
    # window can be closed by clicking the X button or pressing the EXIT button
    # value will be retrieved from the dictionary and stored in the variable v
    window.mainloop()
    if v.get() == 1:
        return "Duos" , eval(incomp.get()), int(eval(numSim.get().replace(',', ' ').replace(' ' , ''))) , int(eval(rSeed.get()))
    else:
        return "Trios", eval(incomp.get()), int(eval(numSim.get().replace(',', ' ').replace(' ' , ''))) , int(eval(rSeed.get()))


def GUI_file_selector():
    """Select markers file"""

    root = tk.Tk()
    root.withdraw()

    # define WorkingDir as folder containing this script
    WorkingDir = os.path.dirname(__file__)
    # and check if Markers folder exists
    MarkersDir = os.path.join(WorkingDir, "Markers")
    # if so, use it as default
    if os.path.exists(MarkersDir):
        WorkingDir = MarkersDir
    # either way, ask user if the currently selected folder is the right one 
    markersFileName = filedialog.askopenfilename(initialdir=WorkingDir,title='Please select a file')

    return markersFileName


# create a DONE! window
def GUI_done(Message = "DONE!"):
    """create a DONE! window"""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo( "...", "DONE!")


if __name__ == "__main__":
    # test
    GUI_setup()
    GUI_file_selector()
    GUI_done()