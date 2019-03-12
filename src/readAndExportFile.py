import tkinter as tk
from tkinter import filedialog
import os


def outFileName(save2File,DIR="output"):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    inDir = os.path.dirname(file_path)
    baseName=os.path.basename(file_path)
    outDir = os.path.join(inDir, DIR)
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    outFile1 = os.path.join(outDir,baseName+"_stats.txt")
    outFile2 = os.path.join(outDir,baseName+"_vecFatherMother.txt")
    outFile3 = os.path.join(outDir,baseName+"_Pedigrees.txt")


    return file_path, outFile1, outFile2, outFile3

def Read_Two_Column_File(file_name, header=1, normalize=True):
    with open(file_name, 'r') as data:
        x = []
        y = []
        it = 0
        for line in data:
            if it >= header:
                p = line.split()
                x.append(float(p[0].replace('"', '')))
                y.append(float(p[1]))
            it += 1

    if normalize:
        y = [float(i)/sum(y) for i in y]



    return x, y


def ReadMutRate(file_name,header=1):
    with open(file_name, 'r') as f:
        it=0
        for line in f:
            if it >= header:
                p = line.split()
                incomprate = float(p[0])
                stepMut = float(p[1])
            it +=1
    return incomprate, stepMut



def exportOutTable(outFile,father, mother, child, mutation_step, index, output, display=True,save2file=True, iteration=0):
    if save2file:
        with open(outFile, 'a') as f:
            if iteration>0:
                print(iteration,"   father       mother\n          child", file=f)
            else:
                print("   father       mother\n          child", file=f)
            print(father, mother, "\n     ", child, "\n     ", output,  mutation_step, index, "\n", file=f)

    if display:
        print("   father       mother\n          child")
        print(father, mother, "\n     ", child, "\n     ", output, mutation_step, index, "\n")

