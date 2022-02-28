# this is utility code-2
import numpy as np
def gradient(i1,i2):
	"""first argument is first point line,
	second argument is second point line"""
	file=input("name of the file")
	f=open(file,"r")
	lines=f.readlines()
	print("first point:",lines[i1-1])
	print("second point:",lines[i2-1])
	p1=np.array(list(map(float,lines[i1-1].split())))
	p2=np.array(list(map(float,lines[i2-1].split())))
	grad=(p2[0]-p1[0])/(p2[1]-p1[1])
	ang=np.arctan(grad)
	return ("angle and gradient are :",ang,grad)
def pt_from_one_pt(i1,i2):
	""" first and second arguments lines are used to find the direction cosine l,m,n
	and third argument line is the point from where we want to find distance."""
	file=input("name of the file")
	f=open(file,"r")
	lines=f.readlines()
	print("first point:",lines[i1-1])
	print("second point:",lines[i2-1])
	print("point from where we want to find point at certain distance")
	p1=np.array(list(map(float,lines[i1-1].split())))
	p2=np.array(list(map(float,lines[i2-1].split())))
	p=np.array(list(map(float,input("Enter the middle point co-ordinate\n").split())))
	d=float(input("Enter the distance\n"))
	l=(p2[0]-p1[0])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	m=(p2[1]-p1[1])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	n=(p2[2]-p1[2])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	return (p[0]+d*l,p[1]+d*m,p[2]+d*n)
def middle_pt(i1,i2):
	"""first argument is first point line,
	second argument is second point line"""
	file=input("name of the file\n")
	f=open(file,"r")
	lines=f.readlines()
	print("first point:",lines[i1-1])
	print("second point:",lines[i2-1])
	p1=np.array(list(map(float,lines[i1-1].split())))
	p2=np.array(list(map(float,lines[i2-1].split())))
	return np.array([(p1[0]+p2[0])/2,(p1[1]+p2[1])/2,(p1[2]+p2[2])/2])
def rotation(i1,i2):
	"""first argument represent position of atom around which rotation is going on
	second line position of atom which are being rotated."""
	####reference of this code is ###########################
	#### https://en.wikipedia.org/wiki/Rotation_matrix ######
	file=input("name of the file")
	f=open(file,"r")
	lines=f.readlines()
	print("Origin vector:",lines[i1-1])
	print("Vector which is being rotated:",lines[i2-1])
	ang=np.array(list(map(float,input("Enter rotation angle around x, y, z-axis separated by space\n").split())))
	vec0=np.array(list(map(float,lines[i1-1].split())))
	vec1=np.array(list(map(float,lines[i2-1].split())))
	ang=ang*np.pi/180
	Rz=np.array([[np.cos(ang[2]),-np.sin(ang[2]),0],
	[np.sin(ang[2]),np.cos(ang[2]),0],
	[0,0,1]])

	Rx=np.array([[1,0,0],
	[0,np.cos(ang[0]),-np.sin(ang[0])],
	[0,np.sin(ang[0]),np.cos(ang[0])]])
	
	Ry=np.array([[np.cos(ang[1]),0,-np.sin(ang[1])],
	[0,1,0],
	[np.sin(ang[1]),0,np.cos(ang[1])]])
	vec=vec1-vec0
	print("rotated vecotor is:")
	return np.dot(np.dot(Rz,np.dot(Ry,Rx)),vec)+vec0
def translation(i1,i2):
    """first argument is line of origin vector and 
    second argument is line of translation vector."""
    file=input("name of the file")
    f=open(file,"r")
    lines=f.readlines()
    print("origin vecotor:",lines[i1-1])
    print("translation vector:",lines[i2-1])
    origin_vec=np.array(list(map(float,lines[i1-1].split())))
    tran_vec=np.array(list(map(float,lines[i2-1].split())))
    return origin_vec+tran_vec
def mirror_images(i1,i2,i3,i4):
    file=input("name of the file")
    f=open(file,'r')
    lines=f.readlines()
    print('1st point in plan',lines[i1-1])
    print('2nd point in plan',lines[i2-1])
    print('3rd point in plan',lines[i3-1])
    print('Point to find mirror images',lines[i4-1])
    p1=np.array(list(map(float,lines[i1-1].split())))
    p2=np.array(list(map(float,lines[i2-1].split())))
    p3=np.array(list(map(float,lines[i3-1].split())))
    xp=np.array(list(map(float,lines[i4-1].split())))
    p2p1=p2-p1 #p2p1 is displacement vector(P2,P1)
    p3p1=p3-p1 #p3p1 is displacement vector(P3,p1)
    dr=np.cross(p2p1,p3p1)#dr is direction ratio
    constant_term=(dr[0]*(xp[0]-p1[0])+dr[1]*(xp[1]-p1[1])+dr[2]*(xp[2]-p1[2]))/np.sum(dr**2)
    image=(-2*dr[0]*constant_term+xp[0],-2*dr[1]*constant_term+xp[1],-2*dr[2]*constant_term+xp[2])
    return image
