import os
from dotenv import load_dotenv

def load_env_vars(env_path=".env"):
    load_dotenv(env_path, override=True)
    # Optionally, print loaded variables
    for key, value in os.environ.items():
        if key.startswith("GEMINI_"):
            print(f"{key}={value}")

# Usage
load_env_vars()