import os
import yt_dlp
from pydub import AudioSegment
import shutil

class MashupError(Exception):
    pass

def create_mashup(singer, n, duration, output_file):

    temp_dir = "temp_downloads"
    os.makedirs(temp_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{temp_dir}/%(title)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{n}:{singer} songs"])
    except Exception as e:
        raise MashupError(f"Download failed: {e}")

    final_audio = AudioSegment.empty()

    for file in os.listdir(temp_dir):
        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(os.path.join(temp_dir, file))
            trimmed = audio[:duration * 1000]
            final_audio += trimmed

    final_audio.export(output_file, format="mp3")

    shutil.rmtree(temp_dir)
