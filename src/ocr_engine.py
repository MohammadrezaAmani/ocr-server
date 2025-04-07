import io

import easyocr
import fitz
import numpy as np
from PIL import Image

reader = easyocr.Reader(["en"], gpu=True)


def is_image_file(filename: str) -> bool:
    return any(
        filename.lower().endswith(ext)
        for ext in [".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff"]
    )


def serialize(result):
    return [
        {
            "text": block[1],
            "confidence": float(block[2]),
            "box": block[0],
        }
        for block in result
    ]


def extract_images_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
        images.append(np.array(img))
    return images


def find_text_in_image(image):
    result = reader.readtext(image, detail=1, workers=4)
    print(result)
    return serialize(result)


def run_ocr(file_path: str):
    if is_image_file(file_path):
        result = reader.readtext(file_path, detail=1, workers=4)
        return {"type": "image", "pages": [{"page": 1, "text": serialize(result)}]}

    if file_path.lower().endswith(".pdf"):
        images = extract_images_from_pdf(file_path)
        results = [find_text_in_image(img) for img in images]
        return {
            "type": "pdf",
            "pages": [
                {"page": i + 1, "text": serialize(r)} for i, r in enumerate(results)
            ],
        }

    raise ValueError("Unsupported file format")
