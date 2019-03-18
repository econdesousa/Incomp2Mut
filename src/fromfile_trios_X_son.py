# ####################################################
# 1
# import modules and functions

from genFamilyAutossomes import *
from getIncomp import *
from readAndExportFile import *

from counttrios_func import counttrios

# ####################################################
# 2
# initialize variables
nSim = 1000
silent = True  # Modo silencioso, Qd fore para correr a serio com muito casos o silent tem de ser True. nesses casos nao se faz prints de ecra
save2File = True  # Aquilo que seria de imprimir para o ecra pode ir para um ficheiro


# ####################################################
# 3
# load data
#       alleles
#       freqs
#       outFile
file_path, outFile1, outFile2, outFile3 = outFileName(save2File, DIR="FromFile_Trios_X_Son")
print(outFile1)
print(outFile2)
print(outFile3)
#with open(outFile1, 'w') as f1:
    #print("comp\tF[0]\tM[0]\tF[1]\tM[1]\tF[2]\tM[2]\tF[3]\tM[3]\tF[4]\tM[4]\tF[5]\tM[5]\tF[6]\tM[6]", file=f1)
#f1.close()
if save2File:
    with open(outFile2, 'w') as f2:
        print("distF\tdistM",file=f2)
    f2.close()

alleles, frequencies = Read_Two_Column_File(file_path)
incomprate, stepMut = ReadMutRate(file_path+"_mutationrate.txt")
incomprate = 0.9
print("incomprate =",incomprate,"stepMut =",stepMut)
#print(incomprate, stepMut)
#alleles, frequencies = ReadMutRate(file_path + "mutationRate")

# ####################################################
# 4
# main loop
if not silent:
    print(file_path, "\n", outFile3)
statsFather = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statsMother = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
compat = 0

with open(outFile1, 'a') as f1:
    for loop in range(nSim) :

        father, mother, child, mutation_step, index = genFamiliesXson(alleles, frequencies)
        child, mutation_step = mutationRate(child, 0, incomprate, stepMut) # mut father allele
        print(mutation_step)
        distFatherMother = countincomp(child, 0, mother)  # vector of size 2 -> [dist to father, dist to mother]

        statsFather[int(distFatherMother[0])] += 1
        statsMother[int(distFatherMother[1])] += 1
        if distFatherMother[0] == 0 and distFatherMother[1] == 0:
            compat += 1

        #print(distFatherMother)
        #print("statsFather = ", statsFather)
        #print("statsMother = ", statsMother)
        #print(compat, "\t", statsFather[0], "\t", statsMother[0],"\t", statsFather[1], "\t", statsMother[1], "\t", statsFather[2], "\t", statsMother[2], "\t",statsFather[3], "\t", statsMother[3],"\t", statsFather[4], "\t", statsMother[4], "\t", statsFather[5], "\t", statsMother[5], "\t",statsFather[6], "\t", statsMother[6],file=f1)
        if save2File :
            with open(outFile2, 'a') as f2 :
                print(distFatherMother[0], "\t", distFatherMother[1], file=f2)
                f2.close()

        exportOutTable(outFile3, father, mother, child, mutation_step, index, distFatherMother, display=not silent,
                       save2file=save2File)

f1.close()

print("")
print("compatibilities = ", compat)
print(#"Compatibilities: ", statsFather[0]+statsMother[0],
      "\nOne step mutations: ", statsFather[1]+statsMother[1],
      "\nTwo steps mutation: ", statsFather[2]+statsMother[2],
      "\nThis is something else: ", statsFather[3]+statsMother[3], "\n\n")
print("Compatibility frequency: ", (statsFather[0]+statsMother[0])/(2*nSim),
      "\nOne step mutation frequency: ", (statsFather[1]+statsMother[1])/(2*nSim),
      "\nTwo steps mutation frequency: ", (statsFather[2]+statsMother[2])/(2*nSim),
      "\nThis is something else: ", (statsFather[3]+statsMother[3])/(2*nSim))