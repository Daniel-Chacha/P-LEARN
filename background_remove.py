from PIL import Image
from rembg import remove

input_name='puppy.jpg'
output_name='puppy.png'

image_input=Image.open(input_name)
image_output=remove(image_input)
image_output.save(output_name)

