from vpython import *

class body:

    def __init__(self):
        self.ball = sphere(pos = vector(0,0,0), radius = 1, color = color.yellow)

def main():

    ball = body()

if __name__ == "__main__":
    main()