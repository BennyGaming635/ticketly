from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Base, engine
from app.routes import auth_router, base_router


def create_tables():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)


# Initialize FastAPI app
app = FastAPI(
    title="Ticketly API",
    description="Self-hosted ticket management platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Initialize database on startup."""
    create_tables()


# Include routers
app.include_router(base_router)
app.include_router(auth_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
