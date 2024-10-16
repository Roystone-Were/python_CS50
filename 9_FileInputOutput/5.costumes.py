import sys  # Import the sys module to handle command-line arguments

from PIL import Image  # Import the Image class from the PIL (Pillow) library for image handling

images = []  # Initialize an empty list to store the images

# Loop through the command-line arguments starting from the second argument (since the first is the script name)
for arg in sys.argv[1:]:
    image = Image.open(arg)  # Open each image file specified in the command-line arguments
    images.append(image)  # Append the opened image object to the 'images' list
    
# The Two images are 'costume1.py' and 'costume2.py' which are embeded in the folder you are working on right now
# - save_all=True: Save all frames (required for saving multiple frames in a GIF)
# - append_images=[images[1]]: Append the second image to the GIF
# - duration=200: Set the duration for each frame to 200 milliseconds
# - loop=0: Set the GIF to loop infinitely
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
''' 
In The Command line you run this argument
👉python costumes.py costume1.gif costume2.gif 

then it will create a new file # costume.py
and if you open the file it will be animated
'''