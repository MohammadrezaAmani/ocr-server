
# OCR Server

A lightweight and async OCR server powered by **FastAPI**, **Celery**, **EasyOCR**, and **Redis**. Supports image and PDF OCR using CPU.

---

## Features

- OCR for images (`.jpg`, `.png`, etc.) and PDFs
- Async task processing with **Celery**
- Accurate OCR using **EasyOCR**
- Task-based API (submit → get result)
- Modular codebase (production-ready)

---

## 📁 Project Structure

```bash
ocr-server/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── src/
│   ├── __main__.py       # FastAPI app entrypoint
│   ├── worker.py         # Celery worker app
│   ├── tasks.py          # Celery OCR task
│   ├── ocr_engine.py     # EasyOCR logic
│   ├── utils.py          # PDF/Image tools
│   └── config.py         # Paths & settings
```

---

## ⚙️ Requirements

- Docker & Docker Compose

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 📡 API Endpoints

**Submit OCR task**

```http
POST /ocr
Form-Data: file=@yourfile.pdf
```

**Get result**

```http
GET /result/{task_id}
```

---

## ✅ Example Response

```json
{
  "status": "completed",
  "result": {
    "type": "pdf",
    "pages": [
      {
        "page": 1,
        "text": [
          {
            "text": "Hello World",
            "confidence": 0.98,
            "box": [[x1, y1], [x2, y2], ...]
          }
        ]
      }
    ]
  }
}
```

---

## 🧪 Test with `curl`

```bash
curl -F "file=@sample.pdf" http://localhost:8000/ocr
curl http://localhost:8000/result/<task_id>
```
