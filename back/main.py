from fastapi import FastAPI, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.settings import get_session

app = FastAPI(debug=True)

origins = ["http://localhost", "http://localhost:8080", "http://localhost:3000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start():
    print("Поехали")


@app.get("/")
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.unique().scalars().all()
    return users


# bot.include_router(src.users_router, prefix="/api/users", tags=["Users"])
#
# bot.include_router(src.chats_router, prefix="/api/chats", tags=["Chats"])
#
# bot.include_router(src.messages_router, prefix="/api/messages", tags=["Messages"])
#
# bot.include_router(src.bootcamps_router, prefix="/api/bootcamps", tags=["Bootcamps"])
#
# bot.include_router(src.websocket_router, prefix="/api/ws", tags=["WS_Messages"])