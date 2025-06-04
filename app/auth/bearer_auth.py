from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import config


class FixedTokenBearer(HTTPBearer):
    def __init__(self, token: str, auto_error: bool = True):
        """
        Args:
            token (str): Expected bearer token.
            auto_error (bool): Whether to raise error automatically.
        """
        super().__init__(auto_error=auto_error)
        self.token = token

    async def __call__(self, request: Request):
        """
        Args:
            request (Request): Incoming HTTP request.

        Returns:
            HTTPAuthorizationCredentials: Validated credentials.

        Raises:
            HTTPException: If token is invalid or missing.
        """
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if credentials.scheme.lower() != "bearer":
                raise HTTPException(
                    status_code=403, detail="Esquema inválido. Use Bearer"
                )
            if credentials.credentials != self.token:
                raise HTTPException(status_code=403, detail="Token inválido")
        else:
            raise HTTPException(status_code=403, detail="Token ausente")
        return credentials


auth_bearer = FixedTokenBearer(token=config.BEARER_TOKEN)
