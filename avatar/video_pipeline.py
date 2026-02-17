# avatar/video_pipeline.py
#MASTER PIPELINE file. It connects everything.

from avatar.llm_formatter import format_for_speech
from avatar.tts_engine import generate_audio
from avatar.avatar_renderer import render_avatar

def generate_avatar_video(raw_text: str):
    """
    Complete pipeline:
    LLM text → formatted → audio → avatar video
    """

    # Step 1: Format text
    formatted_text = format_for_speech(raw_text)
    # Step 2: Generate speech
    audio_file = generate_audio(formatted_text, "avatar_audio.wav")
    # Step 3: Render avatar video
    result_path = render_avatar(audio_file)

    return result_path
