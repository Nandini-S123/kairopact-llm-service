from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str| None = None
    GROQ_API_KEY: str | None = None 
    MODEL_NAME: str = "gpt-4o-mini"
    TIMEOUT: int = 30

settings = Settings()


print("API KEY FOUND:", bool(settings.OPENAI_API_KEY))