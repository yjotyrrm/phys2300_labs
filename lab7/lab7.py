import argparse
from vpython import *


class Body:

    def __init__(self,pos,vel,mass,name, radius):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.name = name
        self.radius = radius
        #make a vpython object for this body
        self.ball = sphere(pos = self.pos, radius = self.radius, color = color.yellow, make_trail = True)

    #update the position of the vpython object
    def render(self):
        self.ball.pos = self.pos
        pass


    #use the leapfrog method to update velocity and position
    def leapfrog_pos(self,step,a):
        self.pos += self.vel*step + .5*a*step**2

    def leapfrog_vel(self,step, a, a1):
        self.vel += .5*(a+a1)*step

    def get_accel_vector(self, other):
        """
        :param other: the other object
        :return: a vector representing the acceleration due to gravity acting on this object as a result of other
        """
        #this is g converted to au^3/kg*s, rather than m^3/kg*s, since aus are the units I'm using
        G =1.36*10**-34
        between = other.pos - self.pos

        mag = (G * other.mass) / between.mag**2



        dir = between.hat

        accel = dir*mag

        return accel

    def get_net_accel(self,bodies):
        """

        :param bodies: list of all bodies in the system
        :return: the net acceleration vector on this body
        """
        #make a list of all bodies other than this one
        others = bodies.copy()

        if self in others:
            others.remove(self)
        netaccel = vector(0,0,0)
        for body in others:
            netaccel += self.get_accel_vector(body)

        return netaccel

def get_alist(bodies):
    """

    :param bodies: list of bodies in system
    :return: list of net accelerations for all bodies, same length as bodies
    """
    alist = []

    for body in bodies:
        alist.append(body.get_net_accel(bodies))

    return alist


def leapfrog_update(bodies, step, alist):
    """

    :param bodies: list of bodies in system
    :param step: length of time step
    :param alist: list of current accelerations
    :return: alist for the next update
    """

    for i,body in enumerate(bodies):
        body.leapfrog_pos(step,alist[i])

    new_alist = get_alist(bodies)

    for i,body in enumerate(bodies):
        body.leapfrog_vel(step, alist[i],new_alist[i])
        body.render()

    return new_alist

def standard_update(bodies, step):
    alist = get_alist(bodies)
    for i, body in enumerate(bodies):
        body.vel += alist[i]
        body.pos += body.vel
        body.render()



def mass_center(bodies):
    """
    calculate the center of mass / center of momentum of the system, and make it so that its initial position and velocity is 0.
    :param bodies: a list containing all the bodies in the system
    """

    total_mass = 0
    weighted_pos = vector(0,0,0)
    weighted_vel = vector(0,0,0)
    for i in bodies:
        weighted_pos += i.pos*i.mass
        weighted_vel += i.vel*i.mass
        total_mass += i.mass

    center_pos = weighted_pos/total_mass
    center_vel = weighted_vel/total_mass

    print(center_pos,center_vel)
    for i in bodies:
        i.pos -= center_pos
        i.vel -= center_vel





def main():
    """
    """
    #initialize framerate and such
    fps = 30
    steps_per_frame = 10

    parser = argparse.ArgumentParser(description="get the input file")
    parser.add_argument('--data', required = True)
    parser.add_argument('--leapfrog', type = bool, default=False)
    parser.add_argument('--visualise', type = bool, default=True)
    args = parser.parse_args()


    with open(args.data) as file:
        data = []
        next(file)
        next(file)

        for line in file:
            data.append(line.split(','))

        file.close()



    #list of bodies in system
    bodies = []
    data = data[:-1]
    for i, body in enumerate(data):
        bodies.append(Body(vector(float(body[1]),float(body[2]),float(body[3])),vector(float(body[4]),float(body[5]),float(body[6])),float(body[7]),body[0],.1))

    #manually add the sun to the simulation
    bodies.append(Body(vector(0,0,0),vector(0,0,0),1.989*10**30,'sun',.2))
    #shift the 0,0 coordinate to be the center of mass of the solar system
    mass_center(bodies)
    mass_center(bodies)
    #loop over the time inteval
    t = 0
    dt = 1
    end_time = 365.25*10**3

    alist = get_alist(bodies)


    if(args.leapfrog):
        print('leapfrog')
        while t < end_time:
            rate(fps * steps_per_frame)
            # as the alist for t(n+1) is needed for calculation, I am returning it as alist so that it does not repeat the calculation
            alist = leapfrog_update(bodies, dt, alist)
            t+=dt


    else:
        print('standard')
        while t < end_time:
            rate(fps * steps_per_frame)
            standard_update(bodies,dt)
            t+=dt


    mass_center(bodies)



if __name__ == "__main__":
    main()