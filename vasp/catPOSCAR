#!/bin/python3 
import sys
import numpy as np
#print(len(sys.argv))
#print((sys.argv[1]))
#print((sys.argv[2]))
POS0=open(sys.argv[1],'r')
POS1=open(sys.argv[2],'r')
lines0=POS0.readlines()
lines1=POS1.readlines()
POS0.close()
POS1.close()

# lattice vectors of both POSCAR files
a0_vec=np.array(list(map(float,lines0[2].split())))
b0_vec=np.array(list(map(float,lines0[3].split())))
c0_vec=np.array(list(map(float,lines0[4].split())))
a1_vec=np.array(list(map(float,lines1[2].split())))
b1_vec=np.array(list(map(float,lines1[3].split())))
c1_vec=np.array(list(map(float,lines1[4].split())))

# cell of both POSCAR files
a0_cell=np.array([a0_vec,b0_vec,c0_vec])
a1_cell=np.array([a1_vec,b1_vec,c1_vec])
compare=a0_cell==a1_cell

# comparing cell
if compare.all():
    print('Fortunately,Lattice vectors are same!!')
else:
    print('Unfortunately,Latttice vectors are not same:\n',compare)

cat_POS=open('cat_POSCAR.vasp','w')
#print(lines0[0].strip('\n')+ " + " +lines1[0])
cat_POS.write(lines0[0].strip('\n')+ " + " +lines1[0])

for line in lines0[1:5]:
    cat_POS.write(line)

lines05=lines0[5].split()
lines15=['X{}'.format(i) for i in range(len(lines1[5].split()))]
#print('  '.join(lines05+lines15)+'\n')
cat_POS.write('  '.join(lines05+lines15)+'\n')

lines06=lines0[6].split()
lines16=lines1[6].split()
#print('  '.join(lines06+lines16)+'\n')
cat_POS.write('  '.join(lines06+lines16)+'\n')

for line in lines0[7:]:
    #print(line)
    cat_POS.write(line)
for line in lines1[8:]:
    #print(line)
    cat_POS.write(line)
cat_POS.close()
print("\nConcatenated POSCAR is written in cat_POSCAR.vasp\n")
