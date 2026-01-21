from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class TicketType(Base):
    """Ticket type model (e.g., General Admission, VIP, etc.)."""
    
    __tablename__ = "ticket_types"
    
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    quantity_available = Column(Integer, nullable=False)
    quantity_sold = Column(Integer, default=0)
