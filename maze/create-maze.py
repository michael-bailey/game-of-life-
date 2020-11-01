import PIL.Image as p
import numpy as np

if __name__ == "__main__":
    maze = np.array([
        [0,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,1,0,1,0,0],
        [0,1,1,1,0,1,0,0],
        [0,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,1,0],
    ])

    img = p.fromarray((maze*255).astype(np.uint8)).convert("1")
    img.save("./maze.png", mode="L")
