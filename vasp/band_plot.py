"""Note:
    1- Use polar_band-KPOINTS for band data extraction from EIGENVAL file
    2- That can be download from here:
        http://www.ranjitcmslab.com/Scripts.html
"""
import numpy as np
import matplotlib.pyplot as plt
band_file=input("Enter the name of band file\n")
data=np.loadtxt(band_file)
rows,cols=data.shape

# band plots
for i in range(1,cols):
    #print(i)
    plt.plot(data[:,0],data[:,i],color='b')

# klables plots
kpts_per_path=int(input('Enter the numbe of kpoints in one path'))
KLABLES=[data[:,0][i-1] for i in range(kpts_per_path,rows+1,kpts_per_path)]
KLABLES.insert(0,data[:,0][0])
for i in KLABLES:
    plt.axvline(i,ls='--',color='r')
    
plt.show()
np.savetxt('klable.txt',KLABLES,fmt='%10.12f')
print("\n K-lables are written the klable.txt file!! \n")
