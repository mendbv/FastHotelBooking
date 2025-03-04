import datetime

from pydantic import BaseModel

class BookingCreate(BaseModel):
    """
    Booking create schema
    """
    user_id: str
    room_id: str
    start_date: datetime.datetime
    end_date: str
    room_type: str

class BookingUpdate(BaseModel):
    """
    Booking update schema
    """
    start_date: datetime.datetime
    end_date: str

class BookingResponse(BaseModel):
    """
    Booking response schema
    """
    user_id: str
    room_id: str
    start_date: datetime.datetime
    end_date: str
    room_type: str

class RoomResponse(BaseModel):
    """
    Room response schema
    """
    room_type: str
    room_number: str

class RoomCreate(BaseModel):
    """
    Room create schema
    """
    room_type: str
    room_number: str