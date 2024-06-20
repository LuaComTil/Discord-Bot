import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle

#   SET A PREFIX FOR COMMANDS
bot =  commands.Bot(command_prefix=".", intents=discord.Intents.all())

# SET THE MESSAGES IN A CYCLE FOR THE BOT STATUS
bot_status = cycle(["Creating a DELETE without WHERE",
                    "Creating a pointer with a null address",
                    "(WHILE = TRUE) { This bot will sell your server data }"])

#   DEFINE TIME AND RUNS THE STATUS
@tasks.loop(seconds=5)
async def changeStatus():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

#   SET WHEN BOT HAS FINISHED EVERY LOAD
@bot.event
async def on_ready():
    print("Bot prontasso!")
    changeStatus.start()

#   BOT AWNSER A HI / CHECK IF IS RUNNIG FINE
@bot.command()
async def oi(ctx):
    await ctx.send(f"Aoeba {ctx.author.mention} bão?")

#   SETS WHERE THE TOKEN IS
with open("token.txt") as file:
    token = file.read().strip()

#   READ EVERY COG
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

#   START THE APP
async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())
