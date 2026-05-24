from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from models.db import DB_Controller
import config
import asyncio


db = DB_Controller()


chat_id = config.CHANNEL
msg_id = config.PUBLIC_MSG

async def public_msgs(client: Client, message: Message):
    customers = await db.get_customers()
    for user_id in customers:
        try:
            await client.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=msg_id)
            await asyncio.sleep(0.2)  # Sleep to avoid hitting rate limits
        except FloodWait as e:
            print(f"Flood wait of {e.x} seconds. Sleeping...")
            await asyncio.sleep(e.x)
        except Exception as e:
            print(f"Error sending message to {user_id}: {e}")