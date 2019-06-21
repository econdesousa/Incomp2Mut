import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import math
from collections import Counter


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


#dirList = getDirNames()


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





def ReadVecData_v2(f):  # data is composed by 16 cols: 8 vectors of type [d2F d2M]
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []
    x5 = []
    y5 = []
    x6 = []
    y6 = []
    x7 = []
    y7 = []
    x8 = []
    y8 = []
    iteration = []
    it = 0
    data = open(f, 'r')
    header = 1
    for line in data:
        if it >= header:
            p = line.split(sep="\t")
            x1.append(p[0])
            y1.append(p[1])
            x2.append(p[2])
            y2.append(p[3])
            x3.append(p[4])
            y3.append(p[5])
            x4.append(p[6])
            y4.append(p[7])
            x5.append(p[8])
            y5.append(p[9])
            x6.append(p[10])
            y6.append(p[11])
            x7.append(p[12])
            y7.append(p[13])
            x8.append(p[14])
            y8.append(p[15])
            iteration.append(p[16])
        it += 1


    return x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8



def ReadVecData_v3(f):  # data is composed by 16 cols: 8 vectors of type [d2F d2M]
    out = []
    it = 0
    data = open(f, 'r')
    header = 1
    for line in data:
        if it >= header:
            P = line.split(sep="\t")
            x1 = float(P[0])
            y1 = float(P[1])
            x2 = float(P[2])
            y2 = float(P[3])
            x3 = float(P[4])
            y3 = float(P[5])
            x4 = float(P[6])
            y4 = float(P[7])
            x5 = float(P[8])
            y5 = float(P[9])
            x6 = float(P[10])
            y6 = float(P[11])
            x7 = float(P[12])
            y7 = float(P[13])
            x8 = float(P[14])
            y8 = float(P[15])
            if math.isnan(x1): x1=0
            if math.isnan(x2): x2=0
            if math.isnan(x3): x3=0
            if math.isnan(x4): x4=0
            if math.isnan(x5): x5=0
            if math.isnan(x6): x6=0
            if math.isnan(x7): x7=0
            if math.isnan(x8): x8=0
            if math.isnan(y1): y1=0
            if math.isnan(y2): y2=0
            if math.isnan(y3): y3=0
            if math.isnan(y4): y4=0
            if math.isnan(y5): y5=0
            if math.isnan(y6): y6=0
            if math.isnan(y7): y7=0
            if math.isnan(y8): y8=0
            vecFather=[x1, x2, x3, x4, x5, x6, x7, x8]
            if all([math.isinf(x) for x in vecFather]):
                x1 = 0; x2 = 0; x3 = 0; x4 = 0; x5 = 0; x6 = 0; x7 = 0; x8 = 0

            vecMother=[y1, y2, y3, y4, y5, y6, y7, y8]
            if all([math.isinf(x) for x in vecMother]):
                y1 = 0; y2 = 0; y3 = 0; y4 = 0; y5 = 0; y6 = 0; y7 = 0; y8 = 0

            vec=[x1+y1,x2+y2,x3+y3,x4+y4,x5+y5,x6+y6,x7+y7,x8+y8]
            vecstr=['-'.join([str(x1),str(y1)]),
                    '-'.join([str(x2), str(y2)]),
                    '-'.join([str(x3), str(y3)]),
                    '-'.join([str(x4), str(y4)]),
                    '-'.join([str(x5), str(y5)]),
                    '-'.join([str(x6), str(y6)]),
                    '-'.join([str(x7), str(y7)]),
                    '-'.join([str(x8), str(y8)])]
            matches = [ x for x in range(len( vec )) if abs( vec[x] - min(vec)) < 0.00001 ]
            out.append('/'.join( [vecstr[index] for index in matches]))
        it += 1
    return out





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



def exportReport_v2(outFileName, inFileName, out):
    #outFileName: path to file to be edited
    #inFileName: name to append to data
    #out data to export
    print(outFileName)
    # sort data to avoid having e.g. [0,1] and [1,0] that is equivalent -> 1 mutation step

    # count unique rows of matrix out
    # first: remove duplication '1.0-0.0/1.0-0.0/0.0-1.0' will become '1.0-0.0/0.0-1.0'
    removeDups=[]
    for x in out:
        removeDups.append("/".join(set(x.split(sep="/"))))

    c = Counter(removeDups)  # get frequencies of data
    d = c.most_common()


    tmp = inFileName.split(sep=".txt")
    inFileName = tmp[0]
    fid = open(outFileName, 'a')
    for x in d:
        print(inFileName, x[0],x[1], sep="\t", file=fid)
        inFileName = ""

    fid.close()




def main(WorkingDir, resultFolderName="compiledResults"):
    finalList = getFileNames()
    print("finalList :" , finalList)
    pDir=WorkingDir
    #pDir = os.path.abspath(os.path.join(WorkingDir, os.pardir))
    pDir = os.path.join(pDir, resultFolderName)
    if not os.path.exists(pDir):
        os.makedirs(pDir)
    else:
        files = [f for f in os.listdir(pDir) if os.path.isfile(os.path.join(pDir,f))]
        for f in files:
            print(os.path.join(pDir, f))
            os.remove(os.path.join(pDir, f))

    for f in finalList:
        print("f :", f)


        tmp = f.split(sep=os.sep)
        inDir = os.path.dirname(f)
        outFileName = os.path.join(pDir, tmp[-2] + ".tsv")

        out = ReadVecData_v3(f)
        exportReport_v2(outFileName, tmp[-1], out)

"""
f='D:/Dropbox/Post-Doc/Colaboracoes/Nadia_Simulations/SofiaAntaoSousa/Incomp2Mut_home/src/Markers/artificiais/ForcedMut_Duos_FatherDaughter_X_nMut_1_1/dist_bimodal_ForcedMut_Duos_FatherDaughter_X_nMut_1_1_vecFatherMother.txt'
f=open(f,mode="r")
x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = ReadVecData(f)
for i in range(len(x1)):
    print([[x1,y1], [x2,y2], [x3,y3], [x4,y4], [x5,y5], [x6,y6], [x7,y7], [x8,y8]])
"""

main(WorkingDir)