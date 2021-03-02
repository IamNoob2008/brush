import discord
import sys
import os
import traceback
import json
import jishaku
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
from keep_alive import keep_alive

def get_prefix(bot, message):
  if not message.guild:
    return commands.when_mentioned_or("--")(bot, message)

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  if str(message.guild.id) not in prefixes:
    return commands.when_mentioned_or("--")(bot, message)

  prefix = prefixes[str(message.guild.id)]
  return commands.when_mentioned_or(prefix)(bot, message)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
#bot.remove_command('help')
status = cycle(["--help", "Discord Server, RSGameTech's Official"])

@bot.event
async def on_ready():
  change_status.start()
  print("Bot is online")

@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

bot.owner_ids=[699566190842085439, 730454267533459568]

extensions = ['cogs.GWR_works.mod',
              'cogs.GWR_works.animation'
              'cogs.fun',
              'cogs.animation',
							'cogs.event',
              'cogs.info',
              'cogs.utility',
              'cogs.api',
              'Extras.Chat',
              'Extras.source'
]
if __name__ == '__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(f"Error loading {extension}", file=sys.stderr)
      traceback.print_exc()

keep_alive()
bot.load_extension("jishaku")
bot.run(os.getenv('TOKEN'))
