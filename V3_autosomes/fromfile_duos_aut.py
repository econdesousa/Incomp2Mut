def FromFile_Duos_Aut(PATH="Markers/APOAI1.txt", nSim=100, seed=7644774):
    print(seed)
    import pyperclip
    pyperclip.copy(seed)
    from genFamilyAutossomes import genFamilies
    from genFamilyAutossomes import mutationRate
    from getIncomp import countincomp
    from readAndExportFile import outFileName
    from readAndExportFile import Read_Two_Column_File
    from readAndExportFile import exportOutTable
    from readAndExportFile import initializeOutFiles
    from readAndExportFile import ReadMutRate

    silent = True  # Silent mode. Remove all print statments if true
    save2File = False  # If false save prints to file instead of displaying on screen

    file_path, outFile1, outFile2, outFile3 = outFileName(save2File, DIR="FromFile_Duos_Aut", fp=PATH)
    alleles, frequencies = Read_Two_Column_File(file_path)
    incomprate, stepMut = ReadMutRate(file_path+"_mutationrate.txt")

    f1, f2 = initializeOutFiles(outFile1, outFile2, outFile3, save2File)

    statsFather = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    statsMother = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    compat = 0

    for loop in range(nSim):

        father, mother, child, mutation_step, index = genFamilies(alleles, frequencies)
        child, mutation_step = mutationRate(child, 0, incomprate, stepMut)
        child, mutation_step = mutationRate(child, 1, incomprate, stepMut)
        distFatherMother = countincomp(child, father)

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

    if save2File:
        f1.close()
    f2.close()
