from PIL import Image, ImageFilter

filename = "wolta.jpg"
with Image.open(filename) as img:
    img.load()

img.show()
width, height = img.size

format = img.format

mode = img.mode

print("Ширинyа: ", width)
print("Высота:  ", height)
print("Формат: ", format)
print("Цветовая модель:", mode)