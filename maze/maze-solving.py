from pprint import pprint
from PIL.Image import fromarray
import numpy as np
from classes.Maze import Maze

if __name__ == "__main__":
    maze = Maze("./maze.png", output_image=True)
    maze.solve_dikstra()

    #twoThousand = Maze("./perfect2k.png", output_image=True, verbose=True)
    #fithteenThoushand = Maze("./perfect15k.png", output_image=True)

    print("done")