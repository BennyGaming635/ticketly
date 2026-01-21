from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from app.config.database import Base


class Ticket(Base):
    """Ticket model representing individual tickets."""
    
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    ticket_type_id = Column(Integer, ForeignKey("ticket_types.id"), nullable=False)
    ticket_code = Column(String, unique=True, nullable=False, index=True)
    is_checked_in = Column(Boolean, default=False)
    checked_in_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
