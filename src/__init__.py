import uuid

import aiofiles
from fastapi import FastAPI, File, UploadFile

from .config import UPLOAD_DIR
from .worker import celery, process_ocr_task

app = FastAPI()


@app.post("/ocr")
async def upload_file(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / filename

    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    task = process_ocr_task.delay(filename)
    return {"task_id": task.id, "message": "OCR task submitted"}


@app.get("/result/{task_id}")
def get_result(task_id: str):
    print("here")

    print("here2")

    task_result = celery.AsyncResult(task_id)
    print("here3")
    print(task_result.state)
    if task_result.state == "PENDING":
        return {"status": "pending"}

    if task_result.state == "SUCCESS":
        return {"status": "completed", "result": task_result.result}

    return {"status": task_result.state, "error": str(task_result.result)}
