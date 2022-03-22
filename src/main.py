from genFamilyAutossomes import mutationRate
from userinterface import GUI_setup
from userinterface import GUI_file_selector
from userinterface import GUI_done
from tkinter.filedialog import asksaveasfile
import os
from forcedmut_duos_aut import *
from forcedmut_trios_aut import *
from readAndExportFile import readCompiled00
from compileResults import main_compile
import shutil
import random as rd



def main():
    modelType , incomp , numSim , randomSeed = GUI_setup()
    markersFileName = ""
    if numSim > 100000:
        warningMessage="\nWARNING\nWith the current number of simulations, the code may take a while.\nDo you want to continue?\n"
        modelType , incomp , numSim , randomSeed = GUI_setup(warningMessage, modelType , incomp , '{:,}'.format(numSim).replace(',', ' '), randomSeed)
    
    while not markersFileName:
        markersFileName = GUI_file_selector()
    print(f"Marker File : {markersFileName}\nFamilial Configuration : {modelType}\nObserved Incompatibility Rate : {incomp}\nNumber of Simulations : {numSim}")
    tempOutFileName = os.path.join(os.path.dirname(markersFileName), os.path.splitext(os.path.basename(markersFileName))[0]+"_"+modelType+"_output.csv" )
    f = open(tempOutFileName, 'w')
    #f = asksaveasfile(mode='w', defaultextension=".csv",initialdir=os.path.dirname(markersFileName),
    #    initialfile=os.path.splitext(os.path.basename(markersFileName))[0]+"_"+modelType+"_output.csv")
    if f is None: # asksaveasfile return 'None' if dialog closed with "cancel".
        return

    rd.seed(randomSeed)
    WorkingDir = os.path.dirname(markersFileName)
    nMutMale = 1
    nMutFemale = 1
    if modelType == "Duos":
        ForcedMut_Duos_Aut(PATH=markersFileName, nMutMale=nMutMale, nMutFemale=nMutFemale, rThresh=0, nSim=numSim, seed=int(rd.uniform(0, 1)*10000000))
        resultsCompiledFileName = os.path.join(WorkingDir, "compiledResults", "ForcedMut_Duos_Aut_nMut_"+str(nMutMale)+"_"+str(nMutFemale)+".tsv")
        folder2remove = os.path.join(WorkingDir, "ForcedMut_Duos_Aut_nMut_"+str(nMutMale)+"_"+str(nMutFemale))
        renameOutputFileName = os.path.join(WorkingDir, os.path.splitext(os.path.basename(markersFileName))[0]+"_Duos_Aut_"+str(nMutMale)+"_"+str(numSim)+"_"+str(randomSeed)+".csv")
    else:
        ForcedMut_Trios_Aut(PATH=markersFileName, nMutMale=1, nMutFemale=1, rThresh=0, nSim=numSim, seed=int(rd.uniform(0, 1)*10000000))
        resultsCompiledFileName = os.path.join(WorkingDir, "compiledResults", "ForcedMut_Trios_Aut_nMut_"+str(nMutMale)+"_"+str(nMutFemale)+".tsv")
        folder2remove = os.path.join(WorkingDir, "ForcedMut_Trios_Aut_nMut_"+str(nMutMale)+"_"+str(nMutFemale))
        renameOutputFileName = os.path.join(WorkingDir, os.path.splitext(os.path.basename(markersFileName))[0]+"_Trios_Aut_"+str(nMutMale)+"_"+str(numSim)+"_"+str(randomSeed)+".csv")
        
    main_compile(WorkingDir)

    n00 = readCompiled00(resultsCompiledFileName)
    percentageHiddenMutations = ( float(n00)/float(numSim) ) * 100
    print(f"% of Hidden Mutations : {percentageHiddenMutations}%")
    mutRate = incomp / (1.0 - ( float(n00)/float(numSim)))
    print(f"Mutation Rate : { mutRate }")
    file_save(f,markersFileName,modelType,incomp,numSim,percentageHiddenMutations,mutRate)
    if os.path.exists(folder2remove):
        shutil.rmtree(folder2remove)
    if os.path.exists(os.path.join(WorkingDir, "compiledResults")):
        shutil.rmtree(os.path.join(WorkingDir, "compiledResults"))
    if os.path.exists(tempOutFileName):
        os.rename(tempOutFileName,renameOutputFileName)
    GUI_done(Message="Done!")


def file_save(f,markersFileName,modelType,incomp,numSim,percentageHiddenMutations,mutRate):
    text2save = f"Marker File,{markersFileName}\nFamilial Configuration,{modelType}\nObserved Incompatibility Rate,{incomp}\nNumber of Simulations,{numSim}\n% of Hidden Mutations,{percentageHiddenMutations}%\nMutation Rate,{mutRate}\n" 
    f.write(text2save)
    f.close() 

if __name__ == "__main__":
    main()



'''
# to create an exe file run the following command in the terminal
pyinstaller -F -n incomp2mut main.py
'''