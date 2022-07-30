# High-Pix encoding
```
Pixel height based data encoding, not the preferred/efficient way of encoding data but yet another experiment with pixels.
```

## Requirements
`PIL` - for reading pixels and info ( `pip install PIL` )

## Writer
**Usage**
```bash
python3 writer.py <out image> <string / text file>
```
![](writer.png)
*( The high-pix encoded version of the inital `writer.py` )*

## Reader
**Usage**
```bash
python3 reader.py <in image> -q # -q for text only output
```
![](reader.png)
*( The high-pix encoded version of the inital `reader.py` )*

## Logic behind this
### Working logic
I was thinking of a way to store data in pixels. Then I suddenly thought about the height of the image and what if we could just represent the data in pixel height of each column ( y height). More like a tiny version of graph. `X` represents each character and `Y` represents the value of the current X pixel. The images have a margin of 1 px and the **"non-black"** pixels get ignored.<br>
**NOTE : This uses base64(utf-8) to represent values from 0-63**

### How the script works
* At start, it jumps to the `y` pixel before the final pixel ( y = height - 1) and the pixel after the initial pixel ( x = 1 ).
* Checks if the pixel is black ( which means it represents 1 ), moves one pixel up in the `y` pixel row by one ( y = y - 1) and increments the counter by 1 ( n = n + 1 )
* This loop (while) continues while the pixel is black in color
* If the current pixel is not black; it stops the loop, appends the counter value ( e.g 5 ) to the character list array and moves to the next pixel in `x` column and starts the same process as mentioned above.
* This process continues till it reaches the end of the image width ( x_max = width - 1 )
* Data is written or read using the character list array ( e.g [ 22, 56, 54...] ) and then converted to it's base64 value by the array present which acts as a map.

## The use?
Well, this specific project serves no purpose other than being an experiment nor meant to be considered serious. I was learning how pixels works and thought of this idea to experiment with the dimensional iteration with an interesting concept to implement.
