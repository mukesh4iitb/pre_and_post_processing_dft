POS=open("TiO2.vasp",'r')
POS_out=open("TiO2_out.vasp",'w')

#Reading POS file
list_vec=[]
for line in POS:
    line1=line.split()
    list_vec.append(line1)
    #print(line1)
    #print("     ".join(line1))
POS.close()

#Start writing POS_out file
POS_out.write('  '.join(list_vec[0])+'\n')
POS_out.write('  '.join(list_vec[1])+'\n')

change_axis=input("Enter the axis you want to enterchange ie ab,bc,ca \n")
if change_axis=='ab':
    A,B=1,2
elif change_axis=='bc':
    A,B=2,3
elif change_axis=='ca':
    A,B=3,1

list_vec[A+1],list_vec[B+1]=list_vec[B+1],list_vec[A+1]
#list_vec[2],list_vec[3]=list_vec[3],list_vec[2]

list_vec[2][A-1],list_vec[2][B-1]=list_vec[2][B-1],list_vec[2][A-1]
list_vec[3][A-1],list_vec[3][B-1]=list_vec[3][B-1],list_vec[3][A-1]
list_vec[4][A-1],list_vec[4][B-1]=list_vec[4][B-1],list_vec[4][A-1]

POS_out.write('        '+'       '.join(list_vec[2])+'\n')
POS_out.write('        '+'       '.join(list_vec[3])+'\n')
POS_out.write('        '+'       '.join(list_vec[4])+'\n')

POS_out.write('    '+'  '.join(list_vec[5])+'\n')
POS_out.write('    '+'    '.join(list_vec[6])+'\n')
POS_out.write(' '.join(list_vec[7])+'\n')

for elem in list_vec[8:]:
    elem[A-1],elem[B-1]=elem[B-1],elem[A-1]
    POS_out.write("       ".join(elem)+'\n')

POS_out.close()
