import os
import shutil
import glob
import gzip


def creating_arxiv_dirs():
    for name in os.listdir("."):
        if os.path.isdir(name) and not name.endswith(".arxiv"):
            
            target = f"{name}.arxiv"
            
            if not os.path.exists(target):
                os.makedirs(target)
                print(f"Created: {target}")
            else:
                print(f"Already exists: {target}")


def creating_arxiv_trees():
    for d in os.listdir("."):
        if d.endswith(".arxiv"):
            
            SOURCE = d.replace(".arxiv", "")
            TARGET = d
            
            if not os.path.exists(SOURCE):
                continue
            
            print(f"\nMirroring: {SOURCE} >> {TARGET}")
            
            for root, dirs, files in os.walk(SOURCE):
                
                rel_path = os.path.relpath(root, SOURCE)
                
                if rel_path == ".":
                    target_path = TARGET
                else:
                    target_path = os.path.join(TARGET, rel_path)
                
                os.makedirs(target_path, exist_ok=True)
                print(f"Created: {target_path}")


def archiving_files():
    for d in os.listdir("."):
        if d.endswith(".arxiv"):
            
            SOURCE = d.replace(".arxiv", "")
            TARGET = d
            
            if not os.path.exists(SOURCE):
                continue
            
            print(f"\nArchiving files: {SOURCE} >> {TARGET}")
            
            for root, dirs, files in os.walk(SOURCE):
                
                rel_path = os.path.relpath(root, SOURCE)
                
                if rel_path == ".":
                    target_path = TARGET
                else:
                    target_path = os.path.join(TARGET, rel_path)
                
                #  Copying input files 
                for f in INPUT_FILES:
                    src_file = os.path.join(root, f)
                    if os.path.exists(src_file):
                        shutil.copy2(src_file, target_path)
                        print(f"Copied: {src_file}")
                
                #  Copying job scripts 
                for job_file in glob.glob(os.path.join(root, JOB_PATTERN)):
                    shutil.copy2(job_file, target_path)
                    print(f"Copied: {job_file}")
                
                #  Copying output files (if exist)
                for f in OUTPUT_FILES:
                    src_file = os.path.join(root, f)
                    if os.path.exists(src_file):
                        shutil.copy2(src_file, target_path)
                        print(f"Copied: {src_file}")


def compressing_outputs():
    for d in os.listdir("."):
        if d.endswith(".arxiv"):
            print(f"\nCompressing files of {d}:")
            for root, dirs, files in os.walk(d):
                for f in files:
                    if f in OUTPUT_FILES:
                        src_file = os.path.join(root, f)
                        gz_file = src_file + ".gz"

                        # Compress using gzip
                        print(f"Compressing {src_file} >> {gz_file}")
                        with open(src_file, 'rb') as f_in, gzip.open(gz_file, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)

                        # Delete original file
                        os.remove(src_file)







if __name__ == "__main__":

    INPUT_FILES = ["POSCAR", "KPOINTS", "INCAR", "POTCAR"]
    OUTPUT_FILES = ["CONTCAR", "OSZICAR", "OUTCAR", "XDATCAR", "vasprun.xml"]
    JOB_PATTERN = "job*.sh"


    creating_arxiv_dirs()
    creating_arxiv_trees()
    archiving_files()
    compressing_outputs()
    print("\nAll done!")
