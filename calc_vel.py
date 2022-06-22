#vel__fit.py
#calculates rotation curve using radio telescope doppler shift data
#dschultz, June 2022

import read_params
import math

radius=[0]
velocity=[0]
degtorad=3.14159/180.0
lytokpc=1/3260.0
pi=3.14159

#Read parameter file
solar_params=read_params.solar_params()
solar_radius=float(solar_params[0])*lytokpc  #converts to kpc
solar_velocity=float(solar_params[1])
inner_params=read_params.inner_params()
NI=int((len(inner_params))/2)  #total number of inner points
outer_params=read_params.outer_params()
NO=int((len(outer_params))/3)  #total number of outer points

#Inner points, quadrant 1
print("inner points, quadrant 1")
for i in range(NI):
    Q1=[0]
    Q1.append(inner_params[i*2])
    Q1.append(inner_params[i*2+1])
    Q1.pop(0)
    print(Q1)
    #calculate velocity using tangent point method
    gallon_rads=float(Q1[0])*degtorad
    radius.append(solar_radius*math.sin(gallon_rads))
    velocity.append(float(Q1[1])+solar_velocity*(math.sin(gallon_rads)))
#next i
radius.append(solar_radius)      #add solar radius
velocity.append(solar_velocity)  #add solar velocity
print(" ")

#Outer points, quadrants 1 & 2
print("outer points, quadrants 1 and 2")
for i in range(NO):
    Q12=[0]
    j=int(outer_params[i*3])
    if j<180:
        Q12.append(outer_params[i*3])
        Q12.append(outer_params[i*3+1])
        Q12.append(outer_params[i*3+2])
        Q12.pop(0)
        print(Q12)
        #calculate velocity using trigonometry
        gallon_rads=float(Q12[0])*degtorad
        radius_kpc=float(Q12[1])*lytokpc
        vel_dop_shf=float(Q12[2])
        b5=gallon_rads
        b11=solar_velocity
        a11=vel_dop_shf
        a8=radius_kpc
        b8=solar_radius
        c5=math.asin( (b8/a8)*math.sin(2*pi-b5)  )
        b14=b11*math.sin(b5)
        c8=0.5*pi-c5
        a14=-1*(a11+b14)/math.cos(c8)
        radius.append(radius_kpc)      
        velocity.append(a14)
    #next i
print(" ")

#Outer points, quadrant 3
print("outer points, quadrant 3")
for i in range(NO):
    Q3=[0]
    j=int(outer_params[i*3])
    if j>180:
        Q3.append(outer_params[i*3])
        Q3.append(outer_params[i*3+1])
        Q3.append(outer_params[i*3+2])
        Q3.pop(0)
        print(Q3)
        #calculate velocity using trigonometry
        gallon_rads=float(Q3[0])*degtorad
        radius_kpc=float(Q3[1])*lytokpc
        vel_dop_shf=float(Q3[2])
        f5=gallon_rads
        f8=solar_radius
        e8=radius_kpc
        g5=math.asin((f8/e8)*math.sin(2*pi-f5))
        g8=0.5*pi-g5
        e11=vel_dop_shf
        f11=solar_velocity
        f14=f11*math.cos(1.5*pi-f5)
        e14=(f14-e11)/math.cos(g8)
        radius.append(radius_kpc)
        velocity.append(e14)
    #next i
print(" ")
radius.pop(0)
velocity.pop(0)
print("Radius(kpc)")
print(radius)
print(" ")
print("Velocity (km/s)")
print(velocity)

#Plot velocity versus radius
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig=plt.figure(figsize=(10,6))
ax=plt.axes()
ax.set_title("Velocity vs Radius")
ax.set_xlabel("Radius (kpc)")
ax.set_xlim(2,16)
ax.set_xticks([2,4,6,8,10,12,14,16])
ax.set_ylabel("Velocity (km/s)")
ax.set_ylim(0,400)
ax.set_yticks([0,50,100,150,200,250,300,350,400])
ax.scatter(radius,velocity,c="red")
plt.grid()
plt.show()

exit()

 
