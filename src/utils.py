import io
from typing import List

import fitz  # PyMuPDF
import numpy as np
from PIL import Image


def is_image_file(filename: str) -> bool:
    return any(
        filename.lower().endswith(ext)
        for ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]
    )


async def extract_images_from_pdf(pdf_path: str) -> List[np.ndarray]:
    doc = fitz.open(pdf_path)
    images = []

    for page in doc:
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data)).convert("RGB")
        images.append(np.array(img))

    return images
