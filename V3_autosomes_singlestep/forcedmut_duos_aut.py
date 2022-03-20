def ForcedMut_Duos_Aut(PATH="Markers/APOAI1.txt", nMutMale=1, nMutFemale=1, rThresh=0.5, nSim=100, seed=7644774):
    # ####################################################
    # 1
    # import modules and functions
    print(seed)
    import pyperclip
    pyperclip.copy(seed)
    from genFamilyAutossomes import genFamilies_v2
    from genFamilyAutossomes import mutationchild
    from getIncomp import countincomp_v2
    from readAndExportFile import outFileName
    from readAndExportFile import Read_Two_Column_File
    from readAndExportFile import exportOutTable
    from readAndExportFile import initializeOutFiles
    # ####################################################
    # 2
    # initialize variables
    silent = True  # True for silent mode, no prints occurring
    save2File = False  # False to save prints to file instead of displaying on screen

    # ####################################################
    # 3
    # load data
    #       alleles
    #       freqs
    #       outFile1:	 *_stats.txt
    #       outFile2:	 *_vecFatherMother.txt
    #       outFile3:	 *_Pedigrees.txt
    file_path, outFile1, outFile2, outFile3 = outFileName(save2File, "ForcedMut_Duos_Aut_nMut_"+str(nMutMale)+"_"+str(nMutFemale), fp=PATH)
    alleles, frequencies = Read_Two_Column_File(file_path)
    #alleles, frequencies = ReadMutRate(file_path + "mutationRate")

    f1, f2 = initializeOutFiles(outFile1, outFile2, outFile3, save2File, legacy=0)
    # f1 will be disregarded; just for legacy purposes

    # ####################################################
    # 4
    # main loop

    for loop in range(nSim):

        father, mother, child, mutation_step, index = genFamilies_v2(alleles, frequencies, nMutMale, nMutFemale, rThresh)
        child = mutationchild(child, mutation_step, index)
        distFatherMother = countincomp_v2(child, father)  # vector of size 8x2

        for i in range(len(distFatherMother)):
            for j in range(len(distFatherMother[0])):
                print(distFatherMother[i][j], end="\t", file=f2)
        print(loop+1, file=f2)

        exportOutTable(outFile3, father, mother, child, mutation_step, index, distFatherMother,
                       display=not silent, save2file=save2File, iteration=loop+1)

    f2.close()
