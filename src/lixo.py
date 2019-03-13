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
#       outFile1
file_path, outFile1, outFile2, outFile3 = outFileName(save2File, "ForcedMut_duos_aut")


print("file_path:\t", file_path, "\noutFile1:\t", outFile1, "\noutFile2:\t", outFile2, "\noutFile3:\t", outFile3 )
