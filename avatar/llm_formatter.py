# avatar/llm_formatter.py

def format_for_speech(text: str) -> str:
    """
    Cleans and prepares LLM output for TTS.
    Removes symbols, makes it natural for speaking.
    """

    # Basic cleaning
    text = text.replace("\n", " ")
    text = text.replace("•", "")
    text = text.replace("-", "")

    # Optional: shorten too long sentences
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]

    formatted_text = ". ".join(sentences)

    return formatted_text
