# 🎵 Mashup Generator
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

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
```
---

## Usage
### Command Line Interface (CLI)
Run the script : 
```bash
python 102313038.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

- Conditions:
  1. `NumberOfVideos` > 10
  2. `AudioDuration` > 20 seconds

### Web Service
1. To Run Locally Set Gmail App Password (PowerShell):
   
   Ensure to Enable 2-Step Verification in Google Account
   ```bash
   $env:EMAIL_USER="yourgmail@gmail.com"
   $env:EMAIL_PASS="your_16_char_app_password"
   ```
   - For deployment, set `EMAIL_USER` & `EMAIL_PASS` inside Environment Variables.
3. Run
   ```bash
   python -m webapp.app
   ```
4. Open:
   ```bash
   http://127.0.0.1:5000
   ```
### Interface
<img width="743" height="811" alt="image" src="https://github.com/user-attachments/assets/a86dc883-7e53-4114-a99e-de2800f93d23" />

   
## 📦 Deployment Note
CLI and Web app fully works locally.

However, incase of deployment YouTube applies anti-bot restrictions on cloud servers.
Due to this, downloading videos from deployed cloud environments may fail.

This limitation is due to YouTube security policies, not code issues.







