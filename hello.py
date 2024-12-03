import asyncio

async def main():
    for i in range(4):
        await asyncio.sleep(3)
        print("Hello")

asyncio.run(main())
# def greetings(to):
#     print(f'hello, {{to}}')
#
# name = input("What's your name? ")
#
# greetings(name)