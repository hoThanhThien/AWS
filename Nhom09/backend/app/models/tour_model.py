from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Date
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime

class Tour(Base):
    __tablename__ = "tour"
    
    id = Column("TourID", Integer, primary_key=True, index=True)
    title = Column("Title", String(100), nullable=False)
    location = Column("Location", String(100))
    description = Column("Description", Text)
    capacity = Column("Capacity", Integer)
    price = Column("Price", Float)
    start_date = Column("StartDate", Date)
    end_date = Column("EndDate", Date)
    status = Column("Status", String(50), default="Available")
    category_id = Column("CategoryID", Integer)
    
    def __repr__(self):
        return f"<Tour(id={self.id}, title={self.title}, price={self.price})>"
