#Adam Vasquez
scene.forward = vector(0,-0.1,-1)


phideg = 90 #Sets angle of the board that makes sense in the experimental setup. In this case, 90 degrees = 0 degrees of the board
phi = phideg*pi/180 #converts degrees to radians


mybox = box(pos=vec(0,0,0), size=vec(1,0.005,1), axis=vec(sin(phi),-cos(phi),0), color=color.yellow) #The wooden board used in the experiment
hi = float(input('Enter initial height of drop:')) #Initial heights used in the experiment are .1, .14, .18, .22, .26, .30, .34, .38, .42, .46
ball= sphere(pos=vec(0,hi,0), radius=.05, color=color.red, make_trail=True)
ball.velocity=vec(0,-0.0000000001,0)
ball.acceleration=vec(0,-9.79,0)

restitutionC = 0.354945 #e (restitutiton coefficient)=0.354945
rho = 1.2 #Lines 19-25, constant variables to take into account for air drag 
diameter = 0.025
A = (pi*(diameter/2)**2)
Cd = 0.47
m = 0.0096
g = 9.79
k = (.5)*rho*A*Cd

dt=0.0000001 #precision of the while loop

while mag(ball.velocity) > 1e-11:  #repeats the free fall motion until the vertical velocity of the ball falls really close to 0
  rate(1/dt) 
  oldVelocity = ball.velocity.y #used to determine the exact moment when the ball reaches it's maximum height after bouncing once (as seen in line 35)
  ball.acceleration = vec(0,-g,0) - (k/m)*mag(ball.velocity)*ball.velocity #acceleration due to air drag
  ball.pos=ball.pos+ball.velocity*dt #kinematics
  ball.velocity=ball.velocity + ball.acceleration*dt #kinematics
  if ball.pos.y<mybox.pos.y: #when the ball reaches the board, bounce the ball pack up with a velocity that is decreased due to the restitution coefficient of the baord.
    ball.pos.y=abs(ball.pos.y) #brings the ball above the plank of wood
    ball.velocity.y= -restitutionC*ball.velocity.y
  if ball.velocity.y < 0 and oldVelocity > 0: #when the ball reaches it's maximum height after bouncing once, record and tell the user the height it reached and stop the loop by equaling the vertical velocity to 0
    heightF = ball.pos.y
    print('The max height of the ball after it bounces is ',heightF, ' m.')
    ball.velocity.y = 0
  
    
    
