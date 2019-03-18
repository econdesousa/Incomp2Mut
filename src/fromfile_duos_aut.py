# ####################################################
# 1
# import modules and functions

seed = 9001
import pyperclip
pyperclip.copy(seed)
from genFamilyAutossomes import *
from getIncomp import *
from readAndExportFile import *
# ####################################################
# 2
# initialize variables
nSim = 100
silent = True  # Modo silencioso, Qd fore para correr a serio com muito casos o silent tem de ser True. nesses casos nao se faz prints de ecra
save2File = True  # Aquilo que seria de imprimir para o ecra pode ir para um ficheiro


# ####################################################
# 3
# load data
#       alleles
#       freqs
#       outFile1:	 *_stats.txt
#       outFile2:	 *_vecFatherMother.txt
#       outFile3:	 *_Pedigrees.txt
file_path, outFile1, outFile2, outFile3 = outFileName(save2File, DIR="FromFile_Duos_Aut")
alleles, frequencies = Read_Two_Column_File(file_path)
incomprate, stepMut = ReadMutRate(file_path+"_mutationrate.txt")

if save2File:
    f1, f2 = initializeOutFiles(outFile1, outFile2, outFile3)

# ####################################################
# 4
# main loop
statsFather = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statsMother = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
compat = 0

for loop in range(nSim):

    father, mother, child, mutation_step, index = genFamilies(alleles, frequencies)
    child, mutation_step = mutationRate(child, 0, incomprate, stepMut)  # mut father allele
    child, mutation_step = mutationRate(child, 1, incomprate, stepMut)  # mut mother allele
    distFatherMother = countincomp(child, father)  # vector of size 2 -> [dist to father, dist to mother]

    statsFather[int(distFatherMother[0])] += 1
    statsMother[int(distFatherMother[1])] += 1
    if distFatherMother[0] == 0 and distFatherMother[1] == 0:
        compat += 1

    if save2File:
        print(compat, "\t", statsFather[0], "\t", statsMother[0], "\t", statsFather[1], "\t", statsMother[1], "\t",
              statsFather[2], "\t", statsMother[2], "\t", statsFather[3], "\t", statsMother[3], "\t", statsFather[4], "\t",
              statsMother[4], "\t", statsFather[5], "\t", statsMother[5], "\t", statsFather[6], "\t", statsMother[6], "\t",
              loop+1, file=f1)
        print(distFatherMother[0], "\t", distFatherMother[1], "\t", loop+1, file=f2)

    exportOutTable(outFile3, father, mother, child, mutation_step, index, distFatherMother,
                   display=not silent, save2file=save2File, iteration=loop + 1)

f1.close()
f2.close()