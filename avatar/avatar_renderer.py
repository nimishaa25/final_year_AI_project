# avatar/avatar_renderer.py
# Uses SadTalker installed locally
import os

def render_avatar(audio_path: str, image_path="avatar.jpg"):
    """
    Calls SadTalker inference to generate talking avatar video.
    """

    command = f"""
    python SadTalker/inference.py \
    --driven_audio {audio_path} \
    --source_image {image_path} \
    --result_dir SadTalker/results
    """

    os.system(command)

    return "SadTalker/results"
