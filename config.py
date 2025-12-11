import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "your_default_api_key")
SOCKS_PROXY = os.getenv("SOCKS_PROXY", "")
