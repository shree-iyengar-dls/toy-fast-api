from pydantic import BaseModel


class CustomOIDC(BaseModel):
    issuer_url: str = "https://identity-test.diamond.ac.uk/realms/dls"
    client_id: str = "ToyFastAPI"
    authorization_endpoint: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/auth"
    )
    token_endpoint: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/token"
    )
    client_secret: str = "yJK1jlm3gnB83Thk2u3drryGzL893ctP"
    jwks_uri: str = (
        "https://identity-test.diamond.ac.uk/realms/dls/protocol/openid-connect/certs"
    )
