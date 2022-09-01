# batch-pdb-align
align protein pdb structures use pymol.
1. Install pymol by [conda](https://pymol.org/conda/) and source activate the pymol environment.
2. Put the script and your structure pdb files to the same folder.
3. Prepare your PDB file with name **like this**:
&ensp;&ensp;&ensp;&ensp;conf0.pdb, conf1.pdb,conf2.pdb,...,confxxx.pdb.
&ensp;&ensp;&ensp;&ensp;This script will align protein structure to **conf0.pdb**
5. Just run command "**python align_rmsd.py --prefix xxx** --ppns=n"
&ensp;&ensp;prefix means the name of your pdb file prefix.
&ensp;&ensp;ppns means the cpus you want to use to align.
The final structure will be store in the folder "**./align**" with the name of "{prefix}x_align.pdb"
The rmsd will be store in **results.txt** when align finished.
