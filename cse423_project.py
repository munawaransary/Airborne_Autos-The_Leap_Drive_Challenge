from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
car_transition_corrector_width=30
car_transition_corrector_height=0
widthofscreen, heightofscreen = 800,500
gravels=[]
score=0
car_velocity_y = 0
car_upward_jump = False
start=True
tree_speed=4
start_right=755
startleft=745
illusion=True
cloud_shifting=False
shifting_magnitude=0
#car
c_l_l_x=47
c_l_l_y=100
c_u_l_x=47
c_u_l_y=135
c_u_r_x=108
c_u_r_y=135
c_l_r_x=108
c_l_r_y=100
t_l_l_x,t_l_l_y=719,100
t_u_l_x,t_u_l_y=719,178
t_u_r_x,t_u_r_y=774,178
t_l_r_x,t_l_r_y=774,100
power_speed=3
p1,p2=700,100
p3,p4=730,130
p5,p6=730,100
p7,p8=760,130
p9,p10=760,100
p11,p12=790,130
tree_or_power=True

for i in range(800):
        gravels.append((i,random.randint(92,99)))

def draw_line(x1, y1, x2, y2, color): #function ta pore banaabo, apatoto draw line diye kori>>>function done with gl points
    
    glColor3f(*color)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = abs(dy) > abs(dx)
   
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
   
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
   
    d = 2*dy - dx
    y = y1
   
    for x in range(int(x1), int(x2) + 1):
        if steep:
            glBegin(GL_POINTS)
            glVertex2f(int(y), int(x))
            glEnd()
        else:
            glBegin(GL_POINTS)
            glVertex2f(int(x), int(y))
            glEnd()
       
        if d > 0:
            y += 1 if y1 < y2 else -1
            d -= 2*dx
        d += 2*dy
def circle_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)
    
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius
    circle_points(x, y, cx, cy)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        circle_points(x, y, cx, cy)

def ground():
    
    draw_line(0,100,800,100,(1,1,1))
    for i in gravels:
        glBegin(GL_POINTS)
        glVertex2f(i[0],i[1])
        glEnd()
def vehicle():
    global car_transition_corrector_width,car_transition_corrector_height

    draw_line(20+car_transition_corrector_width,110+car_transition_corrector_height,75+car_transition_corrector_width,110+car_transition_corrector_height,(1,1,1))#nicher straight line
    draw_line(20+car_transition_corrector_width,110+car_transition_corrector_height,20+car_transition_corrector_width,120+car_transition_corrector_height,(1,1,1))#left er attached line
    draw_line(75+car_transition_corrector_width,110+car_transition_corrector_height,75+car_transition_corrector_width,120+car_transition_corrector_height,(1,1,1))#right er attached line
    draw_line(20+car_transition_corrector_width,120+car_transition_corrector_height,30+car_transition_corrector_width,120+car_transition_corrector_height,(1,1,1))#left er attached line to the right
    draw_line(30+car_transition_corrector_width,120+car_transition_corrector_height,30+car_transition_corrector_width,130+car_transition_corrector_height,(1,1,1))#to the right
    draw_line(75+car_transition_corrector_width,120+car_transition_corrector_height,65+car_transition_corrector_width,120+car_transition_corrector_height,(1,1,1))#right er attached line to the left
    draw_line(65+car_transition_corrector_width,120+car_transition_corrector_height,65+car_transition_corrector_width,130+car_transition_corrector_height,(1,1,1))#to the left
    draw_line(30+car_transition_corrector_width,130+car_transition_corrector_height,65+car_transition_corrector_width,130+car_transition_corrector_height,(1,1,1))#head

    draw_line(c_l_l_x,c_l_l_y,c_u_l_x,c_u_l_y,(0,0,0))
    draw_line(c_u_l_x,c_u_l_y,c_u_r_x,c_u_r_y,(0,0,0))
    draw_line(c_l_r_x,c_l_r_y,c_u_r_x,c_u_r_y,(0,0,0))
    draw_line(c_l_r_x,c_l_r_y,c_l_l_x,c_l_l_y,(0,0,0))
    # draw_line()
    # draw_line()
    # pass
def bird():
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)
    # glBegin(GL_POINTS)
    # for i in range(6):
    #     mid_circle(300,380,i)#birdhead

    # glEnd()
    draw_line(305, 380, 320, 380, (.447, 1, .973))
    draw_line(305, 380, 318, 388, (.447, 1, .973))
    draw_line(318, 388, 310, 380, (.447, 1, .973))
    # draw_line(318, 388, 312, 380, (.447, 1, .973))
    # draw_line(289, 380, 295, 380, (.447, 1, .973))
    # draw_line(289, 380, 295, 377, (.447, 1, .973))
    #
    draw_line(310, 380, 310, 370, (.447, 1, .973))
    draw_line(310, 370, 305, 380, (.447, 1, .973))
    # draw_line(290, 380, 310, 380, (.447, 1, .973))
    
    draw_line(318, 380, 320, 375, (.447, 1, .973))
    draw_line(320, 375, 325, 385, (.447, 1, .973))
    draw_line(318, 380, 325, 385, (.447, 1, .973))

def trees():
    global tree_or_power
    if tree_or_power==True:
        global tree_speed
        glEnable(GL_POINT_SMOOTH)
        for i in range(755-tree_speed,745-tree_speed,-1):
            draw_line(i,100,i,130,(165/255, 42/255, 42/255))
        #tree
        
        draw_line(t_u_l_x,t_u_l_y,t_l_l_x,t_l_l_y,(1,1,1))
        draw_line(t_l_r_x,t_l_r_y,t_u_r_x,t_u_r_y,(1,1,1))
        draw_line(t_u_l_x,t_u_l_y,t_u_r_x,t_u_r_y,(1,1,1))
        draw_line(t_l_l_x,t_l_l_y,t_l_r_x,t_l_r_y,(1,1,1))
        # draw_line
        glColor3f(0, 1, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex2f(750-tree_speed,140)
        glVertex2f(735-tree_speed,145)
        glVertex2f(765-tree_speed,145)
        glVertex2f(750-tree_speed,150)
        glVertex2f(750-tree_speed,166)

        glEnd()


    # Drawing lines with updated coordinates
    else:
        glPointSize(3)
        draw_line(p1, p2, p3, p4, (0, 0, 1))
        draw_line(p3, p4, p5, p6, (0, 1, 0))
        draw_line(p5, p6, p7, p8, (1, 0, 0))
        draw_line(p7, p8, p9, p10, (0, 0, 1))
        draw_line(p9, p10, p11, p12, (1, 0, 0))
  
def clouds():
    global cloud_shifting,score,shifting_magnitude
    # shifting_magnitude=0
    

        

    glEnable(GL_POINT_SMOOTH)
    glColor3f(0, 0, 1)
    glPointSize(20)
    glBegin(GL_POINTS)
    #first phase
    glVertex2f(100+shifting_magnitude,450)
    glVertex2f(120+shifting_magnitude,450)
    glVertex2f(140+shifting_magnitude,450)
    glVertex2f(110+shifting_magnitude,460)
    glVertex2f(130+shifting_magnitude,460)
    #second phase
    glVertex2f(100+200+shifting_magnitude,450-20)
    glVertex2f(120+200+shifting_magnitude,450-20)
    glVertex2f(140+200+shifting_magnitude,450-20)
    glVertex2f(110+200+shifting_magnitude,460-20)
    glVertex2f(130+200+shifting_magnitude,460-20)
    #third phase
    glVertex2f(100+400+shifting_magnitude,450-60)
    glVertex2f(120+400+shifting_magnitude,450-60)
    glVertex2f(140+400+shifting_magnitude,450-60)
    glVertex2f(110+400+shifting_magnitude,460-60)
    glVertex2f(130+400+shifting_magnitude,460-60)
    glEnd()
def update():
    global tree_speed,shifting_magnitude, t_l_l_x,t_u_l_x,t_u_r_x,t_l_r_x,t_u_r_y,c_l_l_x,c_l_l_y
    global c_l_r_x,c_l_r_y,c_u_l_x,c_u_l_y,c_u_r_x,c_u_r_y,score,start,tree_or_power
    if tree_or_power==True:
        if start==True:
            if tree_speed>=750:
                tree_speed=4
                t_l_l_x,t_l_l_y=719,100
                t_u_l_x,t_u_l_y=719,178
                t_u_r_x,t_u_r_y=774,178
                t_l_r_x,t_l_r_y=774,100
                tree_or_power=not tree_or_power
            tree_speed+=4
            t_l_l_x-=4
            t_u_l_x-=4
            t_u_r_x-=4
            t_l_r_x-=4
            if ((c_l_l_x<=t_l_l_x<=c_l_r_x) or (c_l_l_x<=t_l_r_x<=c_l_r_x)) and ((c_l_r_y>=t_u_r_y)):
                score+=1
                if score%29==0:
                    print(int(score/29))
                    if score%2==0:
                        if shifting_magnitude==720:
                            shifting_magnitude-=720
                        shifting_magnitude+=40
                        print(shifting_magnitude,"sm")
            elif ((c_l_l_x<=t_l_l_x<=c_l_r_x) or (c_l_l_x<=t_l_r_x<=c_l_r_x)) and ((c_l_r_y<=t_u_r_y)):
                print("game over")
                start=False
    else:
        global power_speed, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12
        if start==True:

                # Incrementing x-coordinates for horizontal movement
            p1 -= power_speed
            p3 -= power_speed
            p5 -= power_speed
            p7 -= power_speed
            p9 -= power_speed
            p11 -= power_speed
        if p11 < 0 or p1< 0 :
            p1 =700
            p3 = 730
            p5 = 730
            p7 =760
            p9 = 769
            p11 =790 
            tree_or_power=not tree_or_power
def display():
    global car_transition_corrector_width, car_transition_corrector_height, car_velocity_y, car_upward_jump,c_l_l_y,c_u_l_y,c_u_r_y,c_l_r_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range(5):
        mid_circle(35+car_transition_corrector_width, 106+car_transition_corrector_height, i)
        mid_circle(60+car_transition_corrector_width,106+car_transition_corrector_height,i)

    glEnd()
    if car_upward_jump:
        car_transition_corrector_height += car_velocity_y
        c_l_l_y+=car_velocity_y
        c_u_l_y+=car_velocity_y
        c_u_r_y+=car_velocity_y
        c_l_r_y+=car_velocity_y
        car_velocity_y -= 0.2  # Adjust the gravity effect as needed

        if car_transition_corrector_height <= 0:
            car_transition_corrector_height = 0
            car_upward_jump = False
            car_velocity_y = 0
    ground()
    vehicle()
    trees()
    bird()
    clouds()
    update()
    glutSwapBuffers()


def keyboard(key, x, y):
    global car_transition_corrector_height, car_velocity_y, car_upward_jump

    if key == b' ' and not car_upward_jump:
        car_upward_jump = True
        car_velocity_y = 9  # Adjust the jump height as needed



def animation():
    time = glutGet(GLUT_ELAPSED_TIME) / 1000.0  # Convert milliseconds to seconds
    glutPostRedisplay()
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(widthofscreen, heightofscreen)
glutCreateWindow(b"Assignment 2")
glOrtho(0, widthofscreen, 0, heightofscreen, -1, 1)
glClearColor(0, 0, 0, 1)
# glutDisplayFunc(lambda: display(glutGet(GLUT_ELAPSED_TIME) / 1000.0))
# glutIdleFunc(animation)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutIdleFunc(display)
glutDisplayFunc(display)
glutIdleFunc(display)
glutMainLoop()