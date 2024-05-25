from captcha.image import ImageCaptcha
import random
from PIL import Image

#image size
image_size=ImageCaptcha(width=400,height=200)

#generating random captcha text
def generate_random_captcha_text(length=6):
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    captcha_text= ''.join(random.choice(characters)  for _ in range(length))
    return captcha_text

#get random captcha text
captcha_text=generate_random_captcha_text()

#get image of given text
data=image_size.generate(captcha_text)

#write image of given file and save it
image_size.write(captcha_text,'CAPTCHA1.png')

Image.open('CAPTCHA1.png')