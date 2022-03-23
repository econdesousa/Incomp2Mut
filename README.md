# Incomp2Mut

Here we aim to assess mutation rates from incompatibility rates obtained through the Mendelian incompatibility approach.
This work will cover autossomes for familial duos (parent-child) and trios (parents-child).

## Related publications
**Antão-Sousa S, Conde-Sousa E, Gusmão L, Amorim A, Pinto N (2022 submitted) 
Mutation rates estimation depends on population allele frequency distribution: the case of autosomal microsatellites**


## USAGE:
### Batch Processing
To reproduce simulations performed in the paper, please install python (tested on python 3.8) and run pip "install -r requirements.txt".

Use functions callAllfunctions_autosomes_mut1_duos.py and callAllfunctions_autosomes_mut1_trios.py to generate familial profiles for duos/trios and get allele distance between child and each parent.

Pass as input the path to the folder containing markers.

Use the function compileResults.py (same flder as input) to generate a resume of the familial distances:
* 0-0 means hidden mutation
* 1-0 means distance of one step to the father and compatibility with the mother
* 0-1 means compatibility with the father and distance of one step to the mother
* ...

### Single marker
To run the code for a single marker there are two options: runing directly from python or via an executable (available in folder "dist"). 

* From command line: "python main.py" or 
* From executable: double clicking on it.

A GUI will show up and the user must choose the configurations he/she wants:
* Familial configuration: choose between Duos (Father / Child) or Trios (Father / Mother / Child)
* Incompatibility Rate: Enter here the **observed** incompatibility rate.
* Number of Simulations: choose the desired number of simulations
	* for the markers we tested n>100 000 will result in similar Mutation Rates. If n is too big the simulations may take a while depending on the user machine. Please wait for the "Done!" window before disconnecting.
* Random Seed: Starting point in generating random numbers. This can be any number. Using the same number in consecutive runs (with same parameters) will ensure reproducible results. You can enlarge n or test with different random seeds to evaluate convergence of the result.
* OK! button: Press this button to run.

After pressing OK! a window will appear to ask for a file containing the marker information. Select it and press open.

Results will be saved in the same folder of the marker file with the same basename appended by some configuration parameters. 
For example file CSF1PO_Somalia_Duos_Aut_1_100000_7068971.csv was evaluated on a marker file with basename CSF1PO_Somalia 
for Duos in Autossomal markers with a fixed 1 step mutation for 100000 simulations with random seed 7068971.

The parameters will also be displayed in the file along with the % of hidden mutations and the corrected mutation rate.


### Marker files
Please see the marker file in the example "Incomp2Mut/src/Markers/CSF1PO_Norway.txt"
* The first row should contain the name of the marker (in quotes).
* The following rows should contain two collumns separated by a tab.
	* First collumn with the allele (in quotes)
	* Second column with the corresponding allele frequency
	
## Contacts:
For any questions please contact:
* Nádia Pinto: npinto@ipatimup.pt
* Sofia Antão-Sousa: sofias@ipatimup.pt
* Eduardo Conde-Sousa: econdesousa@gmail.com




https://user-images.githubusercontent.com/16939981/159753290-b1852bed-922e-46d2-9236-64931ec2470e.mp4


