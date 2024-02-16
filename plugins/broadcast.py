from pyrogram import Client, filters
import asyncio

from info import ADMINS
from utils import broadcast_messages

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)  
async def broadcast(client, message):
    users = await db.get_all_users()  
    b_msg = message.reply_to_message
    
    status = await message.reply("Starting broadcast...")  
    start_time = time.time()
    
    failed = 0
    sent = 0
    
    for user in users:
        try:
            await broadcast_messages(int(user['id']), b_msg) 
            sent += 1
            await asyncio.sleep(2)  
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            failed += 1
            print(f"Failed for {user['id']}")
            
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await status.edit_text(f"Broadcast completed:\nSent to {sent} users\nFailed for {failed} users\nTook {time_taken} seconds")
