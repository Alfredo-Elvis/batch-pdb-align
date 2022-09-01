import os,os.path
from pymol import cmd
import argparse
from multiprocessing import Pool

def align_multi(file,num,file_num,cpu_num):
        target=file[0]
        mobile=file[1]
        cmd.load(target)
        cmd.load(mobile)
        target_prefix=target[:-4]
        mobile_prefix=mobile[:-4]
        a=cmd.align(mobile_prefix,target_prefix)
        folder = os.path.exists("./align")
        if not folder:
            os.makedirs("./align")
        cmd.save(f"./align/{mobile_prefix}_align.pdb",mobile_prefix)
        a=a[3]/10
        a=str(a)
        a=a[:7]
        result=f"{mobile_prefix},{a}\n"
        f=open(f".results{num}.txt","w")
        f.write(result)
        f.close()
        #print(f"{mobile_prefix}:{results[mobile_prefix]}")
        cmd.delete(all)
        if num % cpu_num == 0:
            file_num=str(file_num)
            lenth=len(file_num)
            lenth=lenth
            process=f"{num}               "
            process=process[:lenth]
            print(f"{process}/{file_num} structures have been analysis.")

def align(prefix,cpu_num):
    file_num = 0
    for root,dirname,filenames in os.walk("./"):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.pdb':
                file_num += 1
    file_num=file_num-1
    print("Analyse begin.")
    pool = Pool(int(cpu_num))
    for i in range(file_num):
    #for i in range(10):
        j=i+1
        target=f"{prefix}0.pdb"
        mobile=f"{prefix}{j}.pdb"
        filename=(target,mobile)
        pool.apply_async(align_multi, (filename,j,file_num,cpu_num,))
    pool.close()
    pool.join()
    results={
    "structure_id":"rmsd"
    }

    text=[]
    #for i in range(10):
    for i in range(file_num):
        j=i+1
        fx=open(f".results{j}.txt")
        ftxt=fx.read()
        text.append(ftxt)
        os.remove(f".results{j}.txt")
    fmd = open('results.txt','w')
    for t in range(len(text)):
        fmd.write(text[t])
    fmd.close()
    with open("results.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            info=line.split(",")
            key=info[0]
            value=info[1]
            results[key]=value
    f.close()
    fr=open("results.txt","w")
    fr.write("structure_id:rmsd\n")
    #for i in range(10):
    for i in range(file_num):
        j=i+1
        result_rmsd=results[f"{prefix}{j}"]
        fr.write(f"{prefix}{j}:{result_rmsd}")
    fr.close()
    print("Finished.")


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix', type=str, default = None)
    parser.add_argument('--ppns', type=int, default = 10)
    args = parser.parse_args()
    if args.prefix!=None:
        prefix=args.prefix
        ppns=args.ppns
        print(f"Using {ppns} Cpus to align and compute RMSD(nm).")
        align(prefix,ppns)
    else:
        print("Usage: python align.py --prefix= --ppns=\n"
            "prefix: the prefix name of pdb file.\n"
            "ppns(10):the cpu numbers.")
        exit(1)
