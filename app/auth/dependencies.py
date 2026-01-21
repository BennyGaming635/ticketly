from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
from app.config.database import get_db
from app.models.user import User
from app.auth.utils import verify_token

# Security scheme for bearer token
security = HTTPBearer()


def get_token_from_cookie(request: Request) -> Optional[str]:
    """Extract JWT token from cookie."""
    return request.cookies.get("access_token")


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
) -> User:
    """Get the current authenticated user from JWT token."""
    
    # Try to get token from cookie first
    token = get_token_from_cookie(request)
    
    # If not in cookie, try Authorization header
    if not token:
        credentials: HTTPAuthorizationCredentials = Depends(security)
        if credentials:
            token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify token
    email = verify_token(token)
    
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Get user from database
    user = db.query(User).filter(User.email == email).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Get the current active user."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
