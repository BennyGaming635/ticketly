from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.sql import func
from app.config.database import Base


class Event(Base):
    """Event model for ticket selling."""
    
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text)
    location = Column(String)
    start_datetime = Column(DateTime(timezone=True), nullable=False)
    end_datetime = Column(DateTime(timezone=True))
    max_tickets = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
