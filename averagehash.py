from PIL import Image

# Open the image file
input_image = Image.open("scaryhackerguy.jpg")

# Convert the image to grayscale
grayscale_image = input_image.convert('L')

# Resize the grayscale image to 8x8
resized_image = grayscale_image.resize((8, 8))

width, height = resized_image.size

# sum grayscale values in image
grayscale_sum = 0
for y in range(height):
    for x in range(width):
        color = resized_image.getpixel((x, y))
        grayscale_sum += color

# get mean of these grayscale values
grayscale_mean = grayscale_sum / (width * height)

hash = ""

# set each pixel grayscale values according to grayscale_mean
for y in range(height):
    for x in range(width):
        color = resized_image.getpixel((x, y))
        if color > grayscale_mean:
            # set this pixel to white, this will be a 1 in the hash
            resized_image.putpixel((x, y), 255)
            hash += "1"
        else:
            # set this pixel to black, this will be a 0 in the hash
            resized_image.putpixel((x, y), 0)
            hash += "0"

print("Binary hash:")
print(hash)

# convert binary hash to hexadecimal
hex_hash = hex(int(hash, 2))
# remove the 0x from the string
hex_hash = hex_hash[2:]

print("Hexadecimal hash:")
print(hex_hash)

resized_image.save("hashedimage.jpg")


