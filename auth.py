from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class Auth:

    security = HTTPBearer()
    def __init__(self, token: str):
        self.token = token

    def verify_token(self, credentials: HTTPAuthorizationCredentials = Depends(security)):
        if credentials.credentials != self.token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return credentials.credentials