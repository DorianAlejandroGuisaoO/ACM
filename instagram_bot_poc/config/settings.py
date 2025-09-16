import os

class Config:
    INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', 'default_user')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD', 'default_pass')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'default_key')
    LOG_LEVEL = 'INFO'
    MAX_RESPONSES_PER_HOUR = 10