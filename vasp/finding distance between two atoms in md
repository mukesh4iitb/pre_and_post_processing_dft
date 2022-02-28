import sys
import numpy as np
ARGV1=sys.argv[1]
ARGV2=int(sys.argv[2])
ARGV3=int(sys.argv[3])
POS=open(ARGV1,'r')
lines=POS.readlines()
POS.close()
a_vec=np.array(list(map(float,lines[2].split())))
b_vec=np.array(list(map(float,lines[3].split())))
c_vec=np.array(list(map(float,lines[4].split())))
a_cell=np.array([a_vec,b_vec,c_vec])

No_of_atom=sum(list(map(int,lines[6].split())))

if lines[7][0]=='D' or lines[7][0]=='d':
    POSITION_direct=[]
    for line in lines[8:No_of_atom+8]:
        #print(line)
        POSITION_direct.append(list(map(float,line.split())))
    POSITION_direct=np.array(POSITION_direct)
    #print(POSITION_direct)
    POSITION_cart=np.dot(POSITION_direct,a_cell)
    #print(POSITION_cart)
elif lines[7][0]=='C' or lines[7][0]=='c':
    POSITION_cart=[]
    for line in lines[8:No_of_atom+8]:
        #print(line)
        POSITION_cart.append(list(map(float,line.split())))
    POSITION_cart=np.array(POSITION_cart)
else:
    print("Something is wrong!!")
POS_1=POSITION_cart[int(ARGV2)-1]
POS_2=POSITION_cart[int(ARGV3)-1]

dist=np.sqrt(np.sum((POS_1-POS_2)**2))
print('Distance: ', dist)
