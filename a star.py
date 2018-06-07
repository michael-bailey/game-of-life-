from PIL import Image
import numpy as np
image = Image.open("maze.bmp","r")
universe = np.array(image)
print(universe)