print("blucles")

import asyncio

class AsyncIterador:
    def __init__(self, limite):
        self.limite = limite
    
    def __aiter__(self):
        self.i = 0
        return self
    
    async def __anext__(self):
        if self.i >= self.limite:
            raise StopAsyncIteration
        await asyncio.sleep(0.5)  # Simula operación asíncrona
        self.i += 1
        return self.i

async def main():
    async for numero in AsyncIterador(3):
        print(numero)  # Output (con delay): 1, 2, 3

asyncio.run(main())