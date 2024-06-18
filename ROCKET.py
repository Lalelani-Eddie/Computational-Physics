##PROGRAM FOR SPACECRAFT
##PHY1004W
##NNXLAL001
## 02 AUGUST 2022



from vpython import*
disk = disk(pos=vector(0,0,0), radius=0.5, color=color.cyan)
rcm = vector(0,0,0)
#rcm = rcm + omega*dt
disk.trail = curve(pos=rcm, color=color.yellow, radius=0.05)

F = 120
theta = 270
omega = 0


vx = gcurve()
vy = gcurve()

thrustpoint=curve(pos=rcm+vector(R*cos(theta),R*sin(theta),0), color=color.green,radius=0.03)
##INITIALISE VARIABLES
dt = 0.005
t = 0.0
rcm = rcm + omega*dt
scene.autoscale = 0
while t < 10.0:
    rate(50)
    vx.plot(pos=(t, pcm.x/M))
    vy.plot(pos=(t, pcm.y/M))
    
    t = t + dt
    Fvector = (F*cos(theta),F*sin(theta),0)
    omega = omega + (F*R/I)*dt
    theta = theta + omega*dt+(F*R/I)*dt
    pcm = pcm + Fvector*dt
    disk.rcm = rcm + omega*dt
    disk.trail.append(pos=rcm)
    
