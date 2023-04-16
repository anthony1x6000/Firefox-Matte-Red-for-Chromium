from PIL import Image
import sys

def change_color(image_path, color):
    with Image.open(image_path) as im:
        im = im.convert('RGB')
        pixels = im.load()
        width, height = im.size
        for x in range(width):
            pixels[x, 0] = color
            pixels[x, 1] = color
        im.save(image_path)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python color.py [image_path] [color]")
        sys.exit(1)
    image_path = sys.argv[1]
    color = hex_to_rgb(sys.argv[2])
    change_color(image_path, color)