from celery import Celery

from .config import CELERY_BROKER_URL
from .tasks import ocr_task_handler

celery = Celery("worker", broker=CELERY_BROKER_URL)


@celery.task(name="app.ocr")
def process_ocr_task(file_name: str):
    return ocr_task_handler(file_name)
