import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



root = tk.Tk()
root.withdraw()
WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(), "Markers"), title='Please select a directory')

def getDirNames():
    dirList = []
    for dirname, dirnames, filenames in os.walk(WorkingDir):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            if 'ForcedMu' in subdirname:
                dirList.append(os.path.join(dirname, subdirname))
            elif 'FromFile' in subdirname:
                dirList.append(os.path.join(dirname, subdirname))

    return dirList


dirList = getDirNames()


def getFileNames():
    dirList = getDirNames()
    finalList = []
    for dirNameIter in dirList:
        fList = os.listdir(dirNameIter)
        tmpList = [x for x in fList if 'vecFatherMother.txt' in x]
        for f in tmpList:
            finalList.append(os.path.join(dirNameIter, f))

    return finalList


def getWorkingCase(d2Fset, d2Mset):
    if d2Fset == set(['0']):
        if d2Mset == set(['0']):
            exit("no info available")
        else:
            WorkingCase = 3
    elif d2Mset == set(['0']):
        if d2Fset == set(['0']):
            exit("no info available")
        else:
            WorkingCase = 2
    else:
        WorkingCase = 1

    return WorkingCase


def ReadVecData(f):
    d2F = []
    d2M = []
    iteration = []
    it = 0
    data = open(f, 'r')
    header = 1
    for line in data:
        if it >= header:
            p = line.split()
            d2F.append(p[0])
            d2M.append(p[1])
            iteration.append(p[2])
        it += 1
        d2Fset = set(d2F)
        d2Mset = set(d2M)

    return d2F, d2M, d2Fset, d2Mset


def exportReport(outFileName, inFileName, d2F, d2M):
    #outFileName: path to file to be edited
    #inFileName: name to append to data
    #d2M and d2F data to use in computations
    print(outFileName)
    # sort data to avoid having e.g. [0,1] and [1,0] that is equivalent -> 1 mutation step
    for i in range(len(d2F)):
        if d2M[i] < d2F[i]:
            tmpvar = d2M[i]
            d2M[i] = d2F[i]
            d2F[i] = tmpvar
    #count unique rows of matrix [d2F,d2M]
    matrixOut = np.array([[float(x) for x in d2F], [float(x) for x in d2M]])
    matrixOut = np.transpose(matrixOut)
    [unique_rows, cnt] = np.unique(matrixOut, axis=0, return_counts=True)

    tmp=inFileName.split(sep=".txt")
    inFileName=tmp[0]
    fid = open(outFileName,'a')
    index=[]
    for i in range(len(cnt)):
        index.append('['+str(unique_rows[i, 0])+' , '+str(unique_rows[i, 1])+']')
        print(inFileName, "\t", unique_rows[i, 0], "\t", unique_rows[i, 1], "\t", cnt[i], file=fid)
        inFileName = ""

    #df = pd.DataFrame({'cnt':cnt},index=index)
    #ax = df.plot.bar(rot=0)
    #outDir = os.path.dirname(outFileName)
    #with PdfPages(os.path.join(outDir,tmp[0]+'.pdf')) as pdf:
    #    pdf.savefig()

    fid.close()


def main(WorkingDir, resultFolderName="compiledResults"):
    finalList = getFileNames()
    pDir = os.path.abspath(os.path.join(WorkingDir, os.pardir))
    pDir = os.path.join(pDir, resultFolderName);
    print("outDIR = ", pDir)
    if not os.path.exists(pDir):
        os.makedirs(pDir)
    else:
        files = [f for f in os.listdir(pDir) if os.path.isfile(os.path.join(pDir,f))]
        for f in files:
            print(os.path.join(pDir, f))
            os.remove(os.path.join(pDir, f))

    for f in finalList:
        tmp = f.split(sep=os.sep)
        inDir = os.path.dirname(f)
        outFileName = os.path.join(pDir, tmp[-2] + ".txt")

        d2F, d2M, d2Fset, d2Mset = ReadVecData(f)
        # PossibleCases = { "trios" : 1, "Duos Father": 2, "Duos Mother": 3}
        # WorkingCase = getWorkingCase(d2Fset,d2Mset)
        # print("file =" , f,"\tWorkingCase =",WorkingCase)

        exportReport(outFileName, tmp[-1], d2F, d2M)


main(WorkingDir)
