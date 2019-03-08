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
nSim = 1000000
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
#       outFile
file_path, outFile, outFile1, outFile2 = outFileName(save2File, "Incompatibilidades_autossomicos")
alleles, frequencies = Read_Two_Column_File(file_path)
#alleles, frequencies = ReadMutRate(file_path + "mutationRate")

# ####################################################
# 4
# main loop
if not silent:
    print(file_path, "\n", outFile)
for loop in range(nSim):

    father, mother, child, mutation_step, index = genFamilies(alleles, frequencies, 1)
    child = mutationchild(child, mutation_step, index)
    output = countincomp(child, father, mother)
    count = counttrios(output)
    compatibility_trios = compatibility_trios + count[0]
    one_step_mutation_trios = one_step_mutation_trios + count[1]
    two_step_mutation_trios = two_step_mutation_trios + count[2]
    something_else_trios = something_else_trios + count[3]
    exportOutTable(outFile, father, mother, child, mutation_step, index, output, display=not silent, save2file=save2File)

print("")
print("Compatibilities: ", compatibility_trios,
      "\nOne step mutations: ", one_step_mutation_trios,
      "\nTwo steps mutation: ", two_step_mutation_trios,
      "\nThis is something else: ", something_else_trios, "\n\n")
print("Compatibility frequency: ", compatibility_trios/(nSim),
      "\nOne step mutation frequency: ", one_step_mutation_trios/(nSim),
      "\nTwo steps mutation frequency: ", two_step_mutation_trios/(nSim),
      "\nThis is something else: ", something_else_trios/(nSim))
