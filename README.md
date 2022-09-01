# Introduction
align protein pdb structures use pymol.  
# How to install
Install pymol by [conda](https://pymol.org/conda/) and activate the pymol environment.  
```conda install -c conda-forge -c schrodinger pymol-bundle```  
# How to use
1. Put the script and your structure pdb files to the same folder.  
2. Prepare your PDB file with name **like this**:  
&ensp;&ensp;&ensp;&ensp;conf0.pdb, conf1.pdb,conf2.pdb,...,confxxx.pdb.  
&ensp;&ensp;&ensp;&ensp;This script will align protein structure to **conf0.pdb**  
3. Just run command ```python align_rmsd.py --prefix xxx --ppns=n```  
&ensp;&ensp;**prefix** means the name of your pdb file prefix.  
&ensp;&ensp;**ppns** means the cpus you want to use to align.  
# Results
The final structure will be stored in the folder **./align**" with the name of "{prefix}x_align.pdb  
The rmsd will be stored in **results.txt** when align finished.  
# Contact me
This script was developed to speed up my own work, and I'm putting it here in the hope that more people will want to try using it.  
Feel free to write me an email (zhouyq@shanghaitech.edu.cn) if you have any question, but I don't guarantee that I'll solve your problem.
