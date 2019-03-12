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
save2File = True  # Aquilo que seria de imprimeir para o ecra pode ir para um ficheiro
compatibility_trios = 0
one_step_mutation_trios = 0
two_step_mutation_trios = 0
something_else_trios = 0


# ####################################################
# 3
# load data
#       alleles
#       freqs
#       outFile1:	 *_stats.txt
#       outFile2:	 *_vecFatherMother.txt
#       outFile3:	 *_Pedigrees.txt
file_path, outFile1, outFile2, outFile3 = outFileName(save2File, "ForcedMut_duos_aut")
alleles, frequencies = Read_Two_Column_File(file_path)
#alleles, frequencies = ReadMutRate(file_path + "mutationRate")

# ####################################################
# 4
# main loop
statsFather = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statsMother = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
compat = 0

for loop in range(nSim):

    father, mother, child, mutation_step, index = genFamilies(alleles, frequencies, 1)
    child = mutationchild(child, mutation_step, index)
    distFatherMother = countincomp(child, father)  # vector of size 2 -> [dist to father, dist to mother]

    statsFather[int(distFatherMother[0])] += 1
    statsMother[int(distFatherMother[1])] += 1
    if distFatherMother[0] == 0 and distFatherMother[1] == 0:
        compat += 1

    #print(distFatherMother)
    #print("statsFather = ", statsFather)
    #print("statsMother = ", statsMother)
    if save2File:
        with open(outFile1, 'a') as f1:  # *_vecFatherMother.txt
            print(compat, "\t", statsFather[0], "\t", statsMother[0], "\t", statsFather[1], "\t", statsMother[1], "\t",
                  statsFather[2], "\t", statsMother[2], "\t", statsFather[3], "\t", statsMother[3], "\t", statsFather[4], "\t",
                  statsMother[4], "\t", statsFather[5], "\t", statsMother[5], "\t", statsFather[6], "\t", statsMother[6],
                  file=f1)
        with open(outFile2, 'a') as f2 :
            print(distFatherMother[0], "\t", distFatherMother[1], file=f2)
            f2.close()

    exportOutTable(outFile3, father, mother, child, mutation_step, index, distFatherMother,
                   display=not silent,save2file=save2File,iteration=loop+1)

print("")
print("Compatibilities: ", compatibility_trios,
      "\nOne step mutations: ", one_step_mutation_trios,
      "\nTwo steps mutation: ", two_step_mutation_trios,
      "\nThis is something else: ", something_else_trios, "\n\n")
print("Compatibility frequency: ", compatibility_trios/(nSim),
      "\nOne step mutation frequency: ", one_step_mutation_trios/(nSim),
      "\nTwo steps mutation frequency: ", two_step_mutation_trios/(nSim),
      "\nThis is something else: ", something_else_trios/(nSim))
