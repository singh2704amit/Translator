import translator_logic
import config

def start_app():
    print(f"--- Welcome to {config.APP_NAME} v{config.VERSION} ---")
    
    text = input("Enter text to translate: ")
    print("\nCommon codes: 'es' (Spanish), 'fr' (French), 'de' (German), 'hi' (Hindi)")
    target = input(f"Enter target language code (default '{config.DEFAULT_TARGET_LANGUAGE}'): ")
    
    # Use default if user presses Enter
    if not target:
        target = config.DEFAULT_TARGET_LANGUAGE

    result = translator_logic.translate_text(text, target)
    
    print("-" * 30)
    print(f"Result: {result}")
    print("-" * 30)

if __name__ == "__main__":
    start_app()

