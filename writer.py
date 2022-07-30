from PIL import Image
import sys
import base64
import os

def encode(string):    
    base64_bytes = base64.b64encode(string.encode("utf-8"))
    return base64_bytes.decode("utf-8")

def split(string):
    return [char for char in string]

base64_chars = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z",
"0","1","2","3","4","5","6","7","8","9","+","/","=" ]

if os.path.exists(sys.argv[2]):
    with open(sys.argv[2], 'r') as f:
        read_text = f.read()
else:
    read_text = sys.argv[2]

im = Image.new('RGBA', (len(encode(read_text)) + 2, 66))
x_max = im.width # need to subtract one pixel from this since color space counts from 1 instead of 0
y_max = im.height - 1 #
start_y = y_max - 1

chars = []
for item in split(encode(read_text)):
    chars.append(int(item.replace(item, str(base64_chars.index(item) + 1 ))))

for x_pixel in range(1, x_max - 1):
    y_pix = start_y
    for pixls in range(0, chars[x_pixel - 1]):
        im.putpixel((x_pixel, y_pix), (0,0,0, 255))
        y_pix -= 1

print("pix-height:", chars)
print("\ntext:", read_text)
im.save(sys.argv[1])
