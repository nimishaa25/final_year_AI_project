# avatar/tts_engine.py
#pip install edge-tts
#pip install pydub
#Download from:
#https://ffmpeg.org/download.html
#Add to PATH.


import asyncio
import edge_tts
from pydub import AudioSegment

VOICE = "en-US-AriaNeural"  # You can change voice

async def _generate_mp3(text: str, mp3_path: str):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(mp3_path)

def generate_audio(text: str, output_path="avatar_audio.wav"):
    """
    Converts text to speech using Edge TTS
    Saves final output as WAV for SadTalker
    """

    mp3_path = "temp_audio.mp3"

    # Run async TTS
    asyncio.run(_generate_mp3(text, mp3_path))

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(output_path, format="wav")

    return output_path
