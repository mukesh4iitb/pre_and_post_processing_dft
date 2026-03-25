###Formula used in this script can be found here:
###https://en.wikipedia.org/wiki/List_of_common_coordinate_transformations##

###In this script I have chose default co-ordinate number is 3. so for radial
###to cartesian we use rad_to_car while in 2d we have to use rad_to_car_2d.##

# this is utility code-1
import numpy as np


def rad_to_car():
    r=float(input("Enter the value of r:\n" ))
    theta=float(input("Enter the value of theta(angle between vec r and z-axis):\n"))
    phi=float(input("Enter the value of phi(angle between projection of r and x-axis):\n"))
    theta=theta*np.pi/180
    phi=phi*np.pi/180
    x=r*np.sin(theta)*np.cos(phi)
    y=r*np.sin(theta)*np.sin(phi)
    z=r*np.cos(theta)
    return (x,y,z)
#print(rad_to_car())
#print("mukesh(singh)")


def car_to_rad():
    x=float(input("Enter x co-ordinate value:\n"))
    y=float(input("Enter y co-ordinate value:\n"))
    z=float(input("Enter z co-ordinate value:\n"))
    r=np.sqrt(x**2+y**2+z**2)
    theta=np.arctan(np.sqrt(x**2+y**2)/z)
    #theta=np.arctan2(np.sqrt(x**2+y**2),z)
    theta=theta*180/np.pi
    phi=np.arctan2(y,x)
    phi=phi*180/np.pi
    return (r,theta,phi)
#print(car_to_rad())
def car_to_rad_wrt_pt():
	print("Enter the first point in 3D separated by space")
	p1=np.array(list(map(float,input().split())))
	print("Enter the second point in 3D separated by space")
	p2=np.array(list(map(float,input().split())))
	r=np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	theta=np.arctan(np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)/(p2[2]-p1[2]))
	phi=np.arctan2((p2[1]-p1[1]),(p2[0]-p1[0]))
	theta=theta*180/np.pi
	phi=phi*180/np.pi
	return (r, theta, phi)	
def car_to_rad_2d():
    x=float(input("Enter x co-ordinate value:\n"))
    y=float(input("Enter y co-ordinate value:\n"))
    r=np.sqrt(x**2+y**2)
    theta=np.arctan2(y,x)
    theta=theta*180/np.pi
    return (r,theta)

def rad_to_car_2d():
    r=float(input("Enter the value of r:\n" ))
    theta=float(input("Enter the value of theta(angle between vec r and x-axis):\n"))
    theta=theta*np.pi/180
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return (x,y)

def cyn_to_car():
    rho=float(input("Enter the value of r:\n" ))
    theta=float(input("Enter the value of theta(angle between vec r and z-axis):\n"))
    z=float(input("Enter the value of z-coordinte:\n"))
    theta=theta*np.pi/180
    x=rho*np.cos(theta)
    y=rho*np.sin(theta)
    return (x,y,z)
def car_to_cyn():
    x=float(input("Enter x co-ordinate value:\n"))
    y=float(input("Enter y co-ordinate value:\n"))
    z=float(input("Enter z co-ordinate value:\n"))
    rho=np.sqrt(x**2+y**2+z**2)
    theta=np.arctan2(y,x)
    #theta=np.arctan2(np.sqrt(x**2+y**2),z)
    theta=theta*180/np.pi
    return (rho, theta, z)

def gradient():
       print("Enter the first point in separated by space")
       p1=np.array(list(map(float,input().split())))
       print("Enter the second point in separated by space")
       p2=np.array(list(map(float,input().split())))
       grad=(p2[0]-p1[0])/(p2[1]-p1[1])
       ang=np.arctan(grad)
       return ("angle and gradient are :",ang,grad)
def pt_from_one_pt():
	print("Enter first point in separated by space")
	p1=np.array(list(map(float,input().split())))
	print("Enter second point in separated by space")
	p2=np.array(list(map(float,input().split())))
	print("Enter the point from which you to find point at certain distance in separated by space")
	p=np.array(list(map(float,input().split())))
	d=float(input("Enter the distance\n"))
	l=(p2[0]-p1[0])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	m=(p2[1]-p1[1])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	n=(p2[2]-p1[2])/np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
	return (p[0]+d*l,p[1]+d*m,p[2]+d*n)
def middle_pt():
	print("Enter the first point in 3D separated by space")
	p1=np.array(list(map(float,input().split())))
	print("Enter the second point in 3D separated by space")
	p2=np.array(list(map(float,input().split())))
	return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2,(p1[2]+p2[2])/2)
def rotation():
	####reference of this code is ###########################
	#### https://en.wikipedia.org/wiki/Rotation_matrix ######
	#theta=float(input("Enter the value of theta\n"))
	#print("Enter the value of vector sepated by space")
	ang=np.array(list(map(float,input("Enter rotation angle around x, y, z-axis separated by space\n").split())))
	vec0=np.array(list(map(float,input("Enter origin vector separated by space\n").split())))
	vec1=np.array(list(map(float,input("Enter vector separated by space\n").split())))
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
def translation():
	tran_vec=np.array(list(map(float,input("enter the translation distance in x, y, z direction sepated by space\n").split())))
	origin_vec=np.array(list(map(float,input("enter the origin vecotor\n").split())))
	return tran_vec+origin_vec
def angle():
	vec1=np.array(list(map(float,input("enter the first vecotor separated by space\n").split())))
	vec2=np.array(list(map(float,input("enter the second vecotor separated by space\n").split())))
	a=np.linalg.norm(vec1)
	b=np.linalg.norm(vec2)
	alpha=np.arccos(np.dot(vec1,vec2)/(a*b))
	alpha=alpha*180/np.pi
	return alpha
def angle_wrt_pt():
	pos0=np.array(list(map(float,input("Enter origin point separated by space\n").split())))
	pos1=np.array(list(map(float,input("Enter first point separated by space\n").split())))
	pos2=np.array(list(map(float,input("Enter second point separated by space\n").split())))
	vec1=pos1-pos0
	vec2=pos2-pos0
	a=np.linalg.norm(vec1)
	b=np.linalg.norm(vec2)
	alpha=np.arccos(np.dot(vec1,vec2)/(a*b))
	alpha=alpha*180/np.pi
	return alpha
