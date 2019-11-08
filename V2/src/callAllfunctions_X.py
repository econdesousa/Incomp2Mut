from forcedmut_duos_fatherDaughter_X import *
from forcedmut_duos_motherDaughter_X import *
from forcedmut_trios_daughter_X import *
from forcedmut_duos_motherSon_X import *

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

NumbSymulations = 1000 # 10**6

NumbMutationsMale = 1
NumbMutationsFemale = 1
RandomThresh=0  # 0: all muts on Male
                # 1: all muts on Female
                # 0<RandomThresh<1: muts randomly distributed
                # >1: force muts in both parents

for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_FatherDaughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=3,seed=int(rd.uniform(0,1)*10000000))
    #ForcedMut_Duos_MotherDaughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    #ForcedMut_Duos_MotherDaughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    #ForcedMut_Duos_MotherSon_X(PATH=file2Work, nMutFemale=NumbMutationsFemale, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    #ForcedMut_Trios_Daughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))


NumbMutationsMale = 2
NumbMutationsFemale = 2
RandomThresh=0  # 0: all muts on Male
                # 1: all muts on Female
                # 0<RandomThresh<1: muts randomly distributed
                # >1: force muts in both parents
'''
for fileName in finalList:
    file2Work=os.path.join(WorkingDir,fileName)
    ForcedMut_Duos_FatherDaughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Duos_MotherDaughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Duos_MotherSon_X(PATH=file2Work, nMutFemale=NumbMutationsFemale, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))
    ForcedMut_Trios_Daughter_X(PATH=file2Work, nMutMale=NumbMutationsMale, nMutFemale=NumbMutationsFemale, rThresh=RandomThresh, nSim=NumbSymulations,seed=int(rd.uniform(0,1)*10000000))

'''