from fastapi import FastAPI
from src.booking.routers import booking_router
from src.users.routers import user_router

app = FastAPI()

app.include_router(booking_router)
app.include_router(user_router)
