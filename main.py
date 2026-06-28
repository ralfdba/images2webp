from pathlib import Path
from PIL import Image

input_folder = Path("images")
output_folder = Path("webp")

extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".gif"}

for image_path in input_folder.rglob("*"):
    if image_path.suffix.lower() in extensions:
        relative = image_path.relative_to(input_folder)
        out = output_folder / relative.with_suffix(".webp")
        out.parent.mkdir(parents=True, exist_ok=True)

        try:
            with Image.open(image_path) as img:
                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGB")

                img.save(out, "WEBP", quality=85, method=6)

            print(f"Converted: {relative}")

        except Exception as e:
            print(f"Error: {relative} -> {e}")