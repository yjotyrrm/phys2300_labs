import argparse
from vpython import *
import pandas as pd

class Body:

    def __init__(self,pos,vel,mass,name):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.name = name
        #make a vpython object for this body
        self.ball = sphere(pos = self.pos, radius = 10*10, color = color.yellow)

    #update the position of the vpython wrapper
    def render(self):
        self.ball.pos = self.pos


    #use the leapfrog method to update velocity and position
    def leapfrog_pos(self,step,a):
        self.pos += self.vel*step + .5*a*step**2

    def leapfrog_vel(self,step, a, a1):
        self.vel += .5*(a+a1)*step

    def get_force_vector(self, other):
        """
        :param other: the other object
        :return: a vector representing the force of gravity acting on this object as a result of other
        """
        G = 6.67 * 10**-11
        between = other.pos - self.pos

        #calculate the magnitude of the force
        mag = (G * self.mass * other.mass) / between.mag**3

        #get the unit vector pointing in the direction of between
        dir = between.hat

        #multiply it by magnitude to get the force vector
        force = dir*mag

        return force

    def get_net_accel(self,bodies):
        """

        :param bodies: list of all bodies in the system
        :return: the net acceleration vector on this body
        """
        #make a list of all bodies other than this one
        others = bodies.copy()
        others.remove(self)
        netf = vector(0,0,0)
        for body in others:
            netf += self.get_force_vector(body)

        return netf/self.mass

def get_alist(bodies):
    """

    :param bodies: list of bodies in system
    :return: list of net accelerations for all bodies, same length as bodies
    """
    alist = []
    for body in bodies:
        alist.append(body.get_net_accel(bodies))

    return alist


def update(bodies, step, alist):
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


def mass_center(bodies):
    """

    :param bodies: a list containing all the bodies in the system
    :return: a position and velocity vector, representing the center of mass of the system
    """
    pass

def main():
    """
    """
    #initialize framerate and such
    fps = 100
    steps_per_frame = 10

    parser = argparse.ArgumentParser(description="get the input file")
    parser.add_argument('data')
    args = parser.parse_args()


    with open(args.data) as file:
        data = []
        next(file)
        next(file)

        for line in file:
            data.append(line.split(','))

        file.close()

    # bodge solution for adding mass to situation
    masses = [3.25 * 10.0 ** 23.0,4.867 * 10.0 ** 24.0,6.054 * 10.0 ** 24.0,6.34 * 10.0 ** 23.0,1.898 * 10.0 ** 27.0,5.683 * 10.0 ** 26.0,8.681 * 10.0 ** 25.0,1.024 * 10.0 ** 26.0,1.309 * 10.0 ** 22.0]

    #list of bodies in system
    bodies = []
    data = data[:-1]
    for i, body in enumerate(data):
        bodies.append(Body(vector(float(body[1]),float(body[2]),float(body[3]))*1.496*10**11,vector(float(body[4]),float(body[5]),float(body[6]))*1.496*10**11,masses[i],body[0]))




    #loop over the time inteval
    t = 0
    dt = 1

    alist = get_alist(bodies)
    while dt < 1000:
        rate(fps*steps_per_frame)
        #as the alist for t(n+1) is needed for calculation, I am returning it as alist so that it does not repeat the calculation
        alist = update(bodies, dt, alist)
        print(bodies[0].pos, bodies[0].ball.pos)


if __name__ == "__main__":
    main()