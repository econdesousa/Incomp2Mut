import math
import os
import tkinter as tk
from collections import Counter
from tkinter import filedialog


def getDirNames(WorkingDir):
    dirList = []
    for dirname, dirnames, filenames in os.walk(WorkingDir):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            if 'ForcedMu' in subdirname:
                dirList.append(os.path.join(dirname, subdirname))
            elif 'FromFile' in subdirname:
                dirList.append(os.path.join(dirname, subdirname))

    return dirList
# dirList = getDirNames()


def getFileNames(WorkingDir):
    dirList = getDirNames(WorkingDir)
    finalList = []
    for dirNameIter in dirList:
        fList = os.listdir(dirNameIter)
        tmpList = [x for x in fList if 'vecFatherMother.txt' in x]
        for f in tmpList:
            finalList.append(os.path.join(dirNameIter, f))

    return finalList


def getWorkingCase(d2Fset, d2Mset):
    if d2Fset == set():
        if d2Mset == set():
            exit("no info available")
        else:
            WorkingCase = 3
    elif d2Mset == set():
        if d2Fset == set():
            exit("no info available")
        else:
            WorkingCase = 2
    else:
        WorkingCase = 1

    return WorkingCase


def ReadVecData_v3(f):  # data is composed by 16 cols: 8 vectors of type [d2F d2M]
    out = []
    it = 0
    data = open(f, 'r')
    header = 1
    for iterator,line in enumerate(data):
        if not iterator % 1000:
            print("Compiling: ", iterator,end="\r")
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
            if math.isnan(x1): x1 = 0
            if math.isnan(x2): x2 = 0
            if math.isnan(x3): x3 = 0
            if math.isnan(x4): x4 = 0
            if math.isnan(x5): x5 = 0
            if math.isnan(x6): x6 = 0
            if math.isnan(x7): x7 = 0
            if math.isnan(x8): x8 = 0
            if math.isnan(y1): y1 = 0
            if math.isnan(y2): y2 = 0
            if math.isnan(y3): y3 = 0
            if math.isnan(y4): y4 = 0
            if math.isnan(y5): y5 = 0
            if math.isnan(y6): y6 = 0
            if math.isnan(y7): y7 = 0
            if math.isnan(y8): y8 = 0
            vecFather = [x1, x2, x3, x4, x5, x6, x7, x8]
            vecFather = [ round ( i , 1 ) for i in vecFather ]
            x1 = vecFather[0]
            x2 = vecFather[1]
            x3 = vecFather[2]
            x4 = vecFather[3]
            x5 = vecFather[4]
            x6 = vecFather[5]
            x7 = vecFather[6]
            x8 = vecFather[7]
            if all([math.isinf(x) for x in vecFather]):
                x1 = 0; x2 = 0; x3 = 0; x4 = 0; x5 = 0; x6 = 0; x7 = 0; x8 = 0
                vecFather = [x1, x2, x3, x4, x5, x6, x7, x8]

            for i in range(len(vecFather)):
                if math.isfinite(vecFather[i]):
                    if math.trunc(vecFather[i]) != vecFather[i]:
                        vecFather[i] = vecFather[i] + 10000

            vecMother = [y1, y2, y3, y4, y5, y6, y7, y8]
            vecMother = [round(i, 1) for i in vecMother]
            y1 = vecMother[0]
            y2 = vecMother[1]
            y3 = vecMother[2]
            y4 = vecMother[3]
            y5 = vecMother[4]
            y6 = vecMother[5]
            y7 = vecMother[6]
            y8 = vecMother[7]
            if all([math.isinf(x) for x in vecMother]):
                y1 = 0; y2 = 0; y3 = 0; y4 = 0; y5 = 0; y6 = 0; y7 = 0; y8 = 0
                vecMother = [y1, y2, y3, y4, y5, y6, y7, y8]


            for i in range(len(vecMother)):
                if math.isfinite(vecMother[i]):
                    if math.trunc(vecMother[i]) != vecMother[i]:
                        vecMother[i] = vecMother[i] + 10000

            vec = [x + y for x, y in zip(vecFather, vecMother)]

            vecstr=['-'.join([str(x1),str(y1)]),
                    '-'.join([str(x2), str(y2)]),
                    '-'.join([str(x3), str(y3)]),
                    '-'.join([str(x4), str(y4)]),
                    '-'.join([str(x5), str(y5)]),
                    '-'.join([str(x6), str(y6)]),
                    '-'.join([str(x7), str(y7)]),
                    '-'.join([str(x8), str(y8)])]
            matches = [x for x in range(len(vec)) if abs(vec[x] - min(vec)) < 0.00001]
            out.append('/'.join([vecstr[index] for index in matches]))
        it += 1
    return out


def exportReport_v2(outFileName, inFileName, out):
    #outFileName: path to file to be edited
    #inFileName: name to append to data
    #out data to export
    #print(outFileName)
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
    return d


def main_compile(WorkingDir, resultFolderName="compiledResults"):
    finalList = getFileNames(WorkingDir)
    #print("finalList :", finalList)
    pDir=WorkingDir
    #pDir = os.path.abspath(os.path.join(WorkingDir, os.pardir))
    pDir = os.path.join(pDir, resultFolderName)
    if not os.path.exists(pDir):
        os.makedirs(pDir)
    else:
        files = [f for f in os.listdir(pDir) if os.path.isfile(os.path.join(pDir, f))]
        for f in files:
            #print(os.path.join(pDir, f))
            os.remove(os.path.join(pDir, f))

    d = [None] * len(finalList)
    for iter, f in enumerate(finalList):
        #print("f :", f)

        tmp = f.split(sep=os.sep)
        inDir = os.path.dirname(f)
        outFileName = os.path.join(pDir, tmp[-2] + ".tsv")

        out = ReadVecData_v3(f)
        d[iter] = exportReport_v2(outFileName, tmp[-1], out)
    
    print(" "*100,end="\r")
    return d


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    WorkingDir = filedialog.askdirectory(initialdir=os.path.join(os.getcwd(), "Markers"), title='Please select a directory')
    main_compile(WorkingDir)

