import numpy as np
#import time 
DOSCAR_FILE=input("Enter the name of the DOSCAR file\n")
#start_time=time.time()
f=open(DOSCAR_FILE,'r')
for i,line in enumerate(f):
	if i==0:
		no_of_atom=int(line.split()[0]) # number of atoms.
		dos_type=int(line.split()[2]) # dos_type is 0 for no patial dos; 1 for included partial dos. 
	if i==5:
		ulim=float(line.split()[0])
		llim=float(line.split()[1])
		fermi_E=float(line.split()[-2])
		#print(llim)
		#print(ulim)
no_of_line=(i+1)
#n=int((no_of_line-5)/3)
n=int((no_of_line-5)/(no_of_atom+1))
print("Fermi Energy of this system:",fermi_E)
#print(n)
#print(no_of_line)
#print("dos_type",dos_type)
#print(no_of_atom)
def dos_total():
	g=open(DOSCAR_FILE,'r')
	list1=[]
	list2=[]
	list3=[]
	for j,lines in enumerate(g):
		if j>5:
        #       if float(lines.split()[0])>llim and float(lines.split()[0])<ulim:
			list1.append(list(map(float,lines.split())))
	dos1=np.array(list1)
	np.savetxt('DOS0',dos1,fmt='%10.5f')




def Density_of_state():
	obj={}
	dos={}
	for k in range(no_of_atom+1):
		obj['l'+str(k)]=[]
		#print(obj['l'+str(k)])
		g=open(DOSCAR_FILE,'r')
		for j,lines in enumerate(g):
			if j>(k*n+5) and j<((k+1)*n+5):
				obj['l'+str(k)].append(list(map(float,lines.split())))
#			print(obj)
#		if j>5 and j<(n+5):
#			list1.append(list(map(float,lines.split())))
#		if j>(n+5) and j<(2*n+5):
#			list2.append(list(map(float,lines.split())))
	#	print(obj['l0'])
		dos['a'+str(k)]=np.array(obj['l'+str(k)])
		np.savetxt('DOS'+str(k),dos['a'+str(k)],fmt='%10.5f')
		#print('value of k',k)
		#print(dos_type)
		if dos_type==0:
			break
#		np.savetxt('DOS'+str(k),dos['a'+str(k)],fmt='%10.5f')
#	dos1=np.array(list1)
#	np.savetxt('TOTAL_DOS',dos1,fmt='%10.5f')
#	dos2=np.array(list2)
#	np.savetxt('PARTIAL_DOS',dos2,fmt='%10.5f')

#dos_type0=input("Enter TOTAL   :if DOSACR has only total dos,\nEnter PARTIAL :if DOSCAR has partial dos ie s,p,d,f and its decomposition\n")
#if dos_type0=="TOTAL":
#        dos_total()
#if dos_type0=="PARTIAL":
#        dos_partial()

def Density_of_state_of_an_atom():
	list0=[]
	list_atom=[]
	g=open(DOSCAR_FILE,'r')
	for j,lines in enumerate(g):
		if j>5 and j<(n+5):
			list0.append(list(map(float,lines.split())))
		if j>(atom_no*n+5) and j<((atom_no+1)*n+5):
			list_atom.append(list(map(float,lines.split())))
	dos0=np.array(list0)
	np.savetxt('DOS0',dos0,fmt='%10.5f')
	dos_atom=np.array(list_atom)
	np.savetxt('DOS'+str(atom_no),dos_atom,fmt='%10.5f')

#atom_no=int(input("Enter the no of atom whose dos you want\n"))			


SYSTEM=input("If you want to Total dos of system: Enter TOTAL \nIf  you  want  specific  atom  dos: Enter ATOM \nIf you want all atom dos+total dos: Enter ALL\n")
if SYSTEM=="TOTAL":
    dos_total()
if SYSTEM=="ATOM":
	atom_no=int(input("Enter the serial no. of atom whose dos you want:\n"))
	Density_of_state_of_an_atom()
if SYSTEM=="ALL":
	Density_of_state()
#end_time=time.time()
#print("Time taken to run program is:",end_time-start_time)


#list0=[]
#list_atom=[]
#g=open("DOSCAR",'r')
#for j,lines in enumerate(g):
#	if j>5 and j<(n+5):
#		list0.append(list(map(float,lines.split())))
#	if j>(atom_no*n+5) and j<((atom_no+1)*n+5):
#		list_atom.append(list(map(float,lines.split())))
#dos0=np.array(list0)
#np.savetxt('DOS0',dos0,fmt='%10.5f')
#dos_atom=np.array(list_atom)	
#np.savetxt('DOS'+str(atom_no),dos_atom,fmt='%10.5f')











#g=open("DOSCAR",'r')
#list1=[]
#list2=[]
#list3=[]
#for j,lines in enumerate(g):
#	if j>5 and j<(n+5):
	#	if float(lines.split()[0])>llim and float(lines.split()[0])<ulim:
#		list1.append(list(map(float,lines.split())))
#	if j>(n+5) and j<(2*n+5):
        #       if float(lines.split()[0])>llim and float(lines.split()[0])<ulim:
#		list2.append(list(map(float,lines.split())))
#	if j>(2*n+5) and j<(3*n+5):
        #       if float(lines.split()[0])>llim and float(lines.split()[0])<ulim:
#		list3.append(list(map(float,lines.split())))
#dos1=np.array(list1)
#print(list1)
#print(type(dos1)
#np.savetxt('dos1',dos1,fmt='%10.3f')
#dos2=np.array(list2)
#np.savetxt('dos2',dos2,fmt='%10.3f')
#dos3=np.array(list3)
#np.savetxt('dos3',dos3,fmt='%10.3f')

