from typing import Optional

from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def add_numbers_to_image(image_path: str, number1: int, number2: int, font_size: int = 100,
                        font_path: Optional[str] = None, rotation: int = 0,
                        output_path: str = "output.png",
                        x1: int = None, y1: int = None,
                        x2: int = None, y2: int = None):
    """
    Add two numbers to an image using Pillow.
    
    Args:
        image_path: Path to the input image
        number1: First number to add
        number2: Second number to add
        font_size: Size of the numbers
        font_path: Path to custom font file (optional)
        rotation: Rotation angle in degrees
        output_path: Path to save the output image
        x1, y1: Coordinates for number1 (if None, will be centered)
        x2, y2: Coordinates for number2 (if None, will be centered)
    """
    number1 = str(number1)
    number2 = str(number2)
    try:
        # Open the image
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        # Load font
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default(font_size)
            
        # Calculate positions if not specified
        width, height = img.size
        number1_width = draw.textlength(number1, font=font)
        number2_width = draw.textlength(number2, font=font)
        
        # Use specified coordinates or default to center
        if x1 is None:
            x1 = (width - number1_width) // 2
        if y1 is None:
            y1 = height // 4
        if x2 is None:
            x2 = (width - number2_width) // 2
        if y2 is None:
            y2 = height * 3 // 4
        
        # Draw rotated numbers
        draw.text((x1, y1), number1, font=font, fill=(0, 0, 0))
        draw.text((x2, y2), number2, font=font, fill=(0, 0, 0))
        
        # Rotate if needed
        if rotation != 0:
            img = img.rotate(rotation, expand=True)
        
        # Save the result
        img.save(output_path)
        print(f"Image saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add numbers to an image')
    parser.add_argument('--image', default='days_without.png', help='Input image path')
    parser.add_argument('--font-size', type=int, default=100, help='Font size')
    parser.add_argument('--font', help='Path to font file')
    parser.add_argument('--rotation', type=int, default=0, help='Rotation angle in degrees')
    parser.add_argument('--output', default='output.png', help='Output image path')
    parser.add_argument('--x1', type=int, help='X coordinate for number1')
    parser.add_argument('--y1', type=int, help='Y coordinate for number1')
    parser.add_argument('--x2', type=int, help='X coordinate for number2')
    parser.add_argument('--y2', type=int, help='Y coordinate for number2')

    for first_number in range(7, 10):
        add_numbers_to_image(
            'days_without.png',
            first_number,
            first_number + 1,
            100,
            None,
            0,
            "outputs/" + str(first_number) + "_" + str(first_number + 1) + ".png",
            x1=100,
        )
