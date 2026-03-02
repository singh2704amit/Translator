from deep_translator import GoogleTranslator

def translate_text(text, target_language='en'):
    """
    Translates text to the target language.
    'auto' detects the source language automatically.
    """
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

def get_languages():
    """Returns a dictionary of supported languages and their codes."""
    return GoogleTranslator().get_supported_languages(as_dict=True)

