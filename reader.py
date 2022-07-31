from PIL import Image
import sys
import base64

def decode(string):    
    sample_string_bytes = base64.b64decode(string.encode("utf-8"))
    return sample_string_bytes.decode("utf-8")

def listToString(string): 
    str1 = "" 
    for ele in string: 
        str1 += ele  
    return str1

im = Image.open(sys.argv[1],'r')

black = ( 0,0,0,255 )

base64_chars = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z",
"0","1","2","3","4","5","6","7","8","9","+","/","=" ]

char_list = []
x_max = im.width - 1 # need to subtract one pixel from this since color space counts from 1 instead of 0
y_max = im.height - 1 #
start_y = y_max - 1

for x_pixel in range(0,x_max):
    current_color = im.getpixel( (x_pixel, start_y) )

    if current_color == black:

        char_num = 1
        pixel_up_y = start_y - 1

        while (im.getpixel( (x_pixel, pixel_up_y ) ) == black ):
            pixel_up_y -= 1
            char_num += 1

        char_list.append(char_num)

if '-c' not in sys.argv:
    print('pix-height: ', char_list)

for index,item in enumerate(char_list):
    char_list[index] = base64_chars[item - 1]

if '-c' not in sys.argv:
    print('\ntext:', decode(listToString(char_list)))
else:
    print(decode(listToString(char_list)))
