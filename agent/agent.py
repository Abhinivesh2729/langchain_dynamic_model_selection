import os
import sys
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, ModelResponse, wrap_model_call

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

@tool
def get_user_location(userId: str) -> str:
    """Get the location of the user from the userId"""
    return f"The user {userId} is in Erode city"


@tool
def get_weather(city: str) -> str:
    """Get weather for the given city"""
    return f"The {city} is very likly to have thunder stroam today, now it seems pre rain"

#dynamic model selection
@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:

    if( len(request.state["messages"]) > 2 ):
        print("Using Advance Model")
        model = advance_model
    else:
        print("Using Basic Model")
        model = basic_model
    
    return handler(request.override(model=model))

#agent

agent = create_agent(
    model = basic_model,
    tools = [get_user_location, get_weather],
    middleware = [dynamic_model_selection],
    system_prompt = "You have been provided with two tools, use them wisely to answer the user query, use the get_user_location tool to get the user location and get the user id from the user input and use get_weather function to get the weather data"
)

response = agent.invoke(
   {
       "messages": [
           {"role": "user",
            "content": "What is the weather in my location, my user id is 1"
            },
       ]
   }
)

print(response["messages"][-1].content)