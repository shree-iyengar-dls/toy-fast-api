import logging

import uvicorn
from fastapi import FastAPI

from toy_fast_api.odd_or_even import odd_or_even_test

app = FastAPI()


LOGGER = logging.getLogger(__name__)


def start():
    LOGGER.info("Starting the service.")
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/odd_or_even/{n}")
def odd_or_even(n: int):
    LOGGER.info(f"Check if {n} is odd or even.")
    return {"n": n, "odd_or_even": odd_or_even_test(n)}
