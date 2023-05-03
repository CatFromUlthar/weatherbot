from deep_translator import GoogleTranslator


def translate(text: str) -> str:
    to_en = GoogleTranslator(source='auto', target='en')
    translated_text = to_en.translate(text)
    return translated_text
