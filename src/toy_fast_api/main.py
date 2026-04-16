import logging
from typing import Any

import jwt
import uvicorn
from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.security import OAuth2AuthorizationCodeBearer

from toy_fast_api.config import ApplicationConfig, CustomOIDC
from toy_fast_api.odd_or_even import odd_or_even_test

secure_router = APIRouter()
app = FastAPI()
LOGGER = logging.getLogger(__name__)


def decode_access_token(config: CustomOIDC):
    jwkclient = jwt.PyJWKClient(config.jwks_uri)
    oauth_scheme = OAuth2AuthorizationCodeBearer(
        authorizationUrl=config.authorization_endpoint,
        tokenUrl=config.token_endpoint,
        refreshUrl=config.token_endpoint,
    )

    def inner(request: Request, access_token: str = Depends(oauth_scheme)):
        signing_key = jwkclient.get_signing_key_from_jwt(access_token)
        decoded: dict[str, Any] = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=config.id_token_signing_alg_values_supported,
            verify=True,
            audience=config.client_audience,
            issuer=config.issuer,
        )
        request.state.decoded_access_token = decoded

    return inner


def get_app(config: ApplicationConfig):
    app = FastAPI(
        title="Toy-FastAPI",
        summary="Toy-FastAPI that checks if a number is odd or even.",
    )
    if config.oidc:
        app.swagger_ui_init_oauth = {
            "clientId": "NOT_SUPPORTED",
        }
    app.include_router(
        secure_router, dependencies=Depends(decode_access_token(config.oidc))
    )
    return app


def start(config: ApplicationConfig):
    LOGGER.info("Starting the service.")
    app = get_app(config)
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@secure_router.get("/odd_or_even/{n}")
def odd_or_even(n: int):
    LOGGER.info(f"Check if {n} is odd or even.")
    return {"n": n, "odd_or_even": odd_or_even_test(n)}
