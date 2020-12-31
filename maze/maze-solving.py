from classes.Node import DijkstraSolver
from pprint import pprint
from PIL.Image import fromarray
import numpy as np
from classes.Maze import Maze
import sys

sys.setrecursionlimit(100000)

if __name__ == "__main__":
    # maze = Maze("./maze.png", output_image=True, threaded=False)
    #maze = Maze("./maze.png", output_image=True, threaded=True)

    # maze = Maze("./perfect2k.png", threaded=False)
    maze: Maze = Maze("./perfect15k.png",  threaded=False)

    # maze.solve_dikstra(recursive = False)
    maze.solve(DijkstraSolver())
    print("done")
