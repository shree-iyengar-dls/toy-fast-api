from pydantic import BaseModel


class CustomOIDC(BaseModel):  # maybe don't need this anymore
    issuer_url: str = "https://identity-test.diamond.ac.uk/realms/dls"
    client_id: str = "ToyFastAPI"
    authorization_endpoint: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/auth"
    )
    token_endpoint: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/token"
    )
    jwks_uri: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/certs"
    )
