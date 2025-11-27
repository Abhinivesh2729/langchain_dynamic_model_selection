import os
import sys
from pathlib import Path

#add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.env_helper import load_env_vars

load_env_vars()
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)


