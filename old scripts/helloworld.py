import asyncio
import sys
import winsound
async def helloworld():
    string = 'hello world'
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        winsound.Beep(30000, 1)
        await asyncio.sleep(0.1)
    await asyncio.sleep(5)

asyncio.run(helloworld())
