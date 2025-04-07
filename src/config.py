from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
CELERY_BROKER_URL = "redis://redis:6379/0"
