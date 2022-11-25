import os
os.system("pip install discord.py")
import discord
from discord.ext import commands
import time
import datetime

afk = commands.AutoShardedBot(command_prefix="afk", shard_count=1, selfbot=True)
afk.launch_time = datetime.datetime.utcnow()

token="MTAyMjg3NjY5NzkxOTUwNDQwNQ.GuEQuQ.xEs0YRbZJc5OabBlHVk601bYc9XSQN7rMFa44E"

@afk.event
async def on_ready():
  await afk.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Mentions"), status=discord.Status.dnd, afk=True)
  print(f"\n----- AFK Message Reply SelfBot -----\n\n-> Logged In As {afk.user}\n\n-------------------------------------")
  global StartTime
  StartTime = time.time()

@afk.event
async def on_message(message):
  if afk.user.mentioned_in(message):
    delta_uptime = datetime.datetime.utcnow() - afk.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await message.reply(f"**Hey, User Is AFK Since: `{hours}` hours, `{minutes}` minutes, `{seconds}` seconds!**", mention_author=False)

afk.run(token, bot=False)
