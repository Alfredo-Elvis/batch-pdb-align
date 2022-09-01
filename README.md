# 介绍  
使用pymol进行大量蛋白结构比对并返回rmsd值。(pdb 文件。)  
# 如何安装  
通过[conda](https://pymol.org/conda/)安装pymol并激活pymol环境  
```conda create --name pymol```  
```conda activate pymol```  
```conda install -c conda-forge -c schrodinger pymol-bundle```  
# 如何使用  
1. 把脚本和你的pdb文件放到同一目录下。  
2. 将pdb文件**名称**改为下列这样：  
&ensp;&ensp;&ensp;&ensp;conf0.pdb, conf1.pdb,conf2.pdb,...,confxxx.pdb.  
&ensp;&ensp;&ensp;&ensp;脚本将会将蛋白质结构比对到 **conf0.pdb**。  
3. 运行命令```python align_rmsd.py --prefix xxx --ppns=n```  
&ensp;&ensp;**prefix** 指pdb文件的前缀，例如conf。  
&ensp;&ensp;**ppns** 指比对结构所用核数。  
# 结果
比对结果以{前缀_align.pdb}的名字存储在“**./align**”文件夹中。
RMSD指被保存在results.txt文件中。
# 联系我
开发这个脚本是为了加快我自己的工作，我把它放在这里是希望有更多的人愿意尝试使用它。  
如果你有任何问题，请随时给我写电子邮件(zhouyq@shanghaitech.edu.cn)，但我不能保证我会解决你的问题。  
    &ensp;&ensp;  
    &ensp;&ensp;  
    &ensp;&ensp;  
# Introduction
Align protein structures use pymol and return the RMSD value.(pdb files just.)  
# How to install
Install pymol by [conda](https://pymol.org/conda/) and activate the pymol environment.  
```conda create --name pymol```  
```conda activate pymol```  
```conda install -c conda-forge -c schrodinger pymol-bundle```  
# How to use
1. Put the script and your structure pdb files to the same folder.  
2. Prepare your PDB file with name **like this**:  
&ensp;&ensp;&ensp;&ensp;conf0.pdb, conf1.pdb,conf2.pdb,...,confxxx.pdb.  
&ensp;&ensp;&ensp;&ensp;This script will align protein structure to **conf0.pdb**  
3. Just run command ```python align_rmsd.py --prefix xxx --ppns=n```  
&ensp;&ensp;**prefix** means the name of your pdb file prefix, i.e., conf.  
&ensp;&ensp;**ppns** means the cpus you want to use to align.  
# Results
The final structure will be stored in the folder "**./align**" with the name of "{prefix}x_align.pdb  
The RMSD will be stored in **results.txt** when align finished.  
# Contact me
This script was developed to speed up my own work, and I'm putting it here in the hope that more people will want to try using it.  
Feel free to write me an email (zhouyq@shanghaitech.edu.cn) if you have any question, but I don't guarantee that I'll solve your problem.
