import os
import sys
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
#add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.env_helper import load_env_vars

load_env_vars()
api_key = os.getenv("GEMINI_API_KEY")
#print(api_key)




#model configs

basic_model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    api_key = api_key
)

advance_model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = api_key
)

#print(advance_model.invoke("Hello, who are you").content)

#tools

