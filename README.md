# 🎵 Mashup Generator

A Python-based Mashup Generator to create audio mashups from Youtube videos of a specific singer. Include:

- **Program 1:** Command Line Interface (CLI)
- **Program 2:** Web Service (Flask-based UI + Email Delivery)

---

## 📂 Project Structure

- `102313038.py` : CLI Entry Point.

- `mashup_core.py` : Core mashup logic (download, trim, merge).

- `webapp/app.py` : Web Service Backend (Flask).

- `webapp/templates/` : HTML templates for the Web App.

- `webapp/static/` : CSS styling and static assets.

---

## ⚙ Prerequisites

Install:

- Python 3.x
- FFmpeg (added to system PATH)
- Dependencies: `yt-dlp`, `pydub`, `flask`, `gunicorn`

Install dependencies:

```bash
pip install -r requirements.txt


