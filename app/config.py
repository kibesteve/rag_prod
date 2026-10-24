import os
# pyrefly: ignore[missing-import]
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    GROQ_FALLBACK_API_KEY = os.getenv('GROQ_FALLBACK_API_KEY', '')
    GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-3.3-70b-versatile')
    
    QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
    QDRANT_URL = os.getenv('QDRANT_CLUSTER_ENDPOINT')
    QDRANT_COLLECTION = os.getenv('QDRANT_COLLECTION_NAME', 'rag_index')
    
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    OPENAI_SLUG = os.getenv("OPENAI_SLUG", "openai")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")
    OPENAI_MODEL_2 = os.getenv("OPENAI_MODEL_2", "gpt-4o")

    GROQ_SLUG = os.getenv("GROQ_SLUG", "groq")
 
    GROQ_MODEL_2 = os.getenv("GROQ_MODEL_2", "llama-3.1-8b-instant")

settings = Settings()

