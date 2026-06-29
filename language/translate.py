from deep_translator import GoogleTranslator



def translate_text(
    text,
    target
):

    result = GoogleTranslator(
        source="auto",
        target=target
    ).translate(text)


    return result