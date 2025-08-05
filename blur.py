from PIL import Image, ImageFilter

before = Image.open('dsds.png')
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.png")