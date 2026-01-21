from .models import Tool, ToolParameter

def get_weather(location: str) -> str:
    """Gets the current weather for a given location"""
    return f"The weather is {location} is cold"

GET_WEATHER_TOOL = Tool(
    name="get_weather",
    description="Gets the current weather for a given location.",
    parameters=[
        ToolParameter(name="location", type="string")
    ]
)