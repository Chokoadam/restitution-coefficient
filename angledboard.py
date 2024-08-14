#Adam Vasquez
scene.forward = vector(0, -0.1, -1)

phideginput = float(input('Enter the angle of the board:')) #Angles used in this experiment were 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
phideg = 90 - phideginput #Converts the angle to an angle adequate for the angle of the board
phi = (phideg * pi) / 180 #Converts degrees to radians
phi2 = (phideginput * pi) / 180  #Converts the original degree input to radians

mybox = box(pos=vec(0, 0, 0), size=vec(0.5, 0.005, 0.5), axis=vec(sin(phi), -cos(phi), 0), color=color.yellow) #Initialization of the wooden plank object used in the experiment, tilted on the axis depending on value phi
ball = sphere(pos=vec(0, 0.22, 0), radius=0.05, color=color.red, make_trail=True) #Initialization of ball object used in the experiment
ball.velocity = vec(0, -0.0000000001, 0) #Sets velocity ball, the vertical velocity is set to a really small number because if it was 0, the while loop later on would not work
ball.acceleration = vec(0, -9.79, 0)

restitutionC = 0.354945 #Lines 16-23, initiliazes air drag constants used to take account for air drag of the ball
rho = 1.2
diameter = 0.025
A = (pi * (diameter / 2) ** 2)
Cd = 0.47
m = 0.0096
g = 9.79
k = 0.5 * rho * A * Cd

dt = 0.0000001 #Sets precision of while loop
phif = atan(tan(phi2) / restitutionC) #Calculates the angle at which the ball bounces off the board
phifdeg = (180 / pi) * phif #Converts the angle at which the ball bounces off the board from radians to degrees
t = vec(cos((pi/2)-phif), sin((pi/2)-phif), 0)  #Unit vector in the direction tangent to the surface of the board at the point of contact.
n = vec(-sin((pi/2)-phif), -cos((pi/2)-phif), 0) #Unit vector in the direction normal (perpendicular) to the surface of the board at the point of contact

while mag(ball.velocity) > 1e-11: #while to simulate the dropping motion of the ball, the loop stops if the velocity becomes less than 1e-11
    rate(1 / dt) #Determines the rate at which the ball falls
    oldVelocity = ball.velocity.y #Used to determine the point at which the ball is on its way down after going bouncing up
    ball.acceleration = vec(0, -g, 0) - (k / m) * mag(ball.velocity) * ball.velocity #Calculates acceleration while taking account for air drag
    ball.pos = ball.pos + ball.velocity * dt #Calculates the position of the ball while in motion
    ball.velocity = ball.velocity + ball.acceleration * dt #Calculates the velocity of the ball while in motion

    if ball.pos.y < mybox.pos.y: #If the ball reaches the surface of the wooden plank, simulate bouncing motion of the ball
        ball.pos.y = abs(ball.pos.y) #Once the ball bounces, it makes sure the ball stays above the board and does not drop below the wooden plank
        v_normal = dot(ball.velocity, n) * n #Calculates the dot product between the ball's velocity vector and the normal vector
        v_tangent = ball.velocity - v_normal #The component of the ball's velocity that is tangent to the surface of the wooden plank

        # Use the reflection formula for elastic collisions to update the velocity
        ball.velocity = restitutionC * v_tangent - v_normal #The ball loses velocity based on the restitution coefficient, and tangent and normal vectors from before determines the direction of motion of the bouncing ball

    if ball.velocity.y < 0 and oldVelocity > 0: #This condition is met once the ball bounces once and when the ball is on it's way down, this is done whenever the previous velocity is positive and when the current velocity of the ball is negative
        print('The angle of the ball after bouncing on the wooden board is ', phifdeg) #Prints out the angle at which the ball bounced at
        ball.velocity.y = 0 #Lines 46-47, stops the while loop by setting the ball's velocity to 0
        ball.velocity.x = 0

  
