from forcedmut_trios_aut import *
import tkinter as tk
from tkinter import filedialog
import os
import random as rd
rd.seed(7068971)

root = tk.Tk()
root.withdraw()
WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(), "Markers"), title='Please select a directory')

WorkDirList = os.listdir(WorkingDir)

tmpList = [x for x in WorkDirList if '.txt' in x]
finalList = [x for x in tmpList if 'mutationrate' not in x]

NumbSymulations = 10**5

NumbMutationsMale = 1
NumbMutationsFemale = 0
RandomThresh = 0  # 0: all muts on Male
                # 1: all muts on Female
                # 0<RandomThresh<1: muts randomly distributed
                # >1: force muts in both parents

for fileName in finalList:
    file2Work=os.path.join(WorkingDir, fileName)
    ForcedMut_Trios_Aut(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations, seed=int(rd.uniform(0, 1)*10000000))
