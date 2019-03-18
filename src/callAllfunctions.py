

from forcedmut_duos_aut import *
from forcedmut_duos_fatherDaughter_X import *
from forcedmut_duos_motherDaughter_X import *
from forcedmut_duos_motherSon_X import *
from forcedmut_trios_aut import *
from forcedmut_trios_daughter_X import *
from fromfile_duos_aut import *
from fromfile_duos_fatherDaughter_X import *
from fromfile_duos_motherDaughter_X import *
from fromfile_duos_motherSon_X import *
from fromfile_trios_aut import *
from fromfile_trios_X_daughter import *

import tkinter as tk
from tkinter import filedialog
import os


root = tk.Tk()
root.withdraw()
WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(),"Markers"),title='Please select a directory')

WorkDirList=list=os.listdir(WorkingDir)

tmpList=[x for x in WorkDirList if '.txt' in x]
finalList=[x for x in tmpList if 'mutationrate' not in x]

NumbSymulations=10
NumbMutations=2
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_Aut(PATH=file2Work, nMut=NumbMutations, nSim=NumbSymulations)
    ForcedMut_Duos_FatherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations)
    ForcedMut_Duos_MotherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations)
    ForcedMut_Duos_MotherSon_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations)
    ForcedMut_Trios_Aut(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations)
    ForcedMut_Trios_Daughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations)
    FromFile_Duos_Aut(PATH=file2Work,nSim=NumbSymulations)
    FromFile_Duos_FatherDaughter_X(PATH=file2Work,nSim=NumbSymulations)
    FromFile_Duos_MotherDaughter_X(PATH=file2Work,nSim=NumbSymulations)
    FromFile_Duos_MotherSon_X(PATH=file2Work,nSim=NumbSymulations)
    FromFile_Trios_Aut(PATH=file2Work,nSim=NumbSymulations)
    FromFile_Trios_Daughter_X(PATH=file2Work,nSim=NumbSymulations)
