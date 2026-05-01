import datetime
import asyncio
import os
import sys
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# --- Конфигурация ---
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env"), override=True)

GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")

# --- Инструменты (Tools) ---
def now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

airbnb_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
        ),
        timeout=30 
    )
)

nanobanana_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='uvx',
            args=["nanobanana-mcp-server@latest"],
            env={
                **({"GEMINI_API_KEY": GEMINI_API_KEY} if GEMINI_API_KEY else {}),
                "IMAGE_OUTPUT_DIR": "./output_images" 
            }
        ),
        timeout=60 
    )
)

# --- Агент с логикой Exponential Backoff ---
root_agent = Agent(
    name="travel_mcp",
    model="gemini-2.5-flash",
    instruction="""You are an expert travel assistant.

    RELIABILITY PROTOCOL (Exponential Backoff):
    1. If any tool call returns a '429' or '503' error, DO NOT STOP.
    2. Wait sequence: 1st fail: 5s, 2nd fail: 15s, 3rd fail: 30s.
    3. State "Quota exceeded, retrying in X seconds..." before each wait.
    
    CORE TASKS:
    1. Use airbnb_mcp to find and detail accommodations.
    2. After selection, call nanobanana_mcp to generate a vintage postcard of the facade.
    3. Use the address from Airbnb for the image prompt.
    """,
    tools=[now, airbnb_mcp, nanobanana_mcp],
)

async def main():
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", "gemini-travel-agency")
    os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "us-central1")
    if not os.path.exists("./output_images"):
        os.makedirs("./output_images")

    try:
        process = await asyncio.create_subprocess_exec(
            "uv", "run", "adk", "run", script_dir,
            stdout=sys.stdout, stderr=sys.stderr
        )
        await process.wait()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())