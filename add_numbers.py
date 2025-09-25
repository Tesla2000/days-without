import os
from pathlib import Path
from typing import Optional, NamedTuple

from PIL import Image, ImageDraw, ImageFont


def add_numbers_to_image(
        image_path: str,
        number1: int,
        number2: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        font_size: int,
        font_path: Optional[str] = None,
        rotation: int = 0,
        output_path: str = "output.png",
        bold_offset: int = 0,
):
    number1 = str(number1)
    number2 = str(number2)
    img = Image.open(image_path).convert("RGBA")

    if font_path and os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default(font_size)

    def draw_rotated_text(base_img, text, position, angle):
        # Create a transparent image to draw the text on
        text_img = Image.new("RGBA", base_img.size, (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_img)

        for dx in range(-bold_offset, bold_offset + 1):
            for dy in range(-bold_offset, bold_offset + 1):
                text_draw.text(
                    (position[0] + dx, position[1] + dy),
                    text,
                    font=font,
                    fill=(0, 0, 0, 255),
                )

        rotated = text_img.rotate(angle, resample=Image.BICUBIC, center=position)

        return Image.alpha_composite(base_img, rotated)

    img = draw_rotated_text(img, number1, (x1, y1), rotation)
    img = draw_rotated_text(img, number2, (x2, y2), rotation)

    img.convert("RGB").save(output_path)
    print(f"Image saved to {output_path}")


class Coordinates(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


if __name__ == "__main__":
    outputs_path = Path("outputs")
    outputs_path.mkdir(parents=True, exist_ok=True)

    for first_number in range(10, 99):
        if first_number < 10:
            coordinates = Coordinates(
                69,
                69,
                50,
                225,
            )
            font_size = 100
        else:
            coordinates = Coordinates(
                42,
                69,
                21,
                225,
            )
            font_size = 90
        x1, y1, x2, y2 = coordinates
        add_numbers_to_image(
            "days_without.png",
            first_number,
            first_number + 1,
            x1,
            y1,
            x2,
            y2,
            font_size,
            None,
            10,
            f"{outputs_path}/" + str(first_number) + "_" + str(first_number + 1) + ".png",
            bold_offset=2,
        )
