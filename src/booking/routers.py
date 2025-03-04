"""
Router for booking app
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import Booking, Room
from .schemas import BookingCreate, BookingUpdate, BookingResponse, RoomCreate, RoomResponse
from src.database import get_db

booking_router = APIRouter()

@booking_router.post("/bookings", response_model=BookingResponse)
async def create_booking(booking: BookingCreate, db: AsyncSession = Depends(get_db)):
    """
    Create booking
    """
    async with db as session:
        new_booking = Booking(**booking.dict())
        session.add(new_booking)
        await session.commit()
        await session.refresh(new_booking)
        return new_booking

@booking_router.get("/bookings", response_model=Sequence[BookingResponse])
async def get_bookings(db: AsyncSession = Depends(get_db)):
    """
    Get all bookings
    """
    async with db as session:
        result = await session.execute(select(Booking))
        return result.scalars().all()

@booking_router.get("/bookings/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get booking by id
    """
    async with db as session:
        result = await session.execute(select(Booking).where(Booking.id == booking_id))
        booking = result.scalar()
        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        return booking

@booking_router.put("/bookings/{booking_id}", response_model=BookingResponse)
async def update_booking(booking_id: int, booking: BookingUpdate, db: AsyncSession = Depends(get_db)):
    """
    Update booking
    """
    async with db as session:
        result = await session.execute(
            select(Booking).where(Booking.id == booking_id)
        )
        existing_booking = result.scalar()
        if not existing_booking:
            raise HTTPException(status_code=404, detail="Booking not found")

        # обновляем только существующее бронирование
        await session.execute(
            Booking.__table__.update()
            .where(Booking.id == booking_id)
            .values(**booking.dict())
        )
        await session.commit()
        return existing_booking

@booking_router.delete("/bookings/{booking_id}")
async def delete_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete booking
    """
    async with db as session:
        result = await session.execute(
            Booking.__table__.delete().where(Booking.id == booking_id).returning(Booking)
        )
        deleted_booking = result.scalar()
        if not deleted_booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        await session.commit()
        return deleted_booking

@booking_router.get("/rooms", response_model=Sequence[RoomResponse])
async def get_rooms(db: AsyncSession = Depends(get_db)):
    """
    Get all rooms
    """
    async with db as session:
        result = await session.execute(select(Room))
        return result.scalars().all()

@booking_router.get("/rooms/{room_id}", response_model=RoomResponse)
async def get_room(room_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get room by id
    """
    async with db as session:
        result = await session.execute(select(Room).where(Room.id == room_id))
        room = result.scalar()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        return room

@booking_router.post("/rooms", response_model=RoomResponse)
async def create_room(room: RoomCreate, db: AsyncSession = Depends(get_db)):
    """
    Create room
    """
    async with db as session:
        new_room = Room(**room.dict())
        session.add(new_room)
        await session.commit()
        await session.refresh(new_room)
        return new_room

@booking_router.put("/rooms/{room_id}", response_model=RoomResponse)
async def update_room(room_id: int, room: RoomResponse, db: AsyncSession = Depends(get_db)):
    """
    Update room
    """
    async with db as session:
        result = await session.execute(
            select(Room).where(Room.id == room_id)
        )
        existing_room = result.scalar()
        if not existing_room:
            raise HTTPException(status_code=404, detail="Room not found")

        # обновляем только существующую комнату
        await session.execute(
            Room.__table__.update()
            .where(Room.id == room_id)
            .values(**room.dict())
        )
        await session.commit()
        return existing_room

@booking_router.delete("/rooms/{room_id}")
async def delete_room(room_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete room
    """
    async with db as session:
        result = await session.execute(
            Room.__table__.delete().where(Room.room_id == room_id).returning(Room)
        )

        deleted_room = result.scalar()
        if not deleted_room:
            raise HTTPException(status_code=404, detail="Room not found")
        await session.commit()
        return deleted_room
