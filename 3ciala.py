#!/usr/bin/python
from visual import *
from visual.graph import *
import math
scene.width = 700
scene.height = 600
scene.title = 'Zagadnienie trzech cial'
scene.autoscale= False
scene.fullscreen = False

m1 = 6
m2 = 6
m3 = 6
t=0
c=0

e1 = 0.1 
e2 = 0.1 
e3 = 0.1

r1 = e1 
r2 = e2
r3 = e3
G = 4
dt =0.001


pos1 = vector(-2.5001, 0.00001, 0.00001) 
pos2 = vector(0.0001, sqrt(25-(2.5)**2), 0.00001) 
pos3 =vector(2.4999, 0.00001, 0.00001)
v0=vector(0,0,0)

v1= vector(1,-sqrt(3),0)
v2 = vector(-2,0, 0)
v3 = vector(1, sqrt(3), 0)
v1*=1.4
v2*=1.4
v3*=1.4




x1 = arange(-500, 500, 1)
curve(x = x1)
curve(y=x1)
curve(z=x1)

P1 = sphere(pos = pos1, radius = r1, color = color.red)
P2 = sphere(pos = pos2, radius = r2, color = color.green)
P3 = sphere(pos = pos3, radius = r3, color = color.blue)


theta1=asin(P1.pos[2]/mag(P1.pos))
fi1=atan(P1.pos[1]/P1.pos[0])
thetap1=asin(v1[2]/mag(v1))
fip1=atan(v1[1]/v1[0])

theta2=asin(P2.pos[2]/mag(P2.pos))
fi2=atan(P2.pos[1]/P2.pos[0])
thetap2=asin(v2[2]/mag(v2))
fip2=atan(v2[1]/v2[0])

theta3=asin(P3.pos[2]/mag(P3.pos))
fi3=atan(P3.pos[1]/P3.pos[0])
thetap3=asin(v3[2]/mag(v3))
fip3=atan(v3[1]/v3[0])


P1.trail = curve(color = P1.color)
P2.trail = curve(color = P2.color)
P3.trail = curve(color = P3.color)

def sila(p, p_m, m):
    r = p-p_m
    r_mag = mag(r)
    r_norm = norm(r)
    a = (-G*m/(r_mag**2)) * r_norm
    return a
    
pos_graph = gdisplay(x=700, y=0, width=500, height=500, 
             title='Diagram fazowy ciala theta', xtitle='a', ytitle='v', 
             xmax=5, xmin=-5., ymax=5, ymin=-5, 
             foreground=color.white, background=color.black)
pos1x_Plot = gdots(color=color.red, size=1)
pos2x_Plot = gdots(color=color.green, size=1)
pos3x_Plot = gdots(color=color.blue, shape="round", size=1)

pos_graph = gdisplay(x=700, y=500, width=500, height=500, 
             title='Diagram fazowy fi', xtitle='a', ytitle='v', 
             xmax=5, xmin=-5., ymax=5, ymin=-5, 
             foreground=color.white, background=color.black)
pos1y_Plot = gdots(color=color.red, size=1)
pos2y_Plot = gdots(color=color.green, size=1)
pos3y_Plot = gdots(color=color.blue, shape="round", size=1)




    
    
while True:
    rate(500)
    #P1
    a1 = sila(P1.pos, P2.pos, m2) + sila(P1.pos, P3.pos, m3)
    dv1 = a1*dt
    v1 = v1 + dv1
    dp1 = v1*dt
    #P2
    a2 = sila(P2.pos, P1.pos, m1) + sila(P2.pos, P3.pos, m3)
    dv2 = a2*dt
    v2 = v2 + dv2
    dp2 = v2*dt
    #P3
    a3 = sila(P3.pos, P2.pos, m2) + sila(P3.pos, P1.pos, m1)
    dv3 = a3*dt
    v3 = v3 + dv3
    dp3 = v3*dt
    t+=dt
    c+=1
    P1.pos = P1.pos + dp1
    P1.trail.append(pos=P1.pos)
    P2.pos = P2.pos + dp2
    P2.trail.append(pos=P2.pos)
    P3.pos = P3.pos + dp3
    P3.trail.append(pos=P3.pos)
    pos1x_Plot.plot(pos=(thetap1,theta1))
    pos1y_Plot.plot(pos=(fip1,fi1))
    pos2x_Plot.plot(pos=(thetap2,theta2))
    pos2y_Plot.plot(pos=(fip2,fi2))
    pos3x_Plot.plot(pos=(thetap3,theta3))
    pos3y_Plot.plot(pos=(fip3,fi3))
    scene.center = vector((m1*P1.pos[0]+m2*P2.pos[0]+m3*P3.pos[0])/(m1+m2+m3),(m1*P1.pos[1]+m2*P2.pos[1]+m3*P3.pos[1])/(m1+m2+m3),(m1*P1.pos[2]+m2*P2.pos[2]+m3*P3.pos[2])/(m1+m2+m3))
  
    theta1=atan((sqrt(P1.pos[0]**2 + P1.pos[1]**2))/P1.pos[2])
    fi1=atan(P1.pos[1]/P1.pos[0])
    thetap1=(P1.pos[0]*P1.pos[2]*v1[0]+(P1.pos[0]**2)*(-v1[2])+v1[1]*(P1.pos[2]*v1[1]-P1.pos[1]*v1[2]))/(sqrt(P1.pos[0]**2 + P1.pos[1]**2)*(P1.pos[0]*P1.pos[1]*P1.pos[2]))
    fip1=(P1.pos[0]*v1[1]-P1.pos[1]*v1[0])/(P1.pos[0]**2 + P1.pos[1]**2)

    theta2=atan((sqrt(P2.pos[0]**2 + P2.pos[1]**2))/P2.pos[2])
    fi2=atan(P2.pos[1]/P2.pos[0])
    thetap2=(P2.pos[0]*P2.pos[2]*v1[0]+(P2.pos[0]**2)*(-v2[2])+v2[1]*(P2.pos[2]*v2[1]-P2.pos[1]*v2[2]))/(sqrt(P2.pos[0]**2 + P2.pos[1]**2)*(P2.pos[0]*P2.pos[1]*P2.pos[2]))
    fip2=(P2.pos[0]*v2[1]-P2.pos[1]*v2[0])/(P2.pos[0]**2 + P2.pos[1]**2)
    
    theta3=atan((sqrt(P3.pos[0]**2 + P3.pos[1]**2))/P3.pos[2])
    fi3=atan(P3.pos[1]/P3.pos[0])
    thetap3=(P3.pos[0]*P3.pos[2]*v3[0]+(P3.pos[0]**2)*(-v3[2])+v3[1]*(P3.pos[2]*v3[1]-P3.pos[1]*v3[2]))/(sqrt(P3.pos[0]**2 + P3.pos[1]**2)*(P3.pos[0]*P3.pos[1]*P3.pos[2]))
    fip3=(P3.pos[0]*v3[1]-P3.pos[1]*v3[0])/(P3.pos[0]**2 + P3.pos[1]**2)
  #  if  mag(P1.pos-P2.pos)<(r1+r2) or mag(P1.pos-P3.pos)<(r1+r3) or (mag(P3.pos-P2.pos)<(r3+r2)):
   #     print "Collision !?"
    #    break

#print "...finish"













