from fastapi import FastAPI

from toy_fast_api.odd_or_even import odd_or_even_test

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/")
async def odd_or_even(n: int):
    return {n: odd_or_even_test(n)}
