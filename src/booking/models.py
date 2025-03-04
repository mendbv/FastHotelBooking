from datetime import datetime
import uuid
from sqlalchemy import ForeignKey, String, Integer, DateTime, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base


class Booking(Base):
    """
    Booking model
    """
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("room.room_id"), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    room_type: Mapped[str] = mapped_column(String(length=20), nullable=False)

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")


class Room(Base):
    """
    Room model
    """
    __tablename__ = "room"

    room_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  # Приведено к Integer
    room_type: Mapped[str] = mapped_column(String(length=20), nullable=False)
    room_number: Mapped[str] = mapped_column(String(length=10), nullable=False)

    bookings = relationship("Booking", back_populates="room")
