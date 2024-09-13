from PIL import Image
import requests

image = Image.open('photo.jpeg')

resized_image = image.resize((960, 800))

def sepia(image):
    image = image.convert('RGB')
    sepia_filter = (0.393, 0.769, 0.189)
    for i in range(image.height):
        for j in range(image.width):
            r, g, b = image.getpixel((j, i))
            sepia_r = min(int(r * sepia_filter[0] + g * sepia_filter[1] + b * sepia_filter[2]), 255)
            sepia_g = min(int(r * sepia_filter[0] + g * sepia_filter[1] + b * sepia_filter[2]), 255)
            sepia_b = min(int(r * sepia_filter[0] + g * sepia_filter[1] + b * sepia_filter[2]), 255)
            image.putpixel((j, i), (sepia_r, sepia_g, sepia_b))
    return image

sepia_image = sepia(resized_image)

sepia_image.save('sepia_resized.png')


url = 'https://yandex.ru/pogoda/chelyabinsk'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f'Ошибка: {response.status_code}')