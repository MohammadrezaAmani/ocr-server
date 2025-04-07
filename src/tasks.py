from .config import UPLOAD_DIR
from .ocr_engine import run_ocr


def ocr_task_handler(file_name: str):
    file_path = UPLOAD_DIR / file_name
    return run_ocr(str(file_path))
