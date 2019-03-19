

from forcedmut_duos_fatherDaughter_X import *
from forcedmut_duos_motherDaughter_X import *
from forcedmut_trios_daughter_X import *
from fromfile_duos_fatherDaughter_X import *
from fromfile_duos_motherDaughter_X import *
from fromfile_trios_X_daughter import *

import tkinter as tk
from tkinter import filedialog
import os
import random as rd
rd.seed(5853712)



root = tk.Tk()
root.withdraw()
WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(),"Markers"),title='Please select a directory')

WorkDirList=os.listdir(WorkingDir)

tmpList=[x for x in WorkDirList if '.txt' in x]
finalList=[x for x in tmpList if 'mutationrate' not in x]

NumbSymulations = 10**2
NumbMutations = 1
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_FatherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Duos_MotherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Trios_Daughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Duos_FatherDaughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Duos_MotherDaughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Trios_Daughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))

NumbMutations = 2
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_FatherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Duos_MotherDaughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Trios_Daughter_X(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Duos_FatherDaughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Duos_MotherDaughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    FromFile_Trios_Daughter_X(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))