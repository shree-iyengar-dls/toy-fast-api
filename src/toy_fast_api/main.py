import logging

import uvicorn
from fastapi import FastAPI

from toy_fast_api.odd_or_even import odd_or_even_test

app = FastAPI()
ALGORITHM = "HS256"

# oauth2_scheme = OAuth2AuthorizationCodeBearer(
#    authorizationUrl= config
# )


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


# def decode_access_token(config: CustomOIDC):
#     jwkclient = jwt.PyJWKClient(config.jwks_uri)
#     oauth_scheme = OAuth2AuthorizationCodeBearer(
#         authorizationUrl=config.authorization_endpoint,
#         tokenUrl=config.token_endpoint,
#         refreshUrl=config.token_endpoint,
#     )

#     def inner(request: Request, access_token: str = Depends(oauth_scheme)):
#         signing_key = jwkclient.get_signing_key_from_jwt(access_token)
#         decoded: dict[str, Any] = jwt.decode(
#             access_token,
#             signing_key.key,
#             algorithms=config.id_token_signing_alg_values_supported,
#             verify=True,
#             audience=config.client_audience,
#             issuer=config.issuer,
#         )
#         request.state.decoded_access_token = decoded

#     return inner
