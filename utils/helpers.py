def clean_text(text):

    return text.strip()


def detect_language_name(code):

    languages={

    "ta":"Tamil",
    "te":"Telugu",
    "hi":"Hindi",
    "en":"English",
    "kn":"Kannada"

    }


    return languages.get(
        code,
        "English"
    )