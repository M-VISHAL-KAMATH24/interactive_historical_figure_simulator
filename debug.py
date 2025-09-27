import os, sys, inspect, logging
logging.basicConfig(level=logging.INFO)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent import root_agent

print("root_agent type:", type(root_agent))
print("root_agent methods:", [m for m in dir(root_agent) if not m.startswith("_")])

if hasattr(root_agent, "run_async"):
    print("run_async signature:", inspect.signature(root_agent.run_async))

# Intercept a single test run to capture event types without UI
async def smoke():
    agen = root_agent.run_async("The user wants to speak to Albert Einstein. The user's message is: 'hi'")
    async for ev in agen:
        print("EVENT:", ev.type, ev.data.keys())

if __name__ == "__main__":
    import asyncio
    asyncio.run(smoke())
