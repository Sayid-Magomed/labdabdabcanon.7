from PIL import Image, ImageFilter
filename = "wolta.jpg"
with Image.open(filename) as img:
    img.load()

new_img = img.resize((img.width // 3, img.height // 3))

new_img.save("resized_wolta.jpg")

converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("image_flipwolta_top.jpg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("image_flip_wolta.jpg")
