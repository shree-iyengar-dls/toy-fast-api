from functools import cached_property
from typing import Any, cast

import requests
from pydantic import BaseModel, Field


class CustomOIDC(BaseModel):
    well_known_url: str = Field(
        description="URL to fetch OIDC config from the provider"
    )
    client_id: str = Field(description="Client ID")
    client_audience: str = Field(
        description="Client Audience(s)", default="toy-fast-api"
    )
    logout_redirect_endpoint: str = Field(
        description="The oidc endpoint required to logout", default=""
    )

    @cached_property
    def _config_from_oidc_url(self) -> dict[str, Any]:
        response: requests.Response = requests.get(self.well_known_url)
        response.raise_for_status()
        return response.json()

    @cached_property
    def device_authorization_endpoint(self) -> str:
        return cast(
            str, self._config_from_oidc_url.get("device_authorization_endpoint")
        )

    @cached_property
    def token_endpoint(self) -> str:
        return cast(str, self._config_from_oidc_url.get("token_endpoint"))

    @cached_property
    def issuer(self) -> str:
        return cast(str, self._config_from_oidc_url.get("issuer"))

    @cached_property
    def authorization_endpoint(self) -> str:
        return cast(str, self._config_from_oidc_url.get("authorization_endpoint"))

    @cached_property
    def jwks_uri(self) -> str:
        return cast(str, self._config_from_oidc_url.get("jwks_uri"))

    @cached_property
    def end_session_endpoint(self) -> str:
        return cast(str, self._config_from_oidc_url.get("end_session_endpoint"))

    @cached_property
    def id_token_signing_alg_values_supported(self) -> list[str]:
        return cast(
            list[str],
            self._config_from_oidc_url.get("id_token_signing_alg_values_supported"),
        )

    def keys(self):
        a = cast(str, self._config_from_oidc_url.get("jwks_uri"))
        b = requests.get(a)
        b.raise_for_status()
        return b.json().get("keys", [])


class ApplicationConfig(BaseModel):
    oidc: CustomOIDC
