import asyncio
from gemini_webapi import GeminiClient
from gemini_webapi.constants import Model
import os
Secure_1PSID = os.getenv("GOOG_SID")
Secure_1PSIDTS = os.getenv("GOOG_TS") 
class GeminiAI:
    def __init__(self,model):
        self.client = GeminiClient(
            model=model,
            secure_1PSID=Secure_1PSID,
            secure_1PSIDTS=Secure_1PSIDTS,
        )
        asyncio.run(self.init())
    async def init(self):
        await self.client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
    async def generate(self, prompt)-> str:
        response = await self.client.generate_content(prompt)
        return response.text
