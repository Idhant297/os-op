from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    agent = Agent(
        task="open chatgpt app",
        llm=ChatOpenAI(model="gpt-4-turbo"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())