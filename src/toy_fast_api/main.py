from fastapi import FastAPI

from toy_fast_api.odd_or_even import odd_or_even_test

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/odd_or_even/{n}")
async def odd_or_even(n: int):
    return {"n": n, "odd_or_even": odd_or_even_test(n)}
