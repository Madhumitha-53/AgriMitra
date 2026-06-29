import os
import uuid
from gtts import gTTS



VOICE_MAP = {

    "ta": "ta",
    "te": "te",
    "hi": "hi",
    "en": "en",
    "kn": "kn",
    "ml": "ml",
    "mr": "mr"

}



def create_voice(text, language):

    lang = VOICE_MAP.get(language, "en")

    file = "voice_" + str(uuid.uuid4()) + ".mp3"

    speech = gTTS(text=text, lang=lang)

    speech.save(file)

    return file



def cleanup_voice_file(file):
    """Remove a temporary voice file after it has been served."""
    try:
        if file and os.path.exists(file):
            os.remove(file)
    except OSError:
        pass
