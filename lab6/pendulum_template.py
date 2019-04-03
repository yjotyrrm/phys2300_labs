import numpy as np
from matplotlib import pyplot as plt
from vpython import *
import argparse

g = 9.81    # m/s**2
l = 0.1     # meters
W = 0.002   # arm radius
R = 0.01     # ball radius
framerate = 30
steps_per_frame = 10

def f(r):
    """
    Pendulum
    """
    theta = r[0]
    omega = r[1]
    # the expression omega - c*omega becomes (1-c) * omega, since c is a constant I simplified
    ftheta = omega
    fomega = -(g/l)*np.sin(theta) - .05*omega
    return np.array([ftheta, fomega], float)

def runga_kutta(h,r):
    k1 = h * f(r)
    k2 = h * f(np.array([r[0] + .5 * k1[0], r[1] + .5 * k1[1]], float))
    k3 = h * f(np.array([r[0] + .5 * k2[0], r[1] + .5 * k2[1]], float))
    k4 = h * f(np.array([r[0] + k3[0], r[1] + k3[1]], float))

    return (k1 + 2*k2 + 2*k3 + k4)/6

def main():
    """
    """
    # Set up initial values
    h = 1.0/(framerate * steps_per_frame)
    r1 = np.array([179*np.pi/180, 0], float)
    r2 = np.array([170*np.pi/180,0],float)
    # Initial x and y
    x1 = l*np.sin(r1[0])
    y1 = -l*np.cos(r1[0])

    x2 = l * np.sin(r2[0])
    y2 = -l * np.cos(r2[0])

    string1 = cylinder(pos = vector(0,0,0), axis = vector(x1,y1,0), radius = W, color = color.cyan)
    ball1 = sphere(pos = vector(x1,y1,0), radius = R, color = color.cyan)

    string2 = cylinder(pos=vector(0, 0, 0), axis=vector(x2, y2, 0), radius=W, color=color.red)
    ball2 = sphere(pos=vector(x2, y2, 0), radius=R, color=color.red)
    # Loop over some time interval
    dt = 0.01
    t = 0
    while t < 50:
        rate(framerate)
        # Use the 4'th order Runga-Kutta approximation
        for i in range(steps_per_frame):

            r1 += runga_kutta(h,r1)
            r2 += runga_kutta(h,r2)

        t += dt
        # Update positions
        x1 = l*np.sin(r1[0])
        y1 = -l*np.cos(r1[0])

        x2 = l * np.sin(r2[0])
        y2 = -l * np.cos(r2[0])
        # Update the cylinder axis
        string1.axis = vector(x1,y1,0)
        string2.axis = vector(x2,y2,0)
        # Update the pendulum's bob
        ball1.pos = vector(x1,y1,0)
        ball2.pos = vector(x2,y2,0)

if __name__ == '__main__':
    main()