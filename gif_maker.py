# GIF in Python

import imageio

filenames = ['gif_1.png', 'gif_2.png']
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('gif.gif', images, duration=0.5, loop=0)
