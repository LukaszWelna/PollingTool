from fastapi import APIRouter
from database import connection_string

user = APIRouter()

@user.get("/")
async def find_all_users():
    return connection_string
