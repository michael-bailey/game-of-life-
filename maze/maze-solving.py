from pprint import pprint
from PIL.Image import fromarray
import numpy as np
from classes.Maze import Maze

if __name__ == "__main__":
    #maze = Maze("./maze.png", output_image=True)

    maze = Maze("./perfect2k.png", output_image=True, verbose=True)
    #maze = Maze("./perfect15k.png")
    maze.solve_dikstra()
    print("done")
