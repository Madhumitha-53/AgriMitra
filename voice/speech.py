from faster_whisper import WhisperModel


model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)



LANGUAGE_MAP = {
    "ta":"Tamil",
    "te":"Telugu",
    "hi":"Hindi",
    "en":"English",
    "kn":"Kannada",
    "ml":"Malayalam"
}



def speech_to_text(audio_file):


    segments, info = model.transcribe(

        audio_file,

        beam_size=5,

        vad_filter=True,

        condition_on_previous_text=False

    )


    text=""


    for segment in segments:

        text += segment.text + " "



    return {

        "text":text.strip(),

        "language":info.language,

        "language_name":
        LANGUAGE_MAP.get(
            info.language,
            "English"
        )

    }