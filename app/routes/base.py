from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    """Root endpoint."""
    return {
        "message": "Welcome to Ticketly API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
