from PIL import Image
import sys

def change_color(image_path, color):
    with Image.open(image_path) as im:
        pixels = im.load()
        pixels[0, 0] = color
        pixels[1, 0] = color
        im.save(image_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python color.py [image_path] [color]")
        sys.exit(1)
    image_path = sys.argv[1]
    color = tuple(int(sys.argv[2].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    change_color(image_path, color)