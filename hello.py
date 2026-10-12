from dotenv import load_dotenv
load_dotenv()

from pydantic_ai import Agent

agent = Agent("google:gemini-3.8-flash")
result = agent.run_sync("Say hello in one sentence.")
print(result.output)