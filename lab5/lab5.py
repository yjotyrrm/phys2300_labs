from vpython import *
from matplotlib import pyplot as plt
from math import sin, cos
import argparse
import math


def set_scene(data):
    """
    Set Vpython Scene
    """
    scene.title = "Assignment 5: Projectile motion"
    scene.width = 800
    scene.heigth = 600
    scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
    To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
    Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
    scene.forward = vector(0, -.3, -1)
    scene.x = -1
    # Set background: floor, table, etc
    floor = box(pos = vector(0,0,0), length = 3000, width = 20, height = .1, color = color.white)

def motion_no_drag(data):
    """
    Create animation for projectile motion with no dragging force
    """
    ball_nd = sphere(pos=vector(-25, data['init_height'], 0),
                        radius=1, color=color.cyan, make_trail=True)
    # Follow the movement of the ball
    scene.camera.follow(ball_nd)
    # Set initial velocity & position
    ball_nd.theta = math.radians(data['theta'])
    ball_nd.mag = data['init_velocity']
    ball_nd.vy = ball_nd.mag * math.sin(ball_nd.theta)
    ball_nd.vx = ball_nd.mag * math.cos(ball_nd.theta)
    ball_nd.v = vector(ball_nd.vx,ball_nd.vy,0)
    # Animate
    while ball_nd.pos.y > 0:
        rate(1/data['deltat'])
        g = vector(0,data['gravity']*data['deltat'],0)
        data['nd_pos_x'].append(ball_nd.pos.x)
        data['nd_pos_y'].append(ball_nd.pos.y)
        ball_nd.v += g
        ball_nd.pos += ball_nd.v




def motion_drag(data):
    ball_d = sphere(pos=vector(-25, data['init_height'], 0),
                     radius=1, color=color.red, make_trail=True)

    ball_d.theta = math.radians(data['theta'])
    ball_d.mag = data['init_velocity']
    ball_d.vy = ball_d.mag * math.sin(ball_d.theta)
    ball_d.vx = ball_d.mag * math.cos(ball_d.theta)
    ball_d.v = vector(ball_d.vx, ball_d.vy, 0)

    while ball_d.pos.y > 0:
        rate(1/data['deltat'])
        g = vector(0,data['gravity']*data['deltat'],0)

        d_mag = data['beta']

        data['d_pos_x'].append(ball_d.pos.x)
        data['d_pos_y'].append(ball_d.pos.y)
        #adding pi to an angle in radians turns around, by rotating it 180 degrees.
        d_y = d_mag * math.sin(ball_d.theta + math.pi)
        d_x = d_mag * math.cos(ball_d.theta + math.pi)
        d = vector(d_x, d_y, 0)

        ball_d.v += g
        ball_d.v += d

        ball_d.pos += ball_d.v

def plot_data(data):

    plt.figure()
    plt.plot(data['d_pos_x'],data['d_pos_y'])
    plt.plot(data['nd_pos_x'], data['nd_pos_y'])
    plt.show()



def main():
    """
    """
    # 1) Parse the arguments
    parser = argparse.ArgumentParser(description="get the starting conditions")
    parser.add_argument('velocity', type=float)
    parser.add_argument('angle', type=float)
    parser.add_argument("--height", type=float, default=1.2)
    args = parser.parse_args()
    # Set Variables
    data = {}       # empty dictionary for all data and variables

    data['nd_pos_x'] = []
    data['d_pos_x'] = []
    data['nd_pos_y'] = []
    data['d_pos_y'] = []
    data['init_velocity'] = args.velocity
    data['theta'] = args.angle
    data['init_height'] = args.height

    print(data['init_velocity'])
    print(data['theta'])
    print(data['init_height'])
    # Constants
    data['rho'] = 1.225  # kg/m^3
    data['Cd'] = 0.5    # coefficient friction
    data['deltat'] = 0.005
    data['gravity'] = -9.8  # m/s^2

    data['ball_mass'] = 0.145  # kg
    data['ball_radius'] = 0.075  # meters
    data['ball_area'] = pi * data['ball_radius']**2
    data['alpha'] = data['rho'] * data['Cd'] * data['ball_area'] / 2.0
    data['beta'] = data['alpha'] / data['ball_mass']
    # Set Scene
    set_scene(data)
    # 2) No Drag Animation
    motion_no_drag(data)
    # 3) Drag Animation
    motion_drag(data)
    # 4) Plot Information: extra credit
    plot_data(data)


if __name__ == "__main__":
    main()
    exit(0)
