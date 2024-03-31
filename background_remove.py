from PIL import Image
from rembg import remove

input_name='/home/daniel/Documents/P LEARN/puppy.jpg'
output_name='/home/daniel/Documents/P LEARN/puppy.png'

image_input=Image.open(input_name)
image_output=remove(image_input)
image_output.save(output_name)

