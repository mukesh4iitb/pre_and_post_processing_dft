import re
concat_osz=input("Enter the name of concatenated OSZICAR file: \n")
osz=open(concat_osz)
lines_osz=osz.readlines()
counter=1
osz_new=open('{}_new'.format(concat_osz),'w+')

for line in lines_osz:
    if re.search("T=", line):
        osz_new.write(str(counter)+" "+ "T=" +line.split("T=")[-1])
        counter=counter+1
    else:
        osz_new.write(line)
