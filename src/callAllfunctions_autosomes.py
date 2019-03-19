

from forcedmut_duos_aut import *
from forcedmut_trios_aut import *
from fromfile_duos_aut import *
from fromfile_trios_aut import *

import tkinter as tk
from tkinter import filedialog
import time
import os
import random as rd
rd.seed(7068971)

root = tk.Tk()
root.withdraw()
WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(),"Markers"),title='Please select a directory')

WorkDirList=os.listdir(WorkingDir)

tmpList=[x for x in WorkDirList if '.txt' in x]
finalList=[x for x in tmpList if 'mutationrate' not in x]

start_time = time.time()
NumbSymulations = 10**6
NumbMutations = 1
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_Aut(PATH=file2Work, nMut=NumbMutations, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    ForcedMut_Trios_Aut(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    FromFile_Duos_Aut(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    FromFile_Trios_Aut(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))

NumbMutations = 2
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    print("--- %s seconds ---" % (time.time() - start_time))
    ForcedMut_Duos_Aut(PATH=file2Work, nMut=NumbMutations, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    ForcedMut_Trios_Aut(PATH=file2Work,nMut=NumbMutations,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    FromFile_Duos_Aut(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    FromFile_Trios_Aut(PATH=file2Work,nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
