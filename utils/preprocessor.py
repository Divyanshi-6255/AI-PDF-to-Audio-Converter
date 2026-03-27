import nltk
nltk.download('punkt', quiet=True)

def clean_text(text: str) -> str:
    """Clean the extracted text"""
    if not text:
        return ""
    
    # Remove extra spaces and newlines
    text = " ".join(text.split())
    
    return text