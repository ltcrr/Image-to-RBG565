from PIL import Image
import struct

def convert_to_rgb565(input_path, output_path, width=256, height=192):
    img = Image.open(input_path).convert('RGB')
    img = img.resize((width, height))

    with open(output_path, 'wb') as f:
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                r5 = (r >> 3) & 0x1F
                g6 = (g >> 2) & 0x3F
                b5 = (b >> 3) & 0x1F
                rgb565 = (r5 << 11) | (g6 << 5) | b5
                
                f.write(struct.pack('<H', rgb565))

    print(f"Output folder : {output_path}")

pathimage = input("Enter image path : ")
convert_to_rgb565(f"{pathimage}", "output.bin")
