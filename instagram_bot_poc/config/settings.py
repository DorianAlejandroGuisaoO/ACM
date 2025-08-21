import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    LOG_LEVEL = 'INFO'
    MAX_RESPONSES_PER_HOUR = 10  # Criterio de sostenibilidad